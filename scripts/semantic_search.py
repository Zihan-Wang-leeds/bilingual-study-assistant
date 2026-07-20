"""
语义搜索引擎 — ChromaDB + Sentence Transformers 实现

与 TF-IDF 并存，可渐进升级。无需 TF-IDF 也能独立工作。
"""
import os
import sys
from typing import Optional

try:
    import chromadb
    from chromadb.config import Settings
    HAS_CHROMADB = True
except ImportError:
    HAS_CHROMADB = False

try:
    from sentence_transformers import SentenceTransformer
    HAS_EMBEDDINGS = True
except ImportError:
    HAS_EMBEDDINGS = False

from config import CHROMA_DB_PATH, EMBEDDING_MODEL, TOP_K


class SemanticSearch:
    """基于 ChromaDB + Embedding 的语义搜索引擎。"""

    def __init__(self, db_path: str = None, model_name: str = None):
        self.db_path = db_path or CHROMA_DB_PATH
        self.model_name = model_name or EMBEDDING_MODEL
        self.client = None
        self.embedder = None
        self._ready = False

        if not HAS_CHROMADB:
            print("⚠️  chromadb 未安装，语义搜索不可用。运行: pip install chromadb")
            return
        if not HAS_EMBEDDINGS:
            print("⚠️  sentence-transformers 未安装，语义搜索不可用。运行: pip install sentence-transformers")
            return

        self._init()

    def _init(self):
        """初始化 ChromaDB 客户端和 embedding 模型。"""
        try:
            os.makedirs(self.db_path, exist_ok=True)
            self.client = chromadb.PersistentClient(
                path=self.db_path,
                settings=Settings(anonymized_telemetry=False),
            )
            self.embedder = SentenceTransformer(self.model_name)
            self._ready = True
            print(f"🔍 语义搜索引擎已就绪 (model: {self.model_name})")
        except Exception as e:
            print(f"⚠️  语义搜索初始化失败: {e}")

    @property
    def is_ready(self) -> bool:
        return self._ready

    def get_or_create_collection(self, course_code: str):
        """获取或创建课程的 collection。"""
        if not self._ready:
            return None
        name = _sanitize_collection_name(course_code)
        try:
            return self.client.get_or_create_collection(name=name)
        except Exception:
            # 如果已存在但 schema 不同，删除重建
            try:
                self.client.delete_collection(name=name)
            except Exception:
                pass
            return self.client.create_collection(name=name)

    def add_chunks(self, course_code: str, chunks: list[dict]) -> int:
        """
        将分块添加到语义索引。

        Args:
            course_code: 课程代码
            chunks: [{"content": str, "metadata": {...}}, ...]

        Returns:
            添加的块数量
        """
        if not self._ready or not chunks:
            return 0

        collection = self.get_or_create_collection(course_code)
        if not collection:
            return 0

        # 生成 embeddings
        texts = [c["content"] for c in chunks]
        embeddings = self.embedder.encode(texts, show_progress_bar=False).tolist()

        # 生成 IDs
        ids = [f"{course_code}_{c['metadata'].get('chunk_index', i)}"
               for i, c in enumerate(chunks)]

        # 元数据（ChromaDB 只接受 str/int/float/bool）
        metadatas = []
        for c in chunks:
            meta = {}
            for k, v in c["metadata"].items():
                if isinstance(v, (str, int, float, bool)):
                    meta[k] = v
                else:
                    meta[k] = str(v)
            metadatas.append(meta)

        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas,
        )

        print(f"  🧠 语义索引: [{course_code}] 已添加 {len(chunks)} 个向量")
        return len(chunks)

    def search(self, query: str, course_code: str = None, top_k: int = None) -> list[dict]:
        """
        语义搜索。

        Args:
            query: 查询文本
            course_code: 限定课程（可选），不指定则搜索全部
            top_k: 返回结果数

        Returns:
            [{"content": str, "metadata": {...}, "score": float}, ...]
        """
        if not self._ready:
            return []

        top_k = top_k or TOP_K
        query_embedding = self.embedder.encode([query], show_progress_bar=False).tolist()

        if course_code:
            collection = self.get_or_create_collection(course_code)
            if not collection:
                return []
            results = collection.query(
                query_embeddings=query_embedding,
                n_results=top_k,
                include=["documents", "metadatas", "distances"],
            )
        else:
            # 搜索所有课程：分别查询每个 collection 并合并
            all_results = []
            for coll_name in self._list_collections():
                collection = self.client.get_collection(name=coll_name)
                r = collection.query(
                    query_embeddings=query_embedding,
                    n_results=top_k,
                    include=["documents", "metadatas", "distances"],
                )
                for i in range(len(r["ids"][0])):
                    all_results.append({
                        "content": r["documents"][0][i],
                        "metadata": r["metadatas"][0][i],
                        "score": round(1 - r["distances"][0][i], 4),  # distance → similarity
                    })
            # 按相似度排序，取 top_k
            all_results.sort(key=lambda x: -x["score"])
            return all_results[:top_k]

        # 单课程结果格式化
        formatted = []
        if results and results["ids"] and results["ids"][0]:
            for i in range(len(results["ids"][0])):
                score = 1 - results["distances"][0][i] if results.get("distances") else 0
                formatted.append({
                    "content": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i],
                    "score": round(score, 4),
                })

        # 按页码排序（保持课件原始顺序）
        formatted.sort(key=lambda r: r["metadata"].get("page_start", r["metadata"].get("section", 999)))
        return formatted

    def _list_collections(self) -> list[str]:
        """列出所有 collection 名称。"""
        if not self._ready:
            return []
        try:
            return self.client.list_collections()
        except Exception:
            return []

    def list_courses(self) -> list[str]:
        """列出已索引的课程（从 collection 名反推）。"""
        return [c for c in self._list_collections()]

    def delete_course(self, course_code: str):
        """删除课程的所有语义索引。"""
        if not self._ready:
            return
        name = _sanitize_collection_name(course_code)
        try:
            self.client.delete_collection(name=name)
            print(f"  🗑️  语义索引已删除: {course_code}")
        except Exception:
            pass


def _sanitize_collection_name(name: str) -> str:
    """ChromaDB collection 名称要求：3-63字符，字母数字+连字符+下划线。"""
    import re
    safe = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    safe = safe.strip('_')
    if len(safe) < 3:
        safe = safe + "_collection"
    return safe[:63]
