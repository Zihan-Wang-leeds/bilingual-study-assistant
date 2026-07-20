"""
PDF 课件加载器 - 从PDF提取结构化文本
"""
import os
import re
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path: str) -> list[dict]:
    """
    从PDF提取文本，返回每页的文本和页码。

    返回格式: [{"page": 1, "text": "..."}, ...]
    """
    reader = PdfReader(pdf_path)
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and text.strip():
            # 清理多余空白
            text = re.sub(r'\n{3,}', '\n\n', text)
            text = re.sub(r' {2,}', ' ', text)
            pages.append({
                "page": i + 1,
                "text": text.strip()
            })

    print(f"[OK] Extracted {len(pages)} pages from {os.path.basename(pdf_path)}")
    return pages


def extract_full_text(pdf_path: str) -> str:
    """提取PDF全部文本为一个字符串。"""
    pages = extract_text_from_pdf(pdf_path)
    return "\n\n".join(f"[第{p['page']}页]\n{p['text']}" for p in pages)


def extract_course_info(pdf_path: str) -> dict:
    """
    从PDF提取课程基本信息（课程代码、名称、教师等）。
    通常在前几页。
    """
    pages = extract_text_from_pdf(pdf_path)
    first_pages_text = "\n".join(p['text'] for p in pages[:5])

    info = {
        "filename": os.path.basename(pdf_path),
        "total_pages": len(pages),
        "first_pages_preview": first_pages_text[:500]
    }

    # 尝试匹配课程代码
    code_match = re.search(r'(MATH\d{4}|COMP\d{4}|STAT\d{4})', first_pages_text)
    if code_match:
        info["course_code"] = code_match.group(1)

    # 尝试匹配课程名称
    name_match = re.search(r'(\w[\w\s&]+(?:Processes|Analysis|Statistics|Mathematics|Methods|Models|Theory))',
                           first_pages_text)
    if name_match:
        info["course_name"] = name_match.group(1).strip()

    return info


if __name__ == "__main__":
    # 测试
    pdf_path = "../课程/MATH2702/课件.pdf"
    info = extract_course_info(pdf_path)
    print("📋 课程信息：")
    for k, v in info.items():
        if k != "first_pages_preview":
            print(f"  {k}: {v}")
    print(f"\n📄 前500字符预览：\n{info['first_pages_preview']}")
