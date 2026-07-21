"""
学习教材生成器 - 将课件PDF转化为可离线阅读的双语自学教材

对每个章节：
  PDF页面 → 提取文本 → LLM整理为教学文档 → 保存为Markdown
"""
import os
import sys
import re
import time
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import (
    COURSES_DIR,
    GENERATION_TEMPERATURE, GENERATION_MAX_TOKENS, GENERATION_SLEEP,
)
from pdf_loader import extract_text_from_pdf, extract_with_structure
from llm_client import call_llm_with_prompts

# 输出目录
OUTPUT_DIR = "guides"

# 非章节关键词（词边界匹配，避免 "toc" 误杀 "stochastic"）
_SKIP_KEYWORDS = [
    r'\bcontents?\b', r'\bschedule\b', r'\babout\b', r'\bproblem\s*sheet\b',
    r'\btoc\b', r'\btable\s+of\s+contents\b', r'\boutline\b', r'\bsyllabus\b',
]
_SKIP_PATTERN = re.compile('|'.join(_SKIP_KEYWORDS), re.IGNORECASE)


def _matches_skip_keyword(title: str) -> bool:
    """检查标题是否匹配非章节关键词（词边界匹配）。"""
    return bool(_SKIP_PATTERN.search(title))


class GuideGenerator:
    """将课件转化为自学教材"""

    def __init__(self, course_code: str, pdf_path: str):
        self.course_code = course_code
        self.pdf_path = pdf_path
        self.output_dir = os.path.join(
            os.path.dirname(pdf_path), OUTPUT_DIR
        )

        # 提取所有页面文本
        print(f"Loading PDF: {pdf_path}")
        self.pages = extract_text_from_pdf(pdf_path)
        print(f"  {len(self.pages)} pages loaded")

    # ================================================================
    # Section boundaries detection (auto-detected, no hardcoded list)
    # ================================================================

    def _auto_detect_sections(self) -> list[dict]:
        """
        使用 pdf_loader.extract_with_structure() 自动检测章节边界。

        支持两种课件格式：
          A) MATH2702 式：纯数字 "1" + 紧随标题文字（同一页配对）
          B) MATH2703 式：编号+标题一行 "1. Chapter 1: Introduction"
          C) "Chapter N: Title" 式

        对于 OCR/扫描版 PDF，直接从已提取的文本搜索章节标记。

        返回: [{number, title, start_page, end_page}, ...]
        """
        print("Auto-detecting sections via font/heading analysis...")

        # 快速检测是否为 OCR（self.pages 中前几页的 blocks 是否为空）
        is_likely_ocr = all(
            len(p.get("blocks", [])) == 0
            for p in self.pages[:min(5, len(self.pages))]
        )

        if is_likely_ocr:
            print("  OCR PDF detected — using full-text search for chapter boundaries")
            sections = self._detect_sections_from_full_text()
        else:
            structure = extract_with_structure(self.pdf_path)
            outline = structure["outline"]
            total_pages = structure["total"]

            # 非 OCR 路径：也用文本搜索检查一下
            body_outline = [
                o for o in outline
                if not _matches_skip_keyword(o["title"])
            ]

            if len(body_outline) < 5:
                print(f"  Only {len(body_outline)} headings found — trying full-text search")
                sections = self._detect_sections_from_full_text()
            else:
                sections = self._detect_from_outline(body_outline)

        if not sections:
            print("  WARNING: No sections detected!")

        total_pages = len(self.pages)

        # 排序和去重
        sections.sort(key=lambda s: s["number"])
        seen = set()
        deduped = []
        for s in sections:
            if s["number"] not in seen:
                seen.add(s["number"])
                deduped.append(s)
        sections = deduped

        # 填充 end_page
        for i, s in enumerate(sections):
            if i + 1 < len(sections):
                s["end_page"] = sections[i + 1]["start_page"] - 1
            else:
                s["end_page"] = total_pages

        # 过滤无效范围并合并过短的章节
        valid = [s for s in sections if s["end_page"] >= s["start_page"]]
        valid = self._merge_short_sections(valid)

        print(f"  Auto-detected {len(valid)} sections")
        for s in valid[:5]:
            print(f"    Section {s['number']:2d}: {s['title'][:55]:55s} pages {s['start_page']:3d}-{s['end_page']:3d}")
        if len(valid) > 5:
            print(f"    ... and {len(valid) - 5} more")

        return valid

    def _detect_sections_from_full_text(self) -> list[dict]:
        """
        从 OCR 提取的完整文本中直接搜索章节边界。

        策略：
          1. 从 TOC（第1页）提取章节标题列表
          2. 搜索 "X.1" 模式（如 "1.1", "2.1"）定位每章起始页
          3. 没有 X.1 标记的章节从上下文推断

        返回: [{number, title, start_page, end_page}, ...]
        """
        sections = []
        seen_numbers = set()

        # 1. 从 TOC 提取章节标题
        chapter_titles = self._extract_chapter_titles_from_toc()
        if chapter_titles:
            print(f"  Extracted {len(chapter_titles)} chapter titles from TOC")

        # 2. 搜索 X.1 模式定位章节起始页
        # "1.1 Title" → Chapter 1 starts here
        chapter_start_re = re.compile(r'^(\d{1,2})\.1\s+')
        chapter_starts = {}  # chapter_num → page

        for page in self.pages:
            page_num = page["page"]
            text = page["text"]
            for line in text.split('\n'):
                line = line.strip()
                m = chapter_start_re.match(line)
                if m:
                    chap_num = int(m.group(1))
                    if chap_num not in chapter_starts:
                        chapter_starts[chap_num] = page_num

        # 3. 寻找后续章节（Ch 9-11 可能没有 X.1）
        # Look for Problem Sheet markers or other chapter indicators
        ps_re = re.compile(r'^Problem\s+Sheet\s+(\d+)', re.IGNORECASE)
        for page in self.pages:
            page_num = page["page"]
            text = page["text"]
            for line in text.split('\n'):
                line = line.strip()
                # "Chapter N" standalone on a page
                ch_marker = re.match(r'^Chapter\s+(\d{1,2})$', line, re.IGNORECASE)
                if ch_marker:
                    cn = int(ch_marker.group(1))
                    if cn not in chapter_starts and cn <= 11:
                        chapter_starts[cn] = page_num

        # 4. Build section list from detected starts + TOC titles
        all_chapters = set(range(1, 12))  # Ch 1-11

        # Fill in missing chapters (9, 10, 11 may not have X.1 markers)
        max_page = len(self.pages)
        sorted_starts = sorted(chapter_starts.items())  # [(num, page), ...]

        # Ensure all TOC chapters are represented
        all_chapters = set(chapter_titles.keys()) | set(chapter_starts.keys())
        if not all_chapters:
            all_chapters = set(range(1, 12))

        for chap_num in sorted(all_chapters):
            if chap_num in chapter_starts:
                start_page = chapter_starts[chap_num]
            else:
                # Infer from nearest known chapters using page distribution
                if sorted_starts:
                    prev_chap = None
                    next_chap = None
                    for cn, cp in sorted_starts:
                        if cn < chap_num:
                            prev_chap = (cn, cp)
                        if cn > chap_num and next_chap is None:
                            next_chap = (cn, cp)

                    if prev_chap and next_chap:
                        prev_num, prev_page = prev_chap
                        next_num, next_page = next_chap
                        total_unknown = next_num - prev_num
                        total_pages_avail = next_page - prev_page
                        pages_per_chap = total_pages_avail / total_unknown
                        offset = chap_num - prev_num
                        start_page = prev_page + int(pages_per_chap * offset)
                        # Ensure we don't overlap with next known chapter
                        if start_page >= next_page:
                            start_page = next_page - max(1, total_pages_avail // total_unknown)
                    elif prev_chap:
                        # Distribute remaining pages among trailing chapters
                        _, prev_page = prev_chap
                        trailing_count = sum(1 for c in all_chapters if c > prev_chap[0])
                        if trailing_count > 0:
                            pages_each = max(1, (max_page - prev_page) // trailing_count)
                            offset = chap_num - prev_chap[0]
                            start_page = min(prev_page + pages_each * offset, max_page)
                        else:
                            start_page = min(prev_page + 8, max_page)
                    else:
                        # First chapter not detected — rough estimate
                        start_page = max(1, chap_num * 8)
                else:
                    start_page = max(1, chap_num * 8)

            # Get title from TOC or use default
            title = chapter_titles.get(chap_num, f"Chapter {chap_num}")
            sections.append({
                "number": chap_num,
                "title": title,
                "start_page": min(start_page, max_page),
                "end_page": None,
            })

        # Sort by chapter number
        sections.sort(key=lambda s: s["number"])
        return sections

    def _extract_chapter_titles_from_toc(self) -> dict:
        """
        从 PDF 文本的前几页（通常第1页）提取章节标题。
        匹配 "N. Chapter N: Title" 格式。
        返回: {chapter_number: title, ...}
        """
        titles = {}
        # TOC patterns: "1. Chapter 1: Introduction" or "N. Chapter N: Title"
        toc_re = re.compile(
            r'^(\d{1,2})\.\s*Chapter\s+\d{1,2}[\.:\)]\s*(.+)',
            re.IGNORECASE
        )

        # Search first 5 pages for TOC entries
        for page in self.pages[:5]:
            for line in page["text"].split('\n'):
                line = line.strip()
                if len(line) < 5 or len(line) > 200:
                    continue
                m = toc_re.match(line)
                if m:
                    num = int(m.group(1))
                    title = m.group(2).strip()
                    # Clean up title (remove trailing URLs, etc.)
                    title = re.sub(r'\s*https?://\S+', '', title)
                    title = re.sub(r'\s*file:///\S+', '', title)
                    if len(title) >= 2:
                        titles[num] = title

        return titles

    def _merge_short_sections(self, sections: list[dict]) -> list[dict]:
        """合并过短的章节（< 2页），可能是误检测。"""
        if len(sections) <= 1:
            return sections
        merged = []
        i = 0
        while i < len(sections):
            s = sections[i]
            page_count = s["end_page"] - s["start_page"] + 1
            if page_count < 2 and i + 1 < len(sections):
                # 过短：合并到下一章
                next_s = sections[i + 1]
                next_s["start_page"] = s["start_page"]
                i += 1
                continue
            merged.append(s)
            i += 1
        return merged

    def _detect_from_outline(self, body_outline: list[dict]) -> list[dict]:
        """从 outline 检测章节（原有逻辑，用于非 OCR PDF）。"""
        # 章节匹配模式
        number_pattern = re.compile(r'^(\d{1,2})$')
        numbered_title_pattern = re.compile(
            r'^(\d{1,2})[\.\)]\s*(?:Chapter\s*\d{1,2}[\.:\)]\s*)?(.+)',
            re.IGNORECASE
        )
        chapter_pattern = re.compile(
            r'^Chapter\s+(\d{1,2})[\.:\)\s-]+(.+)',
            re.IGNORECASE
        )
        part_pattern = re.compile(r'^Part\s+[IVX]+', re.IGNORECASE)
        sections = []
        seen_numbers = set()

        # === Pass 1: 尝试格式 B) "N. Chapter N: Title" 或 "N. Title" ===
        for item in body_outline:
            title = item["title"].strip()

            # 跳过 Part 标记
            if part_pattern.match(title):
                continue

            # 格式 B: "1. Title" 或 "1. Chapter 1: Title"
            m = numbered_title_pattern.match(title)
            if m:
                sec_num = int(m.group(1))
                sec_title = m.group(2).strip()
                if sec_num in seen_numbers:
                    continue
                if len(sec_title) < 2:
                    continue
                seen_numbers.add(sec_num)
                sections.append({
                    "number": sec_num,
                    "title": sec_title,
                    "start_page": item["page"],
                    "end_page": None,
                })
                continue

            # 格式 C: "Chapter N: Title"
            m = chapter_pattern.match(title)
            if m:
                sec_num = int(m.group(1))
                sec_title = m.group(2).strip()
                if sec_num in seen_numbers:
                    continue
                seen_numbers.add(sec_num)
                sections.append({
                    "number": sec_num,
                    "title": sec_title,
                    "start_page": item["page"],
                    "end_page": None,
                })

        # === Pass 2: 格式 A) 纯数字 + 同页紧随标题配对 ===
        i = 0
        while i < len(body_outline):
            item = body_outline[i]
            title = item["title"].strip()

            if part_pattern.match(title):
                i += 1
                continue

            m = number_pattern.match(title)
            if m:
                sec_num = int(m.group(1))
                if sec_num in seen_numbers:
                    i += 1
                    continue
                page = item["page"]
                full_title_parts = []

                j = i + 1
                while j < len(body_outline) and body_outline[j]["page"] == page:
                    next_title = body_outline[j]["title"].strip()
                    if number_pattern.match(next_title):
                        break
                    if 'problem sheet' in next_title.lower():
                        j += 1
                        continue
                    full_title_parts.append(next_title)
                    j += 1

                if full_title_parts:
                    full_title = " ".join(full_title_parts)
                    full_title = re.sub(r'-\s+', '', full_title)
                    if len(full_title) >= 3:
                        seen_numbers.add(sec_num)
                        sections.append({
                            "number": sec_num,
                            "title": full_title,
                            "start_page": page,
                            "end_page": None,
                        })
                i = j
            else:
                i += 1

        # 过滤：至少要有实际标题文本
        sections = [s for s in sections if len(s["title"]) >= 2]
        return sections

    # ================================================================
    # Guide generation
    # ================================================================

    def generate_all(self, start_from: int = 1):
        """
        生成所有章节的教材。使用自动检测，无需硬编码章节列表。
        """
        print(f"\nDetecting section boundaries...")
        boundaries = self._auto_detect_sections()
        print(f"  Found {len(boundaries)} sections")

        os.makedirs(self.output_dir, exist_ok=True)
        self._generate_from_boundaries(boundaries, start_from)

    def _generate_from_boundaries(self, boundaries: list[dict], start_from: int = 1):
        """从检测好的章节边界批量生成教材。"""
        # 生成目录
        index_lines = [
            f"# {self.course_code} - 自学教材 / Self-Study Guide",
            "",
            f"**生成时间 / Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            f"**来源 / Source**: {os.path.basename(self.pdf_path)}",
            f"**总章节数 / Total Sections**: {len(boundaries)}",
            "",
            "## 目录 / Table of Contents",
            "",
        ]

        generated = []
        for b in boundaries:
            if b["number"] < start_from:
                continue

            print(f"\n{'='*60}")
            print(f"Generating Section {b['number']}: {b['title']}")
            print(f"  Pages {b['start_page']}-{b['end_page']}")
            print(f"{'='*60}")

            try:
                # 收集该章节的所有页面文本
                section_text = self._collect_section_text(b)

                # 生成教材
                guide_content = self._generate_section_guide(b, section_text)

                # 保存
                filename = f"Section_{b['number']:02d}_{self._safe_filename(b['title'])}.md"
                filepath = os.path.join(self.output_dir, filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(guide_content)

                print(f"  Saved: {filepath}")
                generated.append(b)

                # 添加到目录
                index_lines.append(
                    f"- [Section {b['number']}: {b['title']}]({filename})"
                )

                # 避免API限流
                time.sleep(GENERATION_SLEEP)

            except Exception as e:
                print(f"  ERROR generating Section {b['number']}: {e}")
                index_lines.append(
                    f"- Section {b['number']}: {b['title']} *(生成失败: {e})*"
                )

        # 保存目录
        index_path = os.path.join(self.output_dir, "README.md")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(index_lines))

        print(f"\n{'='*60}")
        print(f"DONE! Generated {len(generated)}/{len(boundaries)} sections")
        print(f"Output: {self.output_dir}")
        print(f"Start reading: {self.output_dir}/README.md")
        print(f"{'='*60}")

    def _collect_section_text(self, boundary: dict) -> str:
        """收集一个章节的所有页面文本。"""
        texts = []
        for page in self.pages:
            if boundary["start_page"] <= page["page"] <= boundary["end_page"]:
                texts.append(f"[Page {page['page']}]\n{page['text']}")
        return "\n\n".join(texts)

    MAX_CHARS_PER_CHUNK = 25000  # ~6000 tokens, 留安全边距

    def _generate_section_guide(self, boundary: dict, section_text: str) -> str:
        """调用LLM生成一个章节的教学教材。长章节自动分段处理后合并。"""
        if len(section_text) <= self.MAX_CHARS_PER_CHUNK:
            return self._generate_single_guide(boundary, section_text)

        # 长章节：在段落边界拆分为多个chunk，分别生成后合并
        chunks = self._split_at_paragraphs(section_text, self.MAX_CHARS_PER_CHUNK)
        print(f"  Long section ({len(section_text)} chars) → {len(chunks)} chunks")

        partial_guides = []
        for i, chunk_text in enumerate(chunks):
            print(f"    Generating chunk {i+1}/{len(chunks)} ({len(chunk_text)} chars)...")
            partial_boundary = dict(boundary)
            partial_boundary["title"] = f"{boundary['title']} (Part {i+1}/{len(chunks)})"
            guide = self._generate_single_guide(partial_boundary, chunk_text)
            partial_guides.append(guide)
            if i < len(chunks) - 1:
                time.sleep(GENERATION_SLEEP // 2)

        # 合并各段
        return self._merge_partial_guides(boundary, partial_guides)

    def _split_at_paragraphs(self, text: str, max_chars: int) -> list[str]:
        """在段落边界将文本拆分为不超过 max_chars 的片段。"""
        paragraphs = text.split("\n\n")
        chunks = []
        current = ""
        for para in paragraphs:
            if len(current) + len(para) > max_chars and current:
                chunks.append(current.strip())
                current = para
            else:
                current += "\n\n" + para if current else para
        if current.strip():
            chunks.append(current.strip())
        return chunks

    def _generate_single_guide(self, boundary: dict, section_text: str) -> str:
        """生成单个章节教材（文本已确保不超过限制）。"""

        prompt = f"""You are a university professor creating self-study materials for Chinese-speaking students studying abroad (留学生).

Below is the RAW course material for ONE section of the course {self.course_code}.

Your task: Transform this raw material into a COMPLETE, SELF-CONTAINED bilingual study guide.

The student learns ALONE from this document - they have no lectures. You must be thorough.

---
RAW COURSE MATERIAL:
{section_text}
---

⚠️ CRITICAL — BILINGUAL FORMAT (中英双语格式):
The FINAL OUTPUT must be a TRUE bilingual document, NOT English with occasional Chinese glosses. Follow these rules STRICTLY:

1. **Every paragraph/section MUST contain SUBSTANTIAL Chinese explanation.** Do NOT write entire paragraphs in English-only. For each concept, provide the Chinese explanation FIRST, followed by the English version, OR interleave Chinese and English sentence by sentence.

2. **Structure pattern for each topic:**
   - 中文解释 (Chinese explanation): Explain the concept in clear Chinese, using plain language the student can understand.
   - English explanation: Provide the same explanation in English, with proper technical terminology.
   - The two should be comparable in depth — do not write a detailed English paragraph and a one-line Chinese summary.

3. **Technical terms format:** "English Term (中文翻译)" on first use. Then freely use either language.

4. **For definitions, theorems, and formulas:** Present them in English first (to match the course notation), then immediately explain in Chinese what it means, why it matters, and how to use it.

5. **For proofs and worked examples:** Explain the logic and each step in Chinese. Keep the mathematical notation in LaTeX as-is.

6. **Headings:** Keep the English heading, followed by " / " and Chinese translation. Example: "### Topic 1: Simple Random Walk / 简单随机游走"

7. **Mathematics:** Use standard LaTeX notation. After every formula, include a compact table explaining each symbol in both languages.
   **CRITICAL: All matrices MUST use LaTeX `\\begin{{pmatrix}}...\\end{{pmatrix}}` — NEVER use Unicode box-drawing characters.**

Example of GOOD bilingual content:
```
#### Intuition / 直觉理解

**中文解释：** 想象一个醉汉在一条直线上行走。每一步，他随机地向左或向右移动一个单位。经过 n 步后，他的位置就是这 n 次随机移动的累计结果。这种模型被称为"随机游走"，是描述随机演化过程的最基本工具。

**English explanation:** Imagine a drunkard walking on a line. At each step, they randomly move left or right by one unit. After n steps, their position is the cumulative result of these n random moves. This model is called a "random walk" and is the most fundamental tool for describing randomly evolving processes.

**Real-world applications / 实际应用：**
- Stock price daily changes / 股票价格每日变动
- Particle diffusion in physics / 物理学中的粒子扩散
```

Example of BAD content (DO NOT DO THIS):
```
A random walk is a stochastic process that describes a path consisting of a succession of random steps. (随机游走是一种随机过程。)
```
↑ This is English-only with a token Chinese summary — NOT acceptable.


## REQUIRED STRUCTURE:

### 📋 Section Overview / 章节概览
- What this section covers, why it matters

### 🎯 Learning Objectives / 学习目标
- 4-6 specific, measurable objectives

### 📚 Prerequisites / 前置知识
- What the student needs to know before starting

### 📖 Core Content / 核心内容

For EACH major topic in the section, provide:

#### Topic X: [Topic Name]
**Intuition / 直觉理解**: Plain language explanation, analogies

**Formal Definition / 形式化定义**: Precise mathematical definition with EVERY symbol explained

**Key Properties / 关键性质**: Theorems, lemmas, important results

**Proof / 证明** (if present in materials): Step-by-step proof with commentary

**Worked Examples / 例题**: Step-by-step solutions showing every calculation

### 🔗 Connections / 知识关联
- How this section connects to previous and future topics

### ⚠️ Common Mistakes / 常见误区
- 3-5 things students typically misunderstand

### ✍️ Practice / 练习
- 3-5 self-test questions with hints (not full answers)

### 📌 Key Takeaways / 要点总结
- 5-8 bullet points summarizing the most important points

---

IMPORTANT RULES:
1. Include EVERY definition, theorem, example, and proof from the raw material
2. Do NOT skip or summarize - the student needs ALL the content
3. Explain every symbol in every formula
4. Use the EXACT notation from the course materials
5. For proofs, explain the logic step by step, don't just copy
6. The guide should be usable WITHOUT referring back to the original PDF"""

        response = call_llm_with_prompts(
            "You are an expert university professor creating truly bilingual (Chinese/English) self-study textbooks for Chinese international students. Every paragraph you write contains substantial content in BOTH languages — Chinese explanations are as detailed as English ones. You NEVER write English-only paragraphs. You are thorough, patient, and include EVERY detail from the source material.",
            prompt,
            temperature=GENERATION_TEMPERATURE,
            max_tokens=GENERATION_MAX_TOKENS,
        )

        content = response

        # 添加文件头
        header = f"""# Section {boundary['number']}: {boundary['title']}

> {self.course_code} - 自学教材 / Self-Study Guide
> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}
> 来源页: {boundary['start_page']}-{boundary['end_page']}

---

"""
        return header + content

    def _merge_partial_guides(self, boundary: dict, partial_guides: list[str]) -> str:
        """
        合并分段生成的教材。对重复的章节标题去重，用分隔线标注分段点。
        """
        if len(partial_guides) == 1:
            return partial_guides[0]

        merged_header = f"""# Section {boundary['number']}: {boundary['title']}

> {self.course_code} - 自学教材
> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}
> 来源页: {boundary['start_page']}-{boundary['end_page']}
> ⚠️ 本章较长，分为 {len(partial_guides)} 部分生成后合并

---

"""
        parts = []
        for i, guide in enumerate(partial_guides):
            # 去除各分段自带的 header（以 "# " 开头的行），避免重复
            lines = guide.split("\n")
            content_start = 0
            # 跳过 frontmatter header（开头以 "# " 或 "> " 开头的行直到 "---"）
            in_header = True
            for j, line in enumerate(lines):
                if in_header and line.strip() == "---":
                    content_start = j + 1
                    in_header = False
                elif in_header and not (line.startswith("# ") or line.startswith("> ")):
                    in_header = False
                    content_start = j
                    break

            content = "\n".join(lines[content_start:]).strip()
            if len(partial_guides) > 1:
                parts.append(f"## Part {i+1}/{len(partial_guides)}\n\n{content}")
            else:
                parts.append(content)

        return merged_header + "\n\n---\n\n".join(parts)

    @staticmethod
    def _safe_filename(title: str) -> str:
        """将标题转为安全的文件名。"""
        safe = re.sub(r'[^\w\s-]', '', title)
        safe = re.sub(r'\s+', '_', safe)
        return safe[:50]


# ================================================================
# Main
# ================================================================

def main():
    import argparse

    ap = argparse.ArgumentParser(
        description="Generate bilingual self-study guides from course PDFs"
    )
    ap.add_argument("--course", type=str, default=None,
                    help="Course code (e.g. MATH2702). Auto-detects if not specified.")
    ap.add_argument("--all", action="store_true", help="Generate ALL sections")
    ap.add_argument("--section", type=int, default=1, help="Generate single section (default: 1)")
    ap.add_argument("--from-section", type=int, default=1, help="Start from section N")
    args = ap.parse_args()

    # Auto-detect course if not specified
    if args.course:
        course_code = args.course
    else:
        # Find all course directories
        courses = [
            d for d in os.listdir(COURSES_DIR)
            if os.path.isdir(os.path.join(COURSES_DIR, d))
        ]
        if not courses:
            print(f"ERROR: No course directories found in {COURSES_DIR}")
            return
        course_code = courses[0]
        if len(courses) > 1:
            print(f"Multiple courses found: {courses}")
            print(f"Using first: {course_code}. Use --course to specify.")
        else:
            print(f"Auto-detected course: {course_code}")

    pdf_path = os.path.join(COURSES_DIR, course_code, "课件.pdf")

    if not os.path.exists(pdf_path):
        print(f"ERROR: PDF not found: {pdf_path}")
        print(f"  Available courses: {[d for d in os.listdir(COURSES_DIR) if os.path.isdir(os.path.join(COURSES_DIR, d))]}")
        return

    gen = GuideGenerator(course_code, pdf_path)

    # Auto-detect section boundaries (no hardcoded list needed)
    print("Auto-detecting section boundaries...")
    all_boundaries = gen._auto_detect_sections()
    print(f"Found {len(all_boundaries)} section boundaries")

    if args.all:
        # Use detected boundaries to generate all
        os.makedirs(gen.output_dir, exist_ok=True)
        gen._generate_from_boundaries(all_boundaries, start_from=args.from_section)
    else:
        # Generate single section for testing
        target_sec = args.section
        boundary = None
        for b in all_boundaries:
            if b["number"] == target_sec:
                boundary = b
                break

        if not boundary:
            print(f"Section {target_sec} not found in PDF")
            print(f"Available sections: {[b['number'] for b in all_boundaries]}")
            return

        os.makedirs(gen.output_dir, exist_ok=True)

        section_text = gen._collect_section_text(boundary)
        title = boundary["title"]
        print(f"Generating guide for Section {boundary['number']}: {title}")
        print(f"  Pages: {boundary['start_page']}-{boundary['end_page']}")
        print(f"  Text length: {len(section_text)} chars")

        guide = gen._generate_section_guide(boundary, section_text)

        filename = f"Section_{boundary['number']:02d}_{gen._safe_filename(title)}.md"
        filepath = os.path.join(gen.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(guide)

        print(f"\nSaved: {filepath}")
        print(f"Length: {len(guide)} chars")


if __name__ == "__main__":
    main()
