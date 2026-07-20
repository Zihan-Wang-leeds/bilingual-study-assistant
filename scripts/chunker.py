"""
智能分块器 - 自动章节检测 + 多种分块策略

改进项（基于 pdf-harvester 模式）：
  1. 移除硬编码 SECTION_HEADERS → 自动从文本检测章节边界
  2. 新增 chunk_by_sections() — 按章节标题边界分块
  3. 新增 chunk_by_paragraphs() — 按段落语义分块，支持重叠
  4. metadata 一致性改进 (page_start/page_end 整数替代 "pages" 字符串)
  5. 完全向后兼容 chunk_pdf() API
"""
import re
from collections import Counter
from config import CHUNK_SIZE


# ============================================================
# 自动章节检测（替代硬编码 SECTION_HEADERS）
# ============================================================

def detect_sections_from_text(pages: list[dict]) -> dict:
    """
    从页面文本自动检测章节边界，无需硬编码目录。

    检测策略（多模式）：
      1. 编号标题:  "1. Markov Chains", "3.1 Definition"
      2. 单词标题:  行首独立出现的大写/关键词标题
      3. Slide标题: 课件中常见的 "Section X" / "Chapter X" / "Part X"
      4. 利用 pdf_loader 提取的 blocks 中的粗体/大字号行

    Args:
        pages: extract_text_from_pdf() 返回的页面列表

    Returns:
        {
            "sections": [(page_num, section_title), ...],  # 章节起始页
            "page_to_section": {page_num: section_title},   # 每页所属章节
        }
    """
    section_starts = []  # [(page_num, title), ...]

    # 编译检测模式
    numbered_pattern = re.compile(
        r'^\s*(\d{1,2}(?:\.\d{1,2})?)\s+([A-Z][A-Za-z\s\-]{3,60})$',
        re.MULTILINE,
    )
    section_keyword_pattern = re.compile(
        r'^\s*(Section|Chapter|Part|Unit|Lecture)\s+(\d+|[IVX]+)[\s:：\-]*(.*?)$',
        re.MULTILINE | re.IGNORECASE,
    )

    for page in pages:
        page_num = page["page"]
        text = page["text"]

        # 策略 1: 利用 blocks 中的大字号/粗体行（如果存在）
        blocks = page.get("blocks", [])
        for block in blocks:
            if block.get("type") != 0:
                continue
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    font_size = span.get("size", 12)
                    is_bold = "bold" in span.get("font", "").lower()
                    span_text = span["text"].strip()
                    # 大字号+粗体且长度合适 → 很可能是标题
                    if (font_size > 16 or (font_size > 13 and is_bold)) and 5 < len(span_text) < 100:
                        if not any(s[1] == span_text for s in section_starts):
                            section_starts.append((page_num, span_text))
                            break

        # 策略 2: 编号标题匹配
        for match in numbered_pattern.finditer(text):
            title = match.group(2).strip()
            if len(title) > 3:
                if not any(s[1] == title for s in section_starts):
                    section_starts.append((page_num, title))

        # 策略 3: Section/Chapter/Part 关键词
        for match in section_keyword_pattern.finditer(text):
            title = match.group(0).strip()
            if not any(s[1] == title for s in section_starts):
                section_starts.append((page_num, title))

    # 按页码排序
    section_starts.sort(key=lambda x: x[0])

    # 去重：相邻且相同标题只保留第一个
    deduped = []
    for i, (pn, title) in enumerate(section_starts):
        if i > 0 and title == section_starts[i - 1][1] and pn - section_starts[i - 1][0] <= 2:
            continue
        deduped.append((pn, title))
    section_starts = deduped

    # 构建 page→section 映射
    page_to_section = {}
    for i, (start_page, title) in enumerate(section_starts):
        next_page = section_starts[i + 1][0] if i + 1 < len(section_starts) else len(pages) + 1
        for p in range(start_page, next_page):
            page_to_section[p] = title

    print(f"章节检测: 发现 {len(section_starts)} 个候选标题")
    if len(section_starts) < 3:
        print("  WARNING: 检测到的章节较少，PDF 可能为纯图片或无明确标题结构")
        _print_section_starts(section_starts)

    return {
        "section_starts": section_starts,
        "page_to_section": page_to_section,
    }


def detect_sections_from_structure(structure: dict) -> dict:
    """
    从 extract_with_structure() 的输出中提取章节信息。
    更精确，因为使用了字体检测的 outline。

    Args:
        structure: pdf_loader.extract_with_structure() 返回的结构

    Returns:
        同 detect_sections_from_text() 格式
    """
    outline = structure.get("outline", [])
    section_starts = [(o["page"], o["title"]) for o in outline]

    page_to_section = {}
    total_pages = structure.get("total", 0)
    for i, (start_page, title) in enumerate(section_starts):
        next_page = section_starts[i + 1][0] if i + 1 < len(section_starts) else total_pages + 1
        for p in range(start_page, next_page):
            page_to_section[p] = title

    print(f"章节检测 (from structure): 发现 {len(section_starts)} 个标题")

    return {
        "section_starts": section_starts,
        "page_to_section": page_to_section,
    }


def _print_section_starts(section_starts):
    """调试：打印检测到的章节信息。"""
    for page_num, title in section_starts[:20]:
        print(f"    Page {page_num} → {title[:80]}")


# ============================================================
# 分块策略
# ============================================================

def chunk_pdf(pages: list[dict], prefer_sections: bool = True) -> list[dict]:
    """
    对 PDF 页面进行分块（主入口，保持向后兼容）。

    内部自动检测章节结构，优先在章节边界处分块。
    如果检测到的章节较少，退回到按页+字符数分块。

    Args:
        pages: extract_text_from_pdf() 返回的页面列表
        prefer_sections: 是否优先使用章节边界分块

    Returns:
        [{"content": str, "metadata": {...}}, ...]
    """
    # 自动检测章节
    section_info = detect_sections_from_text(pages)

    if prefer_sections and len(section_info["section_starts"]) >= 3:
        return _chunk_by_section_boundaries(pages, section_info)
    else:
        return _chunk_by_page_groups(pages, section_info)


def chunk_by_sections(pages: list[dict], structure: dict = None) -> list[dict]:
    """
    按章节边界分块 — 每个章节一个或多个块。

    如果提供了 structure（来自 extract_with_structure()），
    使用精确的字体检测章节；否则自动从文本检测。

    Args:
        pages: 页面列表
        structure: 可选，extract_with_structure() 的输出

    Returns:
        分块列表
    """
    if structure:
        section_info = detect_sections_from_structure(structure)
    else:
        section_info = detect_sections_from_text(pages)

    return _chunk_by_section_boundaries(pages, section_info)


def chunk_by_paragraphs(
    pages: list[dict],
    max_chunk_size: int = None,
    overlap_chars: int = 100,
) -> list[dict]:
    """
    按段落语义分块（来自 pdf-harvester 的 chunk_by_paragraphs 模式）。

    每个块尽量在段落边界结束，不超过 max_chunk_size 字符。
    相邻块之间有 overlap_chars 字符的重叠，避免检索时截断上下文。

    Args:
        pages: 页面列表
        max_chunk_size: 每块最大字符数（默认用 config 的 CHUNK_SIZE）
        overlap_chars: 相邻块重叠字符数

    Returns:
        分块列表
    """
    if max_chunk_size is None:
        max_chunk_size = CHUNK_SIZE

    # 合并所有页面文本，保留页面边界信息
    full_text_parts = []
    page_boundaries = []  # [(char_pos, page_num), ...]
    pos = 0
    for page in pages:
        text = page["text"].strip()
        if not text:
            continue
        page_boundaries.append((pos, page["page"]))
        full_text_parts.append(text)
        pos += len(text) + 2  # +2 for \n\n separator

    full_text = "\n\n".join(full_text_parts)

    # 按段落分割
    paragraphs = [p.strip() for p in full_text.split("\n\n") if p.strip()]

    chunks = []
    current_chunk_paras = []
    current_size = 0

    for para in paragraphs:
        para_size = len(para)

        if current_size + para_size > max_chunk_size and current_chunk_paras:
            # 保存当前块
            chunk_text = "\n\n".join(current_chunk_paras)
            start_page = _find_page_for_pos(
                full_text.find(current_chunk_paras[0]), page_boundaries
            )
            end_page = _find_page_for_pos(
                full_text.find(current_chunk_paras[-1]) + len(current_chunk_paras[-1]),
                page_boundaries,
            )
            chunks.append({
                "content": chunk_text,
                "metadata": {
                    "chunk_index": len(chunks),
                    "page_start": start_page,
                    "page_end": end_page,
                    "word_count": len(chunk_text),
                }
            })

            # 新块：带重叠（从上一块末尾截取 overlap_chars 字符作为上下文桥接）
            prev_text = "\n\n".join(current_chunk_paras)
            overlap_text = prev_text[-overlap_chars:] if len(prev_text) > overlap_chars else prev_text
            # 从重叠文本的最后一个段落开始新块
            overlap_paras = [p.strip() for p in overlap_text.split("\n\n") if p.strip()]
            current_chunk_paras = overlap_paras if overlap_paras else []
            current_size = sum(len(p) for p in current_chunk_paras)

        current_chunk_paras.append(para)
        current_size += para_size

    # 最后一块
    if current_chunk_paras:
        chunk_text = "\n\n".join(current_chunk_paras)
        start_page = _find_page_for_pos(
            full_text.find(current_chunk_paras[0]), page_boundaries
        )
        end_page = _find_page_for_pos(
            full_text.find(current_chunk_paras[-1]) + len(current_chunk_paras[-1]),
            page_boundaries,
        )
        chunks.append({
            "content": chunk_text,
            "metadata": {
                "chunk_index": len(chunks),
                "page_start": start_page,
                "page_end": end_page,
                "word_count": len(chunk_text),
            }
        })

    print(f"段落分块完成: {len(chunks)} 个块 (来自 {len(pages)} 页)")
    return chunks


# ============================================================
# 内部分块实现
# ============================================================

def _chunk_by_section_boundaries(pages: list[dict], section_info: dict) -> list[dict]:
    """
    在章节边界处分块。同一章节内的页面组合在一起，
    如果章节内容很长则进一步按 CHUNK_SIZE 分割。
    """
    page_to_section = section_info["page_to_section"]
    section_starts = section_info["section_starts"]

    chunks = []
    chunk_idx = 0

    for i, (start_page, title) in enumerate(section_starts):
        next_start = section_starts[i + 1][0] if i + 1 < len(section_starts) else len(pages) + 1

        section_pages = [p for p in pages if start_page <= p["page"] < next_start]
        if not section_pages:
            continue

        section_text = "\n".join(p["text"] for p in section_pages)

        # 如果章节内容较短，作为一块；否则按 CHUNK_SIZE 进一步分割
        if len(section_text) <= CHUNK_SIZE * 1.5:
            chunks.append({
                "content": section_text.strip(),
                "metadata": {
                    "chunk_index": chunk_idx,
                    "page_start": start_page,
                    "page_end": next_start - 1,
                    "section_title": title,
                }
            })
            chunk_idx += 1
        else:
            # 长章节：在段落边界再分块
            sub_chunks = _split_long_section(section_pages, title)
            for sc in sub_chunks:
                sc["metadata"]["chunk_index"] = chunk_idx
                chunks.append(sc)
                chunk_idx += 1

    # 处理未被章节覆盖的页面（如果存在）
    covered_pages = set()
    for c in chunks:
        for p in range(c["metadata"]["page_start"], c["metadata"]["page_end"] + 1):
            covered_pages.add(p)

    orphan_pages = [p for p in pages if p["page"] not in covered_pages and p["text"].strip()]
    if orphan_pages:
        for sub in _chunk_by_page_groups(orphan_pages, section_info):
            sub["metadata"]["chunk_index"] = chunk_idx
            chunks.append(sub)
            chunk_idx += 1

    # 补齐 section_title
    for chunk in chunks:
        if "section_title" not in chunk["metadata"]:
            mid_page = (chunk["metadata"]["page_start"] + chunk["metadata"]["page_end"]) // 2
            chunk["metadata"]["section_title"] = page_to_section.get(mid_page, "")

    tagged = sum(1 for c in chunks if c["metadata"].get("section_title"))
    print(f"章节分块完成: {len(chunks)} 个块, {tagged} 个已标注章节")
    return chunks


def _chunk_by_page_groups(pages: list[dict], section_info: dict = None) -> list[dict]:
    """
    按页面分组分块（原有逻辑的升级版）。

    每 1-3 页一组，在 CHUNK_SIZE 附近切割。
    metadata 使用 page_start/page_end 整数替代 "pages" 字符串。
    """
    page_to_section = section_info.get("page_to_section", {}) if section_info else {}

    chunks = []
    current_text = ""
    current_pages = []
    chunk_idx = 0

    for page in pages:
        page_text = page["text"].strip()
        if not page_text:
            continue

        current_text += "\n" + page_text
        current_pages.append(page["page"])

        if len(current_text) >= CHUNK_SIZE or len(current_pages) >= 3:
            # 确定章节归属
            mid_page = current_pages[len(current_pages) // 2]
            section_title = page_to_section.get(mid_page, "")

            chunks.append({
                "content": current_text.strip(),
                "metadata": {
                    "chunk_index": chunk_idx,
                    "page_start": current_pages[0],
                    "page_end": current_pages[-1],
                    "section_title": section_title,
                }
            })
            chunk_idx += 1
            current_text = ""
            current_pages = []

    # 剩余页面
    if current_text.strip():
        mid_page = current_pages[len(current_pages) // 2]
        section_title = page_to_section.get(mid_page, "")

        chunks.append({
            "content": current_text.strip(),
            "metadata": {
                "chunk_index": chunk_idx,
                "page_start": current_pages[0],
                "page_end": current_pages[-1],
                "section_title": section_title,
            }
        })

    tagged = sum(1 for c in chunks if c["metadata"].get("section_title"))
    print(f"页组分块完成: {len(chunks)} 个块 (来自 {len(pages)} 页), {tagged} 个已标注章节")
    return chunks


def _split_long_section(pages: list[dict], section_title: str) -> list[dict]:
    """将长章节在段落边界处进一步分割。"""
    full_text = "\n".join(p["text"] for p in pages)
    paragraphs = full_text.split("\n\n")

    chunks = []
    current_text = ""
    current_start_page = pages[0]["page"] if pages else 1
    current_page = current_start_page

    for para in paragraphs:
        if len(current_text) + len(para) > CHUNK_SIZE and current_text:
            chunks.append({
                "content": current_text.strip(),
                "metadata": {
                    "page_start": current_start_page,
                    "page_end": current_page,
                    "section_title": section_title,
                }
            })
            current_text = para
            current_start_page = current_page
        else:
            current_text += "\n\n" + para if current_text else para

        # 粗略估计当前段落在哪一页
        for p in pages:
            if para[:30] in p["text"]:
                current_page = p["page"]
                break

    if current_text.strip():
        chunks.append({
            "content": current_text.strip(),
            "metadata": {
                "page_start": current_start_page,
                "page_end": pages[-1]["page"] if pages else current_page,
                "section_title": section_title,
            }
        })

    return chunks


def _find_page_for_pos(char_pos: int, page_boundaries: list) -> int:
    """根据字符位置查找所在页码。"""
    page_num = 1
    for pos, pg in page_boundaries:
        if char_pos >= pos:
            page_num = pg
        else:
            break
    return page_num


# ============================================================
# 测试入口
# ============================================================

if __name__ == "__main__":
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    from pdf_loader import extract_text_from_pdf

    pdf_path = "../课程/MATH2702/课件.pdf"
    pages = extract_text_from_pdf(pdf_path)

    print("\n" + "=" * 60)
    print("策略 A: 自动检测章节分块 (chunk_pdf)")
    print("=" * 60)
    chunks = chunk_pdf(pages)
    section_dist = Counter(
        c["metadata"].get("section_title") or "untagged"
        for c in chunks
    )
    print(f"章节分布 (top 10):")
    for sec, count in sorted(
        section_dist.items(),
        key=lambda x: -x[1],
    )[:10]:
        print(f"  [{count} chunks] {sec[:80]}")

    print("\n" + "=" * 60)
    print("策略 B: 段落分块 (chunk_by_paragraphs)")
    print("=" * 60)
    para_chunks = chunk_by_paragraphs(pages)
    print(f"前3个块的元数据:")
    for c in para_chunks[:3]:
        print(f"  Chunk {c['metadata']['chunk_index']}: "
              f"Pages {c['metadata']['page_start']}-{c['metadata']['page_end']}, "
              f"{c['metadata']['word_count']}字符")
