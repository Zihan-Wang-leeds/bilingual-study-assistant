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
from openai import OpenAI
from dotenv import load_dotenv

from config import (
    API_KEY, BASE_URL, MODEL_NAME,
    TOP_K, TEMPERATURE, MAX_TOKENS
)

# 允许从项目根目录导入 prompts 模块
import sys as _sys
import os as _os
_project_root = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
if _project_root not in _sys.path:
    _sys.path.insert(0, _project_root)

from prompts.study_modes import get_study_prompt

load_dotenv()

# 存储路径
INDEX_FILE = "knowledge_index.json"


class CourseRAG:
    """基于课程课件的RAG问答系统（TF-IDF版）"""

    def __init__(self, index_path: str = INDEX_FILE):
        # LLM客户端
        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY", API_KEY),
            base_url=BASE_URL
        )

        self.index_path = index_path
        self.courses = {}           # {course_code: {"name": ..., "chunks": [...]}}
        self.vectorizer = None      # TfidfVectorizer实例
        self.tfidf_matrix = None    # TF-IDF矩阵
        self.all_chunks = []        # 所有chunk的扁平列表

        # 如果已有索引文件，加载
        if os.path.exists(index_path):
            self._load_index()

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

    def add_chunks(self, course_code: str, course_name: str, chunks: list[dict]) -> int:
        """将分块后的文档添加到课程知识库。"""
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

        # 重建索引
        self._rebuild_tfidf()
        self._save_index()
        return len(chunks)

    def list_courses(self) -> list[str]:
        """列出已索引的课程。"""
        return list(self.courses.keys())

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
               top_k: int = TOP_K) -> list[dict]:
        """
        检索最相关的课程内容（TF-IDF + 余弦相似度）。

        返回: [{"content": "...", "metadata": {...}, "score": 0.95}, ...]
        """
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

    def ask(self, question: str, course_code: str = None,
            mode: str = "concept", top_k: int = TOP_K) -> dict:
        """
        基于课程内容回答问题。

        参数:
            question: 用户问题
            course_code: 课程代码（可选）
            mode: 回答模式 - "concept"概念解释 | "homework"作业引导 | "review"考前复习

        返回: {"answer": "...", "sources": [...], "mode": "..."}
        """
        # 1. 检索
        relevant_docs = self.search(question, course_code, top_k)

        if not relevant_docs:
            return {
                "answer": "在课程资料中没有找到相关内容。请确认课程代码是否正确，或尝试换一种问法。",
                "sources": [],
                "mode": mode
            }

        # 2. 构建上下文
        context_parts = []
        for i, doc in enumerate(relevant_docs):
            meta = doc["metadata"]
            src_info = f"[来源{i+1}] "
            if "course_name" in meta:
                src_info += f"课程: {meta['course_name']}, "
            if "section_title" in meta:
                src_info += f"Section {meta['section']}: {meta['section_title']}"
            elif "section" in meta:
                src_info += f"Section {meta['section']}"
            context_parts.append(f"{src_info}\n{doc['content']}")
        context = "\n\n---\n\n".join(context_parts)

        # 3. 根据模式选择System Prompt
        system_prompt = get_study_prompt(mode, context)

        # 4. 调用LLM
        answer = self._call_llm(system_prompt, question)

        # 5. 整理来源
        sources = []
        for doc in relevant_docs:
            meta = doc["metadata"]
            sources.append({
                "course": meta.get("course_name", ""),
                "section": meta.get("section", ""),
                "section_title": meta.get("section_title", ""),
                "preview": doc["content"][:200]
            })

        return {
            "answer": answer,
            "sources": sources,
            "mode": mode
        }

    def _call_llm(self, system_prompt: str, question: str) -> str:
        """调用LLM生成回答。"""
        try:
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": question}
                ],
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS
            )
            return normalize_math_answer(response.choices[0].message.content)
        except Exception as e:
            return f"API调用失败: {e}"


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
