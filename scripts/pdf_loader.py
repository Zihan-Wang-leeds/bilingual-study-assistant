"""
PDF 课件加载器 - 从PDF提取结构化文本、表格和章节结构

改进项（基于 pdf-harvester 模式）：
  1. PyMuPDF (fitz) 作为主提取引擎，保留布局信息，速度更快
  2. pdfplumber 表格提取 → Markdown 表格
  3. 字体大小/粗体检测 → 自动识别章节标题
  4. 扫描版 PDF 检测 → OCR (Tesseract) 自动回退
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

# --- OCR 支持 ---
try:
    from pdf2image import convert_from_path
    HAS_PDF2IMAGE = True
except ImportError:
    HAS_PDF2IMAGE = False

try:
    import pytesseract
    HAS_TESSERACT = True
    # Windows: auto-detect Tesseract installation
    # pytesseract 默认 tesseract_cmd='tesseract'（仅 PATH 中有用时生效）
    # Windows 用户常需手动指定安装路径
    _candidates = [
        r'C:\Program Files\Tesseract-OCR\tesseract.exe',
        r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
    ]
    for _path in _candidates:
        if os.path.exists(_path):
            pytesseract.pytesseract.tesseract_cmd = _path
            break
except ImportError:
    HAS_TESSERACT = False


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

    # 扫描版/图片型 PDF 检测：如果文本提取结果为空或极少，自动回退到 OCR
    if not _has_meaningful_text(pages) and HAS_PDF2IMAGE and HAS_TESSERACT:
        print(f"[INFO] 检测到扫描版/图片型 PDF，自动切换为 OCR 模式...")
        ocr_pages = _extract_with_ocr(pdf_path)
        if ocr_pages and _has_meaningful_text(ocr_pages):
            pages = ocr_pages
            print(f"[OK] OCR 完成: 提取了 {len(pages)} 页文本")
        else:
            print("[WARN] OCR 也未提取到足够文本，请检查 PDF 质量")

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


def _render_pdf_to_images(pdf_path: str, dpi: int = 250) -> list:
    """
    将 PDF 渲染为 PIL Image 列表。
    优先使用 pdf2image (poppler)，不可用时回退到 PyMuPDF (fitz)。
    """
    # 方法 1: pdf2image + poppler（最佳质量）
    if HAS_PDF2IMAGE:
        try:
            return convert_from_path(pdf_path, dpi=dpi)
        except Exception as e:
            print(f"  [INFO] pdf2image 失败 ({e})，回退到 PyMuPDF...")

    # 方法 2: PyMuPDF (fitz) 内置渲染（Windows 无需装 poppler）
    if HAS_FITZ:
        try:
            from PIL import Image
            import io
            doc = fitz.open(pdf_path)
            images = []
            zoom = dpi / 72  # fitz 默认 72 DPI
            for i in range(len(doc)):
                page = doc[i]
                mat = fitz.Matrix(zoom, zoom)
                pix = page.get_pixmap(matrix=mat)
                img = Image.open(io.BytesIO(pix.tobytes("png")))
                images.append(img)
            doc.close()
            return images
        except Exception as e:
            print(f"  [INFO] PyMuPDF 渲染失败 ({e})")

    print("[ERROR] 无可用的 PDF→图片渲染引擎。请安装 pdf2image+poppler 或 pymupdf")
    return []


def _extract_with_ocr(pdf_path: str, dpi: int = 250) -> list[dict]:
    """
    使用 OCR (Tesseract) 从扫描版/图片型 PDF 提取文本。

    流程：PDF → 图片 → OCR (via pytesseract)
    渲染引擎：pdf2image/poppler 或 PyMuPDF/fitz（自动选择可用引擎）
    """
    if not HAS_TESSERACT:
        print("[ERROR] OCR 需要 pytesseract + Tesseract 系统安装。")
        print("  Windows: https://github.com/UB-Mannheim/tesseract/wiki")
        print("  macOS:   brew install tesseract")
        print("  Linux:   sudo apt install tesseract-ocr")
        return []

    print(f"  OCR mode: converting PDF pages to images (DPI={dpi})...")
    images = _render_pdf_to_images(pdf_path, dpi=dpi)
    if not images:
        return []

    pages = []
    total = len(images)
    print(f"  OCR mode: running Tesseract on {total} pages...")

    for i, img in enumerate(images):
        try:
            text = pytesseract.image_to_string(img, lang='eng')
        except Exception as e:
            print(f"  [WARN] OCR failed on page {i+1}: {e}")
            text = ""

        pages.append({
            "page": i + 1,
            "text": text.strip(),
            "blocks": [],
            "width": img.width,
            "height": img.height,
        })

        if (i + 1) % 10 == 0 or i == total - 1:
            print(f"  OCR progress: {i+1}/{total} pages")

    return pages


def _has_meaningful_text(pages: list[dict], threshold: int = 50) -> bool:
    """检查提取结果是否包含有意义的文本（前几页平均字符数超过阈值）。"""
    if not pages:
        return False
    sample = pages[:min(5, len(pages))]
    avg_len = sum(len(p["text"]) for p in sample) / len(sample)
    return avg_len >= threshold


# --- 结构提取（基于 pdf-harvester 的 extract_with_structure 模式） ---

def extract_with_structure(pdf_path: str) -> dict:
    """
    提取 PDF 文本 + 自动检测标题结构。

    使用字体大小和粗体来识别标题层级，无需硬编码目录。
    适用于课件 PDF（Slide 标题通常字号更大/加粗）。

    对于扫描版/OCR PDF，回退到基于文本模式的标题检测。

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

    # 先检查是否有文本块可用（非扫描版）
    sample_text = ""
    for page in doc[:min(3, len(doc))]:
        sample_text += page.get_text("text")
    is_scanned = len(sample_text.strip()) < 100

    if is_scanned:
        # 扫描版 PDF：使用 OCR 提取文本后再做结构分析
        doc.close()
        print("[INFO] 扫描版 PDF 检测到，使用 OCR 文本进行结构分析...")
        ocr_pages = extract_text_from_pdf(pdf_path)
        if not ocr_pages or not _has_meaningful_text(ocr_pages):
            print("[WARN] OCR 文本不足，无法进行结构分析")
            return {
                "total": len(ocr_pages) if ocr_pages else 0,
                "pages": [{"page": p["page"], "text": p["text"], "headings": [], "paragraphs": []}
                          for p in (ocr_pages or [])],
                "outline": [],
            }
        outline = []
        pages_out = []
        for p in ocr_pages:
            headings, body_lines = _detect_headings_from_text(p["text"])
            pages_out.append({
                "page": p["page"],
                "text": p["text"],
                "headings": [{"text": h, "level": lv, "font_size": 0, "page": p["page"]}
                            for h, lv in headings],
                "paragraphs": [" ".join(body_lines)] if body_lines else [],
            })
            for h, lv in headings:
                if not any(o["title"] == h for o in outline):
                    outline.append({"title": h, "page": p["page"], "level": lv})
        print(f"[OK] 结构提取完成: {len(pages_out)} 页, {len(outline)} 个标题")
        print(f"  (使用 OCR 文本模式匹配，标题检测精度有限)")
        return {
            "total": len(pages_out),
            "pages": pages_out,
            "outline": outline,
        }

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
    if is_scanned:
        print(f"  (使用 OCR 文本模式匹配，标题检测精度有限)")
    return {
        "total": len(pages_out),
        "pages": pages_out,
        "outline": outline,
    }


def _detect_headings_from_text(text: str) -> tuple:
    """
    从纯文本中基于模式匹配检测标题（OCR 回退方案）。

    检测规则（保守策略，减少误匹配）：
      - "N. Chapter N: Title" → Level 1
      - "Chapter N: Title" 或 "Chapter N - Title" → Level 1
      - "N.N Title" (如 "1.1 What is a time series?") → Level 2
      - "Problem Sheet N" → Level 2
      - 排除：纯数字行、明显是公式/代码的行

    返回: ([(标题文本, level), ...], [正文行, ...])
    """
    headings = []
    body_lines = []
    lines = text.split('\n')

    # Level 1 patterns: chapter-level headings
    l1_patterns = [
        # "N. Chapter N: Title" e.g. "1. Chapter 1: Introduction"
        (r'^(\d{1,2})\.\s*Chapter\s+\1[\.:\)]\s*(.+)', 1),
        # "N. Chapter N - Title"
        (r'^(\d{1,2})\.\s*Chapter\s+\1\s*[-–—]\s*(.+)', 1),
        # "Chapter N: Title" or "Chapter N. Title"
        (r'^Chapter\s+(\d{1,2})[\.:\)\s-]+(.+)', 1),
    ]

    # Level 2 patterns: subsection-level
    l2_patterns = [
        # "N.M Title" e.g. "1.1 What is a time series?"
        (r'^(\d{1,2}\.\d+)\s+(.+)', 2),
        # "Problem Sheet N" or "Problem Sheet N: Title"
        (r'^Problem\s+Sheet\s+\d+.*', 2),
    ]

    for line in lines:
        line = line.strip()
        if not line or len(line) < 4:
            body_lines.append(line)
            continue

        # 跳过明显的非标题行
        if _is_likely_not_heading(line):
            body_lines.append(line)
            continue

        matched = False

        for pattern, level in l1_patterns:
            m = re.match(pattern, line, re.IGNORECASE)
            if m:
                # 保留完整行作为标题文本（generate_guide.py 需要解析编号）
                headings.append((line, level))
                matched = True
                break

        if not matched:
            for pattern, level in l2_patterns:
                m = re.match(pattern, line, re.IGNORECASE)
                if m:
                    headings.append((line, level))
                    matched = True
                    break

        if not matched:
            body_lines.append(line)

    return headings, body_lines


def _is_likely_not_heading(line: str) -> bool:
    """检测一行文本是否大概率不是标题（启发式规则）。"""
    # 纯数字或纯标点
    if re.match(r'^[\d\s\.\,\;\:\-\=\+\*\/\(\)\[\]\{\}\<\>\|\&\^\%\$\#\@\!\\\?\'\"\_\~\`]+$', line):
        return True
    # 太短
    if len(line) < 4:
        return True
    # 明显是公式/代码（包含过多数学符号且字母很少）
    alpha_chars = sum(1 for c in line if c.isalpha())
    if alpha_chars < len(line) * 0.3:
        return True
    # 以 "== " 或 "--" 开头（可能是分隔线或 OCR 噪音）
    if re.match(r'^[=\-]{2,}', line):
        return True
    # 看起来像方程式引用编号加噪音
    if re.match(r'^\d{1,3}[\.\)]\s*[=\-\(\)\[\]]', line):
        return True
    return False


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
