"""
索引构建器 - 扫描课程目录，将PDF课件转换为可检索的向量索引
"""
import os
import sys

# 添加 scripts 目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_loader import extract_text_from_pdf, extract_course_info
from chunker import chunk_pdf
from rag_engine import CourseRAG


def find_course_pdfs(courses_dir: str) -> dict:
    """
    扫描课程目录，返回每个课程的PDF文件列表。

    目录结构:
        课程/
        ├── MATH2702/
        │   ├── 课件.pdf
        │   └── 作业.pdf
        ├── COMP2000/
        │   └── ...

    返回: {"MATH2702": ["路径1", "路径2"], ...}
    """
    courses = {}
    if not os.path.exists(courses_dir):
        print(f"⚠️  课程目录不存在: {courses_dir}")
        return courses

    for folder in os.listdir(courses_dir):
        folder_path = os.path.join(courses_dir, folder)
        if os.path.isdir(folder_path):
            pdfs = [
                os.path.join(folder_path, f)
                for f in os.listdir(folder_path)
                if f.lower().endswith('.pdf')
            ]
            if pdfs:
                courses[folder] = pdfs

    return courses


def build_course_index(course_code: str, pdf_paths: list[str],
                       rag: CourseRAG = None, semantic: bool = False) -> int:
    """
    为单个课程构建搜索索引。

    流程: PDF → 提取文本 → 智能分块 → TF-IDF 索引 (+ 语义索引)

    返回: 添加的文档块总数
    """
    if rag is None:
        rag = CourseRAG()

    print(f"\n{'='*60}")
    print(f"📚 正在索引: {course_code}")
    print(f"{'='*60}")

    total_chunks = 0
    course_name = course_code  # 默认使用课程代码

    for pdf_path in pdf_paths:
        filename = os.path.basename(pdf_path)
        print(f"\n📄 处理: {filename}")

        # Step 1: 提取文本
        pages = extract_text_from_pdf(pdf_path)
        if not pages:
            print(f"  ⚠️ 跳过空文件")
            continue

        # Step 2: 提取课程信息
        info = extract_course_info(pdf_path)
        if info.get("course_name"):
            course_name = info["course_name"]
        print(f"  课程名称: {course_name}")

        # Step 3: 智能分块
        chunks = chunk_pdf(pages)
        print(f"  分块数: {len(chunks)}")

        # Step 4: 存入索引（TF-IDF + 可选语义）
        count = rag.add_chunks(course_code, course_name, chunks, semantic=semantic)
        total_chunks += count

    print(f"\n✅ [{course_code}] 索引完成！总计 {total_chunks} 个文档块")
    return total_chunks


def build_all(semantic: bool = False):
    """构建所有课程的索引。"""
    from config import COURSES_DIR

    rag = CourseRAG()
    courses = find_course_pdfs(COURSES_DIR)

    if not courses:
        print("\n📭 没有找到课程PDF文件。")
        print(f"   请将课件PDF放入对应的课程文件夹，例如：")
        print(f"   {COURSES_DIR}/MATH2702/课件.pdf")
        return

    print(f"\n🔍 发现 {len(courses)} 门课程：")
    for code, pdfs in courses.items():
        print(f"  📁 {code}: {len(pdfs)} 个PDF文件")

    for code, pdfs in courses.items():
        build_course_index(code, pdfs, rag, semantic=semantic)

    # 显示最终统计
    print(f"\n{'='*60}")
    print(f"📊 知识库总览")
    print(f"{'='*60}")
    stats = rag.get_course_stats()
    for code, count in stats.items():
        print(f"  🎓 {code}: {count} 个文档块")

    print(f"\n💡 现在可以运行 chat.py 开始提问了！")


def build_course(course_code: str, semantic: bool = False):
    """构建单个课程的索引（增量）。"""
    from config import COURSES_DIR
    course_dir = os.path.join(COURSES_DIR, course_code)
    if not os.path.exists(course_dir):
        print(f"ERROR: Course directory not found: {course_dir}")
        return

    pdfs = [
        os.path.join(course_dir, f)
        for f in os.listdir(course_dir)
        if f.lower().endswith('.pdf')
    ]
    if not pdfs:
        print(f"ERROR: No PDF files found in {course_dir}")
        return

    rag = CourseRAG()
    build_course_index(course_code, pdfs, rag, semantic=semantic)


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Build course search index")
    ap.add_argument("--course", type=str, default=None,
                    help="Build index for a single course (incremental)")
    ap.add_argument("--semantic", action="store_true",
                    help="Also build ChromaDB semantic index (requires: pip install chromadb sentence-transformers)")
    args = ap.parse_args()

    if args.course:
        build_course(args.course, semantic=args.semantic)
    else:
        build_all(semantic=args.semantic)
