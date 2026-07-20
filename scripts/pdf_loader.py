"""
PDF 课件加载器 - 从PDF提取结构化文本、表格和章节结构

改进项（基于 pdf-harvester 模式）：
  1. PyMuPDF (fitz) 作为主提取引擎，保留布局信息，速度更快
  2. pdfplumber 表格提取 → Markdown 表格
  3. 字体大小/粗体检测 → 自动识别章节标题
  4. 扫描版 PDF 检测 → 提示 OCR 需求
  5. PyPDF2 作为回退方案
"""
import os
import re
from typing import Optional

# --- 主引擎：PyMuPDF (fitz) ---
try:
    import fitz  # PyMuPDF
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False

# --- 表格提取：pdfplumber ---
try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False

# --- 回退：PyPDF2 ---
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path: str, method: str = "auto") -> list[dict]:
    """
    从PDF提取文本，返回每页的文本和页码。

    Args:
        pdf_path: PDF 文件路径
        method: "fitz" | "pypdf2" | "auto" (默认自动选最优)

    返回格式: [{"page": 1, "text": "..."}, ...]
    """
    if not os.path.exists(pdf_path):
        print(f"[ERROR] 文件不存在: {pdf_path}")
        return []

    if method == "auto":
        method = "fitz" if HAS_FITZ else "pypdf2"

    if method == "fitz" and HAS_FITZ:
        pages = _extract_with_fitz(pdf_path)
    else:
        pages = _extract_with_pypdf2(pdf_path)

    # 清理多余空白
    for p in pages:
        p["text"] = re.sub(r'\n{4,}', '\n\n\n', p["text"])
        p["text"] = re.sub(r' {2,}', ' ', p["text"])
        p["text"] = p["text"].strip()

    print(f"[OK] Extracted {len(pages)} pages from {os.path.basename(pdf_path)} (engine: {method})")
    return pages


def _extract_with_fitz(pdf_path: str) -> list[dict]:
    """使用 PyMuPDF (fitz) 提取，保留布局信息。"""
    doc = fitz.open(pdf_path)
    pages = []

    for i, page in enumerate(doc):
        # get_text("text") 保留换行和缩进，比 PyPDF2 更准确
        text = page.get_text("text")
        # 同时获取 blocks 信息供后续结构分析
        blocks = page.get_text("dict")["blocks"]

        pages.append({
            "page": i + 1,
            "text": text,
            "blocks": blocks,          # 内部使用，保留布局信息
            "width": page.rect.width,
            "height": page.rect.height,
        })

    doc.close()
    return pages


def _extract_with_pypdf2(pdf_path: str) -> list[dict]:
    """PyPDF2 回退方案。"""
    reader = PdfReader(pdf_path)
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and text.strip():
            pages.append({
                "page": i + 1,
                "text": text.strip(),
                "blocks": [],
                "width": 0,
                "height": 0,
            })

    return pages


# --- 结构提取（基于 pdf-harvester 的 extract_with_structure 模式） ---

def extract_with_structure(pdf_path: str) -> dict:
    """
    提取 PDF 文本 + 自动检测标题结构。

    使用字体大小和粗体来识别标题层级，无需硬编码目录。
    适用于课件 PDF（Slide 标题通常字号更大/加粗）。

    返回:
        {
            "total": 总页数,
            "pages": [{
                "page": 页码,
                "text": 纯文本,
                "headings": [{"text": 标题文本, "level": 1|2, "font_size": 字号}],
                "paragraphs": [段落文本],
            }],
            "outline": [{"title": 标题, "page": 页码, "level": 层级}],  # 文档大纲
        }
    """
    if not HAS_FITZ:
        print("[WARNING] extract_with_structure 需要 PyMuPDF (fitz)，回退到 PyPDF2")
        pages = extract_text_from_pdf(pdf_path, method="pypdf2")
        return {
            "total": len(pages),
            "pages": [{"page": p["page"], "text": p["text"], "headings": [], "paragraphs": []} for p in pages],
            "outline": [],
        }

    doc = fitz.open(pdf_path)
    pages_out = []
    outline = []

    for i, page in enumerate(doc):
        page_num = i + 1
        blocks = page.get_text("dict")["blocks"]
        page_text = page.get_text("text")

        headings = []
        paragraphs = []
        current_para = []

        for block in blocks:
            if block["type"] != 0:  # 非文本块（图片等），跳过
                continue

            for line in block.get("lines", []):
                line_text = ""
                font_sizes = []
                is_bold = False

                for span in line.get("spans", []):
                    line_text += span["text"]
                    font_sizes.append(span["size"])
                    if "bold" in span["font"].lower() or "Bold" in span["font"]:
                        is_bold = True

                line_text = line_text.strip()
                if not line_text:
                    if current_para:
                        paragraphs.append(" ".join(current_para))
                        current_para = []
                    continue

                avg_font_size = sum(font_sizes) / len(font_sizes) if font_sizes else 12

                # 标题检测规则（来自 pdf-harvester 模式）:
                #   Level 1: 字号 > 18 或 (字号 > 14 且加粗) → 主标题
                #   Level 2: 字号 > 14 或 加粗 → 子标题
                if avg_font_size > 18 or (avg_font_size > 14 and is_bold):
                    if current_para:
                        paragraphs.append(" ".join(current_para))
                        current_para = []
                    headings.append({
                        "text": line_text,
                        "level": 1 if avg_font_size > 18 else 2,
                        "font_size": round(avg_font_size, 1),
                        "page": page_num,
                    })
                    # 加入大纲（每个标题只记首次出现）
                    if not any(o["title"] == line_text for o in outline):
                        outline.append({
                            "title": line_text,
                            "page": page_num,
                            "level": 1 if avg_font_size > 18 else 2,
                        })
                elif avg_font_size > 14 or is_bold:
                    if current_para:
                        paragraphs.append(" ".join(current_para))
                        current_para = []
                    headings.append({
                        "text": line_text,
                        "level": 2,
                        "font_size": round(avg_font_size, 1),
                        "page": page_num,
                    })
                else:
                    current_para.append(line_text)

        if current_para:
            paragraphs.append(" ".join(current_para))

        pages_out.append({
            "page": page_num,
            "text": page_text.strip(),
            "headings": headings,
            "paragraphs": paragraphs,
        })

    doc.close()

    print(f"[OK] 结构提取完成: {len(pages_out)} 页, {len(outline)} 个标题")
    return {
        "total": len(pages_out),
        "pages": pages_out,
        "outline": outline,
    }


# --- 表格提取（基于 pdf-harvester 的 table_to_markdown 模式）---

def extract_tables_from_pdf(pdf_path: str) -> list[dict]:
    """
    从 PDF 中提取所有表格，转为 Markdown 格式。

    返回:
        [{
            "page": 页码,
            "table_index": 该页第几张表,
            "rows": 行数,
            "cols": 列数,
            "markdown": Markdown 表格字符串,
        }]
    """
    if not HAS_PDFPLUMBER:
        print("[WARNING] 表格提取需要 pdfplumber，请: pip install pdfplumber")
        return []

    tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            page_tables = page.extract_tables()
            for t_idx, table in enumerate(page_tables):
                if not table or len(table) < 2:  # 至少要有表头+1行数据
                    continue

                markdown = _table_to_markdown(table)
                if not markdown:
                    continue

                tables.append({
                    "page": page_num,
                    "table_index": t_idx + 1,
                    "rows": len(table),
                    "cols": len(table[0]) if table[0] else 0,
                    "markdown": markdown,
                })

    print(f"[OK] 提取了 {len(tables)} 个表格 from {os.path.basename(pdf_path)}")
    return tables


def _table_to_markdown(table: list) -> str:
    """将二维表数据转为 Markdown 表格（来自 pdf-harvester 模式）。"""
    if not table or len(table) == 0:
        return ""

    def clean_cell(cell):
        if cell is None:
            return ""
        return str(cell).replace("\n", " ").strip()

    headers = [clean_cell(c) for c in table[0]]
    if not any(headers):  # 全是空表头
        return ""

    md = "| " + " | ".join(headers) + " |\n"
    md += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    for row in table[1:]:
        cells = [clean_cell(c) for c in row]
        while len(cells) < len(headers):
            cells.append("")
        if not any(cells):  # 跳过全空行
            continue
        md += "| " + " | ".join(cells[:len(headers)]) + " |\n"

    return md


# --- 扫描版检测（来自 pdf-harvester 的 is_scanned_pdf 模式）---

def is_scanned_pdf(pdf_path: str) -> bool:
    """
    检测 PDF 是否为扫描版（图片为主，无可提取文本）。

    检查前3页的文本量：如果平均每页 < 100 字符，判定为扫描版。
    """
    if not HAS_FITZ:
        return False

    doc = fitz.open(pdf_path)
    total_text = 0

    for page in doc[:min(3, len(doc))]:
        text = page.get_text().strip()
        total_text += len(text)

    page_count = len(doc)
    doc.close()
    return (total_text / min(3, page_count)) < 100


# --- 以下保持与原有 API 兼容 ---

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
        "first_pages_preview": first_pages_text[:500],
    }

    # 尝试匹配课程代码
    code_match = re.search(r'(MATH\d{4}|COMP\d{4}|STAT\d{4})', first_pages_text)
    if code_match:
        info["course_code"] = code_match.group(1)

    # 尝试匹配课程名称
    name_match = re.search(
        r'(\w[\w\s&]+(?:Processes|Analysis|Statistics|Mathematics|Methods|Models|Theory))',
        first_pages_text,
    )
    if name_match:
        info["course_name"] = name_match.group(1).strip()

    # 新增：自动检测标题结构
    if HAS_FITZ:
        structure = extract_with_structure(pdf_path)
        info["detected_outline"] = structure["outline"]
        info["scanned"] = is_scanned_pdf(pdf_path)

    return info


if __name__ == "__main__":
    # 测试
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    pdf_path = "../课程/MATH2702/课件.pdf"
    if not os.path.exists(pdf_path):
        # 尝试绝对路径
        base = os.path.dirname(os.path.abspath(__file__))
        pdf_path = os.path.join(base, "../课程/MATH2702/课件.pdf")

    print("=" * 60)
    print("1. 基本提取测试")
    print("=" * 60)
    pages = extract_text_from_pdf(pdf_path)
    print(f"  总页数: {len(pages)}")
    print(f"  第1页前150字符: {pages[0]['text'][:150]}")

    print("\n" + "=" * 60)
    print("2. 结构提取测试")
    print("=" * 60)
    structure = extract_with_structure(pdf_path)
    print(f"  检测到 {len(structure['outline'])} 个标题:")
    for o in structure['outline'][:10]:
        indent = "  " * (o['level'] - 1)
        print(f"  {indent}Page {o['page']}: {o['title'][:60]}")

    print("\n" + "=" * 60)
    print("3. 表格提取测试")
    print("=" * 60)
    tables = extract_tables_from_pdf(pdf_path)
    print(f"  提取了 {len(tables)} 个表格")
    if tables:
        print(f"  第1个表格 (Page {tables[0]['page']}):")
        print(tables[0]['markdown'][:300])

    print("\n" + "=" * 60)
    print("4. 扫描版检测")
    print("=" * 60)
    print(f"  is_scanned: {is_scanned_pdf(pdf_path)}")
