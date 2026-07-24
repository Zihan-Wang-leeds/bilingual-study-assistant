"""
索引构建器 - 扫描课程目录，将PDF课件 + Markdown教材转换为可检索的向量索引
"""
import os
import re
import sys

import paths; paths.setup()

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


def find_markdown_guides(course_dir: str) -> list[str]:
    """
    查找课程的 Markdown 自学教材文件（guides/ 目录下的 .md 文件）。

    Args:
        course_dir: 课程文件夹路径（如 课程/MATH2703/）

    Returns:
        排序后的 .md 文件路径列表
    """
    guides_dir = os.path.join(course_dir, "guides")
    if not os.path.exists(guides_dir):
        return []

    md_files = []
    for f in os.listdir(guides_dir):
        if f.lower().endswith('.md'):
            md_files.append(os.path.join(guides_dir, f))
    return sorted(md_files)


def chunk_markdown_file(md_path: str) -> list[dict]:
    """
    将 Markdown 教材按 ## 二级标题分块。

    策略：
      - 整文件作为主 chunk，包含所有内容
      - 按 ## 二级标题切分为子 chunks（适用于大文件）
      - 如果文件较短（< CHUNK_SIZE），作为单一 chunk

    Args:
        md_path: .md 文件路径

    Returns:
        [{"content": str, "metadata": {...}}, ...]
    """
    from config import CHUNK_SIZE

    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    filename = os.path.basename(md_path)
    # 从文件名提取章节标题（如 Section_01_Introduction → Introduction）
    clean_name = filename.replace('.md', '')
    # 尝试提取中文/英文标题
    section_title = clean_name

    chunks = []

    # 按 ## 标题分割
    sections = re.split(r'\n(?=## )', text)
    # 文件开头（第一个 ## 之前的内容）作为 pre-content
    pre_content = ""
    section_parts = []

    for i, section in enumerate(sections):
        if not section.strip():
            continue
        # 第一个 section 可能包含文件开头的介绍
        if i == 0 and not section.strip().startswith('## '):
            pre_content = section.strip()
            continue
        section_parts.append(section.strip())

    # 如果章节很少（<=2），整个文件作为一个块
    if len(section_parts) <= 2:
        chunks.append({
            "content": text.strip(),
            "metadata": {
                "source_file": filename,
                "section_title": section_title,
                "subsection": "",
                "source_type": "markdown_guide",
            }
        })
    else:
        # 每个 ## section 作为一个块
        # 但给每个块前面加上 pre_content 作为上下文
        for i, part in enumerate(section_parts):
            # 提取子标题
            heading_match = re.match(r'^## (.+)$', part, re.MULTILINE)
            subsection = heading_match.group(1).strip() if heading_match else f"Part {i+1}"

            # 太短的块（< 200 chars）合并到下一个
            if len(part) < 200:
                if i + 1 < len(section_parts):
                    section_parts[i+1] = part + "\n\n" + section_parts[i+1]
                continue

            chunks.append({
                "content": part,
                "metadata": {
                    "source_file": filename,
                    "section_title": section_title,
                    "subsection": subsection,
                    "source_type": "markdown_guide",
                }
            })

    return chunks


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

    # 清除旧索引，避免重复累积
    rag.clear_course(course_code)

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

        # Step 4: 存入索引（defer rebuild，批量添加完成后再重建一次）
        count = rag.add_chunks(course_code, course_name, chunks,
                               semantic=semantic, defer_rebuild=True)
        total_chunks += count

    # Step 5: 索引 Markdown 教材（guides/ 目录下）
    if pdf_paths:
        course_dir = os.path.dirname(pdf_paths[0])
    else:
        from config import COURSES_DIR
        course_dir = os.path.join(COURSES_DIR, course_code)

    md_files = find_markdown_guides(course_dir)
    if md_files:
        print(f"\n📝 发现 {len(md_files)} 个 Markdown 教材文件")
        for md_path in md_files:
            md_filename = os.path.basename(md_path)
            md_chunks = chunk_markdown_file(md_path)
            if md_chunks:
                count = rag.add_chunks(course_code, course_name, md_chunks,
                                       semantic=semantic, defer_rebuild=True)
                total_chunks += count
                print(f"  ✅ {md_filename}: {len(md_chunks)} 个块")
    else:
        print(f"\n📝 未发现 Markdown 教材（可选：guides/*.md）")

    # 批量添加完成，一次性重建 TF-IDF 索引
    rag.finalize_index()

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
