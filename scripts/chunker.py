"""
智能分块器 - 按页面范围切分 + 精确章节标注
"""
import re
from config import CHUNK_SIZE

# MATH2702 course section headers (from table of contents)
SECTION_HEADERS = {
    1: "Stochastic processes and the Markov property",
    2: "Random walk",
    3: "Discrete time Markov chains",
    4: "Martingales and Gambler",
    5: "Examples from actuarial",
    6: "Class Structure",
    7: "Hitting times",
    8: "Recurrence and transience",
    9: "Stationary distributions",
    10: "Reversibility",
    11: "Long-term behaviour",
    12: "End of Part I",
    13: "Poisson process with Poisson increments",
    14: "Poisson process with exponential holding times",
    15: "Poisson process in infinitesimal",
    16: "Counting processes",
    17: "Continuous time Markov jump processes",
    18: "Forward and backward equations",
    19: "Class structure and hitting times",
    20: "Long-term behaviour of Markov jump",
    21: "Queues",
    22: "End of Part II",
}


def chunk_pdf(pages: list[dict], prefer_sections: bool = True) -> list[dict]:
    """
    对PDF页面进行分块。按页分组（每1-3页一块）。
    """
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
            chunks.append({
                "content": current_text.strip(),
                "metadata": {
                    "chunk_index": chunk_idx,
                    "pages": f"{current_pages[0]}-{current_pages[-1]}",
                }
            })
            chunk_idx += 1
            current_text = ""
            current_pages = []

    if current_text.strip():
        chunks.append({
            "content": current_text.strip(),
            "metadata": {
                "chunk_index": chunk_idx,
                "pages": f"{current_pages[0]}-{current_pages[-1]}",
            }
        })

    print(f"分块完成: {len(chunks)} 个块 (来自 {len(pages)} 页)")

    # 精确标注章节
    _tag_sections_by_page(chunks, pages)

    return chunks


def _tag_sections_by_page(chunks: list[dict], pages: list[dict]):
    """
    通过扫描每页的章节标题来确定章节边界。

    方法：扫描每一页是否包含section header，建立 page→section 映射。
    然后根据chunk的页码范围分配section。
    """
    # Step 1: 扫描每一页，检测section header
    page_to_section = {}  # page_num → section_num
    section_info = {}     # section_num → title

    for page in pages:
        page_num = page["page"]
        text = page["text"]

        # 为每个section查找其标题是否出现在该页
        for sec_num, keyword in SECTION_HEADERS.items():
            # 用标题的前几个有意义单词作为搜索词
            search_words = " ".join(keyword.split()[:3])
            if len(search_words) < 10:
                search_words = keyword.split()[0] if keyword.split() else keyword

            if search_words.lower() in text.lower():
                # 进一步验证：检查是否是真正的section标题（行首出现，数字+标题）
                pattern = re.compile(
                    rf'(?:^|\n)\s*{sec_num}\s+{re.escape(search_words[:30])}',
                    re.IGNORECASE
                )
                if pattern.search(text):
                    if sec_num not in page_to_section:
                        page_to_section[page_num] = sec_num
                        section_info[sec_num] = keyword
                        break  # 一页只标记一个section

    # Step 2: 填充中间页面
    # 如果page 5是section 1, page 10是section 2，则pages 5-9都是section 1
    section_starts = sorted(page_to_section.items())  # [(page, sec), ...]

    for i, (page_num, sec_num) in enumerate(section_starts):
        next_page = section_starts[i + 1][0] if i + 1 < len(section_starts) else len(pages) + 1
        for p in range(page_num, next_page):
            if p not in page_to_section:
                page_to_section[p] = sec_num

    # Step 3: 为每个chunk分配section
    for chunk in chunks:
        pages_str = chunk["metadata"]["pages"]
        start_page = int(pages_str.split("-")[0])
        end_page = int(pages_str.split("-")[-1])

        # 查找chunk覆盖页面中的section
        found_sections = set()
        for p in range(start_page, end_page + 1):
            if p in page_to_section:
                found_sections.add(page_to_section[p])

        if found_sections:
            # 使用出现频率最高的section
            from collections import Counter
            section_counts = Counter()
            for p in range(start_page, end_page + 1):
                if p in page_to_section:
                    section_counts[page_to_section[p]] += 1
            best_sec = section_counts.most_common(1)[0][0]
            chunk["metadata"]["section"] = best_sec
            chunk["metadata"]["section_title"] = section_info.get(best_sec, SECTION_HEADERS.get(best_sec, ""))
        else:
            chunk["metadata"]["section"] = ""
            chunk["metadata"]["section_title"] = ""

    detected = len(section_info)
    tagged = sum(1 for c in chunks if c["metadata"].get("section"))
    print(f"章节检测: 发现 {detected} 个section标题, 标注了 {tagged}/{len(chunks)} 个块")

    if detected < 10:
        print("  WARNING: 章节检测较少，可能是PDF格式特殊")
        _print_detected_sections(section_starts, section_info)


def _print_detected_sections(section_starts, section_info):
    """调试：打印检测到的章节信息"""
    for page_num, sec_num in section_starts:
        print(f"    Page {page_num} → Section {sec_num}: {section_info.get(sec_num, '?')}")


if __name__ == "__main__":
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    from pdf_loader import extract_text_from_pdf

    pdf_path = "../课程/MATH2702/课件.pdf"
    pages = extract_text_from_pdf(pdf_path)
    chunks = chunk_pdf(pages)

    # 统计各章节
    from collections import Counter
    section_dist = Counter(
        c["metadata"].get("section") or "untagged"
        for c in chunks
    )
    print(f"\n章节分布:")
    for sec, count in sorted(section_dist.items(),
                             key=lambda x: (0 if str(x[0]).isdigit() else 999, int(x[0]) if str(x[0]).isdigit() else 0)):
        print(f"  Section {sec}: {count} chunks")
