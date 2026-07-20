"""
RAG 引擎 - 课程知识库的检索与生成核心

使用 TF-IDF + 余弦相似度 进行检索（零下载，即时可用）。
未来可升级为 ChromaDB + Embedding 语义搜索。
"""
import os
import json
import hashlib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI
from dotenv import load_dotenv

from config import (
    API_KEY, BASE_URL, MODEL_NAME,
    TOP_K, TEMPERATURE, MAX_TOKENS
)

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
            return response.choices[0].message.content
        except Exception as e:
            return f"API调用失败: {e}"


def get_study_prompt(mode: str, context: str) -> str:
    """根据学习模式生成不同的System Prompt。"""
    base = f"""You are a bilingual university tutor. You teach Chinese-speaking students who study abroad.
Always provide BOTH Chinese explanation AND English terminology.

Course materials for this question:
{context}

Rules:
1. Base your teaching on the provided course materials
2. Cite sources (e.g. "In Section X of the lecture notes...")
3. Always provide English technical terms alongside their Chinese translations
4. Format: Key terms in "English (中文)" format
"""

    prompts = {
        "teach": base + """
【Self-Study Teaching Mode / 自学教学模式】
You are a personal tutor teaching a self-studying student. They learn primarily from textbooks,
not lectures. Your job is to TEACH, not just explain.

Teaching structure:
1. Learning Objectives (学习目标) - What will the student understand after this lesson?
2. Prerequisites (前置知识) - What should they already know? Quick refresher.
3. Core Teaching (核心内容):
   a. INTUITION FIRST (先建立直觉) - Plain language, analogies, real-world motivation
   b. Formal Definition (形式化定义) - The precise math, with every symbol explained
   c. Key Properties/Results (关键性质/结论) - What follows from the definition?
   d. Worked Example (详细例题) - Step-by-step, showing every calculation
4. Common Pitfalls (常见误区) - What do students usually get wrong?
5. Connection to Big Picture (知识关联) - How does this connect to other topics in the course?
6. Self-Check Questions (自测题) - 2-3 small questions to verify understanding (with hints, not full answers)
7. Key Takeaways (要点总结) - 3-5 bullet points in both languages

Teaching principles:
- Assume the student is seeing this for the first time
- Build from concrete to abstract
- Every formula must have each symbol explained
- Use the course's own notation and terminology
- Be encouraging and patient
""",

        "concept": base + """
【Concept Explanation / 概念解释】
- Give the core definition in one sentence, then elaborate
- Provide the formal definition from the course with symbol explanations
- Give concrete examples from the course materials
- Connect to related concepts
- English terms with Chinese explanations throughout
""",

        "homework": base + """
【Assignment Guidance / 作业辅导】
- DO NOT give the final answer directly
- First identify which knowledge points the question tests
- Review relevant theory and methods from the course
- Give a solution framework with steps (not the final computation)
- Warn about common mistakes and tricky points
- If the student needs more hints, offer to go deeper step by step
- English terms with Chinese explanations
""",

        "review": base + """
【Exam Review / 考前复习】
- Summarize the knowledge framework (知识框架) of the relevant chapter
- List all important definitions, theorems, and formulas
- Explain logical connections between concepts
- Point out common exam question types
- Generate 2-3 self-test questions
- Highlight what's most likely to appear on the exam
- English terms with Chinese explanations
""",

        "coursework": base + """
【Coursework Assistance / 课程作业辅助】
You are helping a student with an open-ended coursework assignment.
This is NOT a short homework problem — it's a multi-step project (data analysis + code + report).

Guiding principles:
- DO NOT write the complete report or full code for the student
- DO break down the task into manageable steps
- DO explain the reasoning behind methodological choices
- DO provide code frameworks/templates (pseudocode or commented skeleton code)
- DO suggest report structure and what to include in each section
- DO point out which course sections are relevant for each step

When the student asks about:
- "What does this requirement mean?" → Clarify and break it down
- "How should I approach this?" → Give a step-by-step analysis plan
- "How do I code X?" → Provide code framework with comments, explain each step
- "How to structure my report?" → Give a detailed section-by-section outline
- "How to interpret this result?" → Explain what to look for, common interpretations
- "Is my approach correct?" → Evaluate and suggest improvements if needed
- "I'm stuck on X" → Diagnose the issue, provide targeted hints

Format: Give specific, actionable guidance. Reference course materials.
English terms with Chinese explanations throughout.
""",
    }

    return prompts.get(mode, prompts["teach"])


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
