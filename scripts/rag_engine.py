"""
RAG 引擎 - 课程知识库的检索与生成核心

使用 TF-IDF + 余弦相似度 进行检索（零下载，即时可用）。
未来可升级为 ChromaDB + Embedding 语义搜索。
"""
import os
import json
import hashlib
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from llm_client import get_client, call_llm, call_llm_with_prompts, call_llm_stream, call_llm_stream_with_prompts

from config import (
    API_KEY, BASE_URL, MODEL_NAME,
    TOP_K, TEMPERATURE, MAX_TOKENS, MODE_MAX_TOKENS
)

# 允许从项目根目录导入 prompts 模块
import sys as _sys
import os as _os
_project_root = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
if _project_root not in _sys.path:
    _sys.path.insert(0, _project_root)

from prompts.study_modes import get_study_prompt

# 存储路径
INDEX_FILE = "knowledge_index.json"


class CourseRAG:
    """基于课程课件的RAG问答系统（TF-IDF版）"""

    def __init__(self, index_path: str = INDEX_FILE):
        self.index_path = index_path
        self.courses = {}           # {course_code: {"name": ..., "chunks": [...]}}
        self.vectorizer = None      # TfidfVectorizer实例
        self.tfidf_matrix = None    # TF-IDF矩阵
        self.all_chunks = []        # 所有chunk的扁平列表
        self.semantic = None        # SemanticSearch 实例（按需加载）

        # 如果已有索引文件，加载
        if os.path.exists(index_path):
            self._load_index()

    def _init_semantic(self):
        """按需加载语义搜索引擎（避免启动时强制依赖 chromadb）。"""
        if self.semantic is None:
            try:
                from semantic_search import SemanticSearch
                self.semantic = SemanticSearch()
            except ImportError:
                self.semantic = False  # 标记为不可用
        return self.semantic if self.semantic else None

    # ================================================================
    # 索引持久化
    # ================================================================

    def _save_index(self):
        """保存索引到JSON文件。"""
        data = {
            "courses": self.courses,
        }
        with open(self.index_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"💾 索引已保存 ({len(self.all_chunks)} 个文档块)")

    def _load_index(self):
        """从JSON文件加载索引。"""
        with open(self.index_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.courses = data.get("courses", {})

        # 重建TF-IDF索引
        self._rebuild_tfidf()
        print(f"📂 索引已加载: {len(self.courses)} 门课程, {len(self.all_chunks)} 个文档块")

    def _rebuild_tfidf(self):
        """重建TF-IDF向量化器和矩阵。"""
        self.all_chunks = []
        for code, course in self.courses.items():
            for chunk in course["chunks"]:
                self.all_chunks.append({
                    "content": chunk["content"],
                    "metadata": {
                        "course_code": code,
                        "course_name": course["name"],
                        **chunk["metadata"]
                    }
                })

        if self.all_chunks:
            texts = [c["content"] for c in self.all_chunks]
            self.vectorizer = TfidfVectorizer(
                max_features=5000,
                ngram_range=(1, 2),  # unigrams + bigrams 对数学术语更好
                stop_words='english',
            )
            self.tfidf_matrix = self.vectorizer.fit_transform(texts)
            print(f"  TF-IDF词汇量: {len(self.vectorizer.get_feature_names_out())}")

    # ================================================================
    # 索引管理
    # ================================================================

    def clear_course(self, course_code: str):
        """清除某个课程的全部索引块（用于重建前清理）。"""
        if course_code in self.courses:
            count = len(self.courses[course_code]["chunks"])
            del self.courses[course_code]
            self._rebuild_tfidf()
            self._save_index()
            print(f"[{course_code}] 已清除 {count} 个旧块")
            return count
        return 0

    def add_chunks(self, course_code: str, course_name: str, chunks: list[dict],
                   semantic: bool = False, defer_rebuild: bool = False) -> int:
        """将分块后的文档添加到课程知识库。

        Args:
            defer_rebuild: True 时跳过 TF-IDF 重建，由调用者在批量添加完成后手动 rebuild。
        """
        if course_code not in self.courses:
            self.courses[course_code] = {
                "name": course_name,
                "chunks": []
            }

        for chunk in chunks:
            self.courses[course_code]["chunks"].append({
                "content": chunk["content"],
                "metadata": chunk["metadata"]
            })

        print(f"[{course_code}] 已添加 {len(chunks)} 个文档块")

        if not defer_rebuild:
            self._rebuild_tfidf()
            self._save_index()

        # 语义索引（如果可用）
        if semantic:
            sem = self._init_semantic()
            if sem and sem.is_ready:
                sem.add_chunks(course_code, chunks)

        return len(chunks)

    def finalize_index(self):
        """重建 TF-IDF 索引并保存（批量添加完成后调用一次）。"""
        self._rebuild_tfidf()
        self._save_index()

    def list_courses(self) -> list[str]:
        """列出已索引的课程。"""
        return list(self.courses.keys())

    def get_course_overview(self, course_code: str) -> str:
        """
        获取课程概览：名称 + 章节列表。
        优先从 Markdown 教材文件名提取（最干净），否则从 PDF chunk 元数据提取。

        用于注入 AI 上下文，让 AI 知道课程的完整结构，
        从而正确映射用户说的「第一章」到具体章节名。
        """
        if course_code not in self.courses:
            return ""

        c = self.courses[course_code]
        name = c.get("name", course_code)

        # 收集 Markdown 教材中的章节标题（更干净）
        md_sections = []
        seen_md = set()
        for chunk in c.get("chunks", []):
            meta = chunk.get("metadata", {})
            if meta.get("source_type") != "markdown_guide":
                continue
            st = meta.get("section_title", "")
            if st and st not in seen_md:
                seen_md.add(st)
                md_sections.append(st)

        # 如果没有 Markdown 章节，从 PDF 元数据提取
        if not md_sections:
            seen = set()
            for chunk in c.get("chunks", []):
                meta = chunk.get("metadata", {})
                st = meta.get("section_title", "")
                # 过滤噪音：至少 8 个字符，不含过多 OCR 错误
                if st and st not in seen and len(st) >= 8:
                    # 过滤明显的 OCR 垃圾（太多单字符/随机字母）
                    words = st.split()
                    if len(words) >= 2 and all(len(w) > 1 for w in words[:4]):
                        seen.add(st)
                        md_sections.append(st)

        if not md_sections:
            return f"Course: {course_code} ({name})"

        lines = [f"当前课程 / Current Course: {course_code} — {name}"]
        lines.append(f"课程章节列表 / Available chapters ({len(md_sections)} total):")
        for i, sec in enumerate(md_sections, 1):
            # 清理文件名格式
            clean = sec.replace('_', ' ')
            lines.append(f"  {i}. {clean}")

        return "\n".join(lines)

    def get_course_stats(self, course_code: str = None) -> dict:
        """获取知识库统计信息。"""
        if course_code:
            if course_code in self.courses:
                return {course_code: len(self.courses[course_code]["chunks"])}
            return {}
        else:
            return {code: len(c["chunks"]) for code, c in self.courses.items()}

    # ================================================================
    # 检索
    # ================================================================

    def search(self, query: str, course_code: str = None,
               top_k: int = TOP_K, use_semantic: bool = False) -> list[dict]:
        """
        检索最相关的课程内容。

        参数:
            use_semantic: True 时使用 ChromaDB 语义搜索（需安装依赖），
                          False 时使用 TF-IDF（零依赖，即时可用）

        返回: [{"content": "...", "metadata": {...}, "score": 0.95}, ...]
        """
        # 尝试语义搜索
        if use_semantic:
            sem = self._init_semantic()
            if sem and sem.is_ready:
                results = sem.search(query, course_code=course_code, top_k=top_k)
                if results:
                    return results
            # Fallback: 语义搜索不可用或结果为空

        # TF-IDF 搜索（默认，零依赖）
        if not self.vectorizer or not self.all_chunks:
            return []

        # 将查询转为TF-IDF向量
        query_vec = self.vectorizer.transform([query])

        # 如果指定了课程，只搜索该课程
        if course_code:
            candidate_indices = [
                i for i, c in enumerate(self.all_chunks)
                if c["metadata"].get("course_code", "").upper() == course_code.upper()
            ]
            if not candidate_indices:
                return []
            candidate_matrix = self.tfidf_matrix[candidate_indices]
            similarities = cosine_similarity(query_vec, candidate_matrix)[0]
            # 取 top_k
            top_indices = np.argsort(similarities)[::-1][:top_k]
            results = []
            for idx in top_indices:
                if similarities[idx] > 0:  # 过滤完全无关的结果
                    orig_idx = candidate_indices[idx]
                    results.append({
                        "content": self.all_chunks[orig_idx]["content"],
                        "metadata": self.all_chunks[orig_idx]["metadata"],
                        "score": round(float(similarities[idx]), 4)
                    })
            # 按页码排序，保持课件原始顺序
            results.sort(key=lambda r: r["metadata"].get("page_start", r["metadata"].get("section", 999)))
            return results
        else:
            # 搜索全部课程
            similarities = cosine_similarity(query_vec, self.tfidf_matrix)[0]
            top_indices = np.argsort(similarities)[::-1][:top_k]
            results = []
            for idx in top_indices:
                if similarities[idx] > 0:
                    results.append({
                        "content": self.all_chunks[idx]["content"],
                        "metadata": self.all_chunks[idx]["metadata"],
                        "score": round(float(similarities[idx]), 4)
                    })
            # 按页码排序，保持课件原始顺序
            results.sort(key=lambda r: r["metadata"].get("page_start", r["metadata"].get("section", 999)))
            return results

    # ================================================================
    # 生成
    # ================================================================

    def _build_context(self, question: str, course_code: str = None,
                       top_k: int = TOP_K) -> tuple:
        """构建检索上下文 + 来源列表（ask / ask_stream 共用）。"""
        relevant_docs = self.search(question, course_code, top_k)

        course_overview = ""
        if course_code:
            course_overview = self.get_course_overview(course_code)
        elif len(self.courses) == 1:
            course_overview = self.get_course_overview(list(self.courses.keys())[0])

        if relevant_docs:
            context_parts = []
            if course_overview:
                context_parts.append(f"[课程信息 / Course Info]\n{course_overview}")
            for i, doc in enumerate(relevant_docs):
                meta = doc["metadata"]
                src_info = f"[来源{i+1}] "
                if "course_name" in meta:
                    src_info += f"课程: {meta['course_name']}, "
                if "section_title" in meta:
                    src_info += f"Section {meta.get('section', '?')}: {meta['section_title']}"
                elif "section" in meta:
                    src_info += f"Section {meta['section']}"
                context_parts.append(f"{src_info}\n{doc['content']}")
            context = "\n\n---\n\n".join(context_parts)
        else:
            context = "[未在课件中找到直接相关内容 / No directly relevant content found in course materials]"
            if course_overview:
                context = f"[课程信息 / Course Info]\n{course_overview}\n\n{context}"

        sources = []
        for doc in relevant_docs:
            meta = doc["metadata"]
            sources.append({
                "course": meta.get("course_name", ""),
                "section": meta.get("section", ""),
                "section_title": meta.get("section_title", ""),
                "preview": doc["content"][:200]
            })
        return context, sources

    def ask(self, question: str, course_code: str = None,
            mode: str = "concept", top_k: int = TOP_K,
            history: list[dict] = None) -> dict:
        """
        基于课程内容回答问题。

        参数:
            question: 用户问题
            course_code: 课程代码（可选）
            mode: 回答模式 - "teach"|"concept"|"homework"|"review"|"coursework"
            history: 对话历史 [{"role": "user/assistant", "content": "..."}]

        返回: {"answer": "...", "sources": [...], "mode": "..."}
        """
        # 1. 检索 + 构建上下文
        context, sources = self._build_context(question, course_code, top_k)

        # 2. 构建消息
        system_prompt = get_study_prompt(mode, context)
        messages = [{"role": "system", "content": system_prompt}]
        if history:
            for turn in history[-12:]:
                messages.append({"role": turn["role"], "content": turn["content"]})
        messages.append({"role": "user", "content": question})

        # 3. 调用LLM
        max_tok = MODE_MAX_TOKENS.get(mode, MAX_TOKENS)
        answer = call_llm(messages, temperature=TEMPERATURE, max_tokens=max_tok)

        return {"answer": normalize_math_answer(answer), "sources": sources, "mode": mode}

    def ask_stream(self, question: str, course_code: str = None,
                   mode: str = "concept", top_k: int = TOP_K,
                   history: list[dict] = None):
        """
        流式版本 ask() — 逐个 token yield。

        先 yield ("meta", dict) 元数据，然后逐 ("token", str) yield 回答文本。
        Yields:
            ("meta", {"sources": [...], "mode": "..."})  — 元数据
            ("token", str)                                 — 逐个 delta 文本
        """
        # 1. 检索 + 构建上下文
        context, sources = self._build_context(question, course_code, top_k)
        yield ("meta", {"sources": sources, "mode": mode})

        # 2. 构建消息
        system_prompt = get_study_prompt(mode, context)
        messages = [{"role": "system", "content": system_prompt}]
        if history:
            for turn in history[-12:]:
                messages.append({"role": turn["role"], "content": turn["content"]})
        messages.append({"role": "user", "content": question})

        # 3. 流式生成
        max_tok = MODE_MAX_TOKENS.get(mode, MAX_TOKENS)
        for delta in call_llm_stream(
            messages=messages,
            temperature=TEMPERATURE,
            max_tokens=max_tok,
        ):
            yield ("token", delta)


def normalize_math_answer(answer: str) -> str:
    """Clean up common raw TeX patterns before the browser renders Markdown."""
    if not answer:
        return answer

    answer = _convert_bare_bracket_math(answer)
    answer = _wrap_standalone_math_lines(answer)
    return answer


def _convert_bare_bracket_math(text: str) -> str:
    """Convert equation blocks written as bare [ ... ] into MathJax blocks."""
    pattern = re.compile(r'(^|\n)\s*\[\s*\n([\s\S]*?)\n\s*\]\s*(?=\n|$)')

    def repl(match):
        prefix, body = match.group(1), match.group(2).strip()
        if _looks_like_math(body):
            return f"{prefix}\\[\n{body}\n\\]\n"
        return match.group(0)

    return pattern.sub(repl, text)


def _wrap_standalone_math_lines(text: str) -> str:
    r"""Wrap raw equation lines such as X_n = X_0 + \sum... in display math."""
    lines = text.splitlines()
    output = []
    in_fence = False
    in_display_math = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            output.append(line)
            continue

        if stripped in {"\\[", "$$"}:
            in_display_math = True
            output.append(line)
            continue
        if stripped in {"\\]", "$$"}:
            in_display_math = False
            output.append(line)
            continue

        if not in_fence and not in_display_math and _is_raw_equation_line(stripped):
            output.append("\\[")
            output.append(stripped)
            output.append("\\]")
        else:
            output.append(line)

    return "\n".join(output)


def _is_raw_equation_line(line: str) -> bool:
    if not line or line.startswith(("#", "-", "*", "|", ">", "\\(", "\\[")):
        return False
    if len(line) > 140:
        return False
    if re.search(r'\\(sum|prod|frac|sqrt|mathbb|mathbf|alpha|beta|gamma|lambda|pi|infty)', line):
        return True
    return bool(re.search(r'[A-Za-z]_\{?[A-Za-z0-9]+\}?\s*=', line))


def _looks_like_math(text: str) -> bool:
    return bool(re.search(r'\\[A-Za-z]+|[_^{}=+\-*/]|[A-Z]_\w', text))


if __name__ == "__main__":
    rag = CourseRAG()

    print("\n知识库状态：")
    stats = rag.get_course_stats()
    if stats:
        for code, count in stats.items():
            print(f"  {code}: {count} 个文档块")
    else:
        print("  （空 - 请先运行 build_index.py 导入课件）")

    if stats:
        print("\n" + "=" * 60)
        print("开始问答测试（输入 exit 退出）")
        print("=" * 60)
        while True:
            q = input("\n问题: ").strip()
            if q.lower() == "exit":
                break

            result = rag.ask(q, mode="concept")
            print(f"\n回答:\n{result['answer']}")
            print(f"\n参考来源:")
            for s in result["sources"]:
                print(f"  - Section {s['section']}: {s['section_title']}")
