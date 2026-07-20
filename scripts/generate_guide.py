"""
学习教材生成器 - 将课件PDF转化为可离线阅读的双语自学教材

对每个章节：
  PDF页面 → 提取文本 → LLM整理为教学文档 → 保存为Markdown
"""
import os
import sys
import re
import time
import json
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import API_KEY, BASE_URL, MODEL_NAME, COURSES_DIR
from pdf_loader import extract_text_from_pdf

load_dotenv()

# 输出目录
OUTPUT_DIR = "guides"

# MATH2702 section definitions (number, title, key search words)
MATH2702_SECTIONS = [
    (1, "Stochastic Processes and the Markov Property",
     "Stochastic processes and the Markov property"),
    (2, "Random Walk",
     "Random walk"),
    (3, "Discrete Time Markov Chains",
     "Discrete time Markov chains"),
    (4, "Martingales and Gambler's Ruin",
     "Martingales and Gambler"),
    (5, "Examples from Actuarial Science",
     "Examples from actuarial"),
    (6, "Class Structure",
     "Class Structure"),
    (7, "Hitting Times",
     "Hitting times"),
    (8, "Recurrence and Transience",
     "Recurrence and transience"),
    (9, "Stationary Distributions",
     "Stationary distributions"),
    (10, "Reversibility of Markov Chains",
     "Reversibility"),
    (11, "Long-term Behaviour of Markov Chains",
     "Long-term behaviour of Markov ch"),
    (12, "End of Part I: Discrete Time Markov Chains",
     "End of Part I"),
    (13, "Poisson Process with Poisson Increments",
     "Poisson process with Poisson increments"),
    (14, "Poisson Process with Exponential Holding Times",
     "Poisson process with exponential"),
    (15, "Poisson Process in Infinitesimal Time Periods",
     "Poisson process in infinitesimal"),
    (16, "Counting Processes",
     "Counting processes"),
    (17, "Continuous Time Markov Jump Processes",
     "Continuous time Markov jump processes"),
    (18, "Forward and Backward Equations",
     "Forward and backward equations"),
    (19, "Class Structure and Hitting Times (CT)",
     "Class structure and hitting times"),
    (20, "Long-term Behaviour of Markov Jump Processes",
     "Long-term behaviour of Markov jump"),
    (21, "Queues",
     "Queues"),
    (22, "End of Part II: Continuous Time Markov Jump Processes",
     "End of Part II"),
]


class GuideGenerator:
    """将课件转化为自学教材"""

    def __init__(self, course_code: str, pdf_path: str):
        self.course_code = course_code
        self.pdf_path = pdf_path
        self.output_dir = os.path.join(
            os.path.dirname(pdf_path), OUTPUT_DIR
        )

        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY", API_KEY),
            base_url=BASE_URL
        )

        # 提取所有页面文本
        print(f"Loading PDF: {pdf_path}")
        self.pages = extract_text_from_pdf(pdf_path)
        print(f"  {len(self.pages)} pages loaded")

    # ================================================================
    # Section boundaries detection
    # ================================================================

    def _find_section_boundaries(self, sections_def: list[tuple]) -> list[dict]:
        """
        通过扫描页面找到每个章节的起始和结束页。

        返回: [{number, title, start_page, end_page}, ...]
        """
        boundaries = []

        for sec_num, sec_title, search_key in sections_def:
            start_page = self._find_section_start(sec_num, search_key)
            if start_page:
                boundaries.append({
                    "number": sec_num,
                    "title": sec_title,
                    "start_page": start_page,
                    "end_page": None  # 稍后填充
                })

        # 填充 end_page（下一节的起始页 - 1）
        for i, b in enumerate(boundaries):
            if i + 1 < len(boundaries):
                b["end_page"] = boundaries[i + 1]["start_page"] - 1
            else:
                b["end_page"] = len(self.pages)

        # 标记覆盖范围
        covered_pages = set()
        for b in boundaries:
            for p in range(b["start_page"], b["end_page"] + 1):
                covered_pages.add(p)

        # 处理未被覆盖的页面（front matter, problem sheets between sections）
        uncovered = sorted(set(range(1, len(self.pages) + 1)) - covered_pages)
        if uncovered:
            print(f"  Note: {len(uncovered)} pages not in any section (problem sheets, etc.)")

        return boundaries

    def _find_section_start(self, sec_num: int, search_key: str,
                            skip_first_n_pages: int = 6) -> int:
        """
        找到某个章节在PDF中的起始页码。

        skip_first_n_pages: 跳过目录页（TOC会包含所有章节标题，但不是正文开始）
        """
        # 构建搜索模式：行首或换行后的 "数字 标题"
        # 注意：TOC条目通常后面跟"......"页码，正文标题是独立行
        # 排除TOC特征：行中包含 "....." 的TOC条目不是正文
        pattern = re.compile(
            rf'(?:^|\n)\s*{sec_num}\s+{re.escape(search_key[:40])}',
            re.IGNORECASE
        )

        # 从后往前搜索（正文在后，TOC在前），且跳过目录页
        for page in reversed(self.pages):
            if page["page"] <= skip_first_n_pages:
                continue
            text = page["text"]
            if pattern.search(text):
                # 排除TOC条目（含有连续点号的）
                # 检查匹配行是否包含 "...." 特征
                match = pattern.search(text)
                line_start = text.rfind('\n', 0, match.start())
                line_end = text.find('\n', match.end())
                line = text[max(0, line_start):line_end if line_end > 0 else len(text)]
                if '.....' not in line and '·' not in line:
                    return page["page"]

        # 如果严格匹配失败，尝试更宽松的匹配
        words = search_key.split()[:3]
        loose_pattern = re.compile(
            rf'(?:^|\n)\s*{sec_num}\s+.*{re.escape(words[0])}.*{re.escape(words[-1])}',
            re.IGNORECASE
        )
        for page in reversed(self.pages):
            if page["page"] <= skip_first_n_pages:
                continue
            text = page["text"]
            if loose_pattern.search(text):
                match = loose_pattern.search(text)
                line_start = text.rfind('\n', 0, match.start())
                line_end = text.find('\n', match.end())
                line = text[max(0, line_start):line_end if line_end > 0 else len(text)]
                if '.....' not in line:
                    return page["page"]

        print(f"  WARNING: Section {sec_num} '{search_key}' start page not found")
        return None

    # ================================================================
    # Guide generation
    # ================================================================

    def generate_all(self, sections_def: list[tuple] = None,
                     start_from: int = 1):
        """
        生成所有章节的教材。
        """
        if sections_def is None:
            sections_def = MATH2702_SECTIONS

        print(f"\nDetecting section boundaries...")
        boundaries = self._find_section_boundaries(sections_def)
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
                time.sleep(2)

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

    def _generate_section_guide(self, boundary: dict, section_text: str) -> str:
        """调用LLM生成一个章节的教学教材。"""
        # 估算token数，如果太长则截断
        max_chars = 30000  # ~7500 tokens, 安全值
        if len(section_text) > max_chars:
            print(f"  Truncating section text: {len(section_text)} → {max_chars} chars")
            section_text = section_text[:max_chars] + "\n\n[Content truncated due to length]"

        prompt = f"""You are a university professor creating self-study materials for a Chinese-speaking student studying abroad.

Below is the RAW course material for ONE section of the course {self.course_code}.

Your task: Transform this raw material into a COMPLETE, SELF-CONTAINED study guide.

The student learns ALONE from this document - they have no lectures. You must be thorough.

---
RAW COURSE MATERIAL:
{section_text}
---

Generate a comprehensive study guide in the following structure. Use BILINGUAL format throughout:
- Technical terms: "English Term (中文翻译)"
- Explanations: mix of Chinese and English for clarity
- Mathematics: universal notation, explain each symbol

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

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are an expert university professor creating bilingual (Chinese/English) self-study textbooks. You are thorough, patient, and include EVERY detail from the source material."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=6000
        )

        content = response.choices[0].message.content

        # 添加文件头
        header = f"""# Section {boundary['number']}: {boundary['title']}

> {self.course_code} Stochastic Processes - 自学教材
> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}
> 来源页: {boundary['start_page']}-{boundary['end_page']}

---

"""
        return header + content

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
    course_code = "MATH2702"
    pdf_path = os.path.join(COURSES_DIR, course_code, "课件.pdf")

    if not os.path.exists(pdf_path):
        print(f"ERROR: PDF not found: {pdf_path}")
        return

    gen = GuideGenerator(course_code, pdf_path)

    # 先生成Section 1测试效果
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="Generate ALL sections")
    ap.add_argument("--section", type=int, default=1, help="Generate single section (default: 1)")
    ap.add_argument("--from-section", type=int, default=1, help="Start from section N")
    args = ap.parse_args()

    # Always detect all section boundaries first
    print("Detecting all section boundaries...")
    all_boundaries = gen._find_section_boundaries(MATH2702_SECTIONS)
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
