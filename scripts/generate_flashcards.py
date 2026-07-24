"""
闪卡生成器 — 从课件自动提取关键定义/定理/公式，生成 Anki 可导入的 CSV + Markdown

用法:
    python scripts/generate_flashcards.py --course MATH2702
    python scripts/generate_flashcards.py --course MATH2702 --sections 1-5
"""
import os
import sys
import csv
import re
import io
from datetime import datetime

import paths; paths.setup()

from config import (
    COURSES_DIR, GENERATION_TEMPERATURE, GENERATION_MAX_TOKENS,
)
from pdf_loader import extract_text_from_pdf
from llm_client import call_llm_with_prompts

OUTPUT_DIR = "guides"
FLASHCARD_SYSTEM_PROMPT = """You are a university professor extracting key concepts from course materials for flashcard creation.

Your task: Read the course content and extract the most important DEFINITIONS, THEOREMS, FORMULAS, and KEY CONCEPTS.

For each item, create a flashcard with:
- FRONT: The term, concept name, or a targeted question (in English)
- BACK: The definition, explanation, formula, or answer (BILINGUAL: English + Chinese)

FORMAT YOUR RESPONSE as a structured list. Each flashcard MUST follow this exact format:

---FLASHCARD---
FRONT: <term or question in English>
BACK: <detailed answer in English>
BACK_CN: <Chinese translation/summary>
SOURCE: <section number or page reference>
TYPE: <definition|theorem|formula|concept>
---END---

Generate 10-20 flashcards covering ALL important points in the material.
Focus on concepts that students MUST memorize for exams.
Every formula must use LaTeX notation ($...$ for inline, $$...$$ for display)."""


def generate_flashcards(course_code: str, pdf_path: str,
                        sections: tuple = None, pre_text: str = None) -> list[dict]:
    """从 PDF 课件生成闪卡列表。

    Args:
        course_code: 课程代码
        pdf_path: PDF 文件路径
        sections: 可选的页面范围 (start, end)
        pre_text: 可选的预提取文本（传入后跳过 PDF 提取，用于 Web 端避免重复 OCR）
    """
    print(f"\n[Flashcards] Generating flashcards for {course_code}...")
    print(f"   Source: {pdf_path}")

    if pre_text:
        print(f"   Using pre-extracted text ({len(pre_text)} chars)")
        full_text = pre_text
    else:
        pages = extract_text_from_pdf(pdf_path)
        if not pages:
            print("ERROR: No pages extracted from PDF")
            return []

        # 筛选页面范围
        if sections:
            start, end = sections
            pages = [p for p in pages if start <= p["page"] <= end]
            print(f"   Pages {start}-{end} ({len(pages)} pages)")

        # 合并文本
        full_text = "\n\n".join(f"[Page {p['page']}]\n{p['text']}" for p in pages)

    # 过长则截断（保留开头和结尾）
    max_chars = 15000
    if len(full_text) > max_chars:
        half = max_chars // 2
        full_text = full_text[:half] + "\n\n[... content truncated ...]\n\n" + full_text[-half:]

    print(f"   Processing {len(full_text)} chars...")

    user_prompt = f"""Extract flashcards from the following course material for {course_code}.

Course material:
{full_text}

Extract 15-20 key concepts as flashcards using the required format.
Include definitions, theorems, formulas, and important concepts.
Each formula MUST use LaTeX (e.g., $X_n$ for inline, $$P(X=x)$$ for display)."""

    response = call_llm_with_prompts(
        system_prompt=FLASHCARD_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        temperature=GENERATION_TEMPERATURE,
        max_tokens=GENERATION_MAX_TOKENS,
    )

    # 解析响应
    flashcards = _parse_flashcards(response)
    print(f"   Extracted {len(flashcards)} flashcards")
    return flashcards


def _parse_flashcards(text: str) -> list[dict]:
    """解析 LLM 返回的闪卡文本。"""
    cards = []
    pattern = re.compile(
        r'---FLASHCARD---\s*(.*?)\s*---END---',
        re.DOTALL
    )
    for match in pattern.finditer(text):
        block = match.group(1)
        card = {}
        for field in ('FRONT', 'BACK', 'BACK_CN', 'SOURCE', 'TYPE'):
            m = re.search(rf'^{field}:\s*(.+?)$', block, re.MULTILINE)
            if m:
                card[field.lower()] = m.group(1).strip()
        if card.get('front') and card.get('back'):
            cards.append(card)

    return cards


def save_flashcards(course_code: str, output_dir: str,
                    flashcards: list[dict]):
    """保存闪卡为 Markdown 和 Anki CSV。"""
    os.makedirs(output_dir, exist_ok=True)

    # Markdown
    md_path = os.path.join(output_dir, "Flashcards.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f"# {course_code} - Flashcards / 闪卡\n\n")
        f.write(f"> 生成时间 / Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"> 共 {len(flashcards)} 张卡片 / Total cards\n\n")
        f.write("---\n\n")

        for i, card in enumerate(flashcards, 1):
            f.write(f"## Card {i}: {card.get('front', '')}\n\n")
            f.write(f"**Front / 正面**: {card.get('front', '')}\n\n")
            f.write(f"**Back / 反面**: {card.get('back', '')}\n\n")
            f.write(f"**中文**: {card.get('back_cn', '')}\n\n")
            f.write(f"*Type: {card.get('type', '')} | Source: {card.get('source', '')}*\n\n")
            f.write("---\n\n")

    print(f"   [Markdown] {md_path}")

    # Anki CSV
    csv_path = os.path.join(output_dir, "Flashcards.csv")
    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Front', 'Back', 'Chinese', 'Type', 'Source', 'Tags'])
        for card in flashcards:
            writer.writerow([
                card.get('front', ''),
                card.get('back', ''),
                card.get('back_cn', ''),
                card.get('type', ''),
                card.get('source', ''),
                f"{course_code}",
            ])

    print(f"   [CSV] {csv_path}")
    print(f"\n[Tip] Import into Anki: File -> Import -> Select {csv_path}")
    print(f"   Import Anki: File -> Import -> Select {csv_path}")


def main():
    import argparse

    ap = argparse.ArgumentParser(
        description="Generate bilingual flashcards from course PDFs"
    )
    ap.add_argument("--course", type=str, required=True,
                    help="Course code (e.g. MATH2702)")
    ap.add_argument("--sections", type=str, default=None,
                    help="Page range (e.g. '1-20')")
    args = ap.parse_args()

    course_code = args.course.upper()
    pdf_path = os.path.join(COURSES_DIR, course_code, "课件.pdf")

    if not os.path.exists(pdf_path):
        print(f"ERROR: PDF not found: {pdf_path}")
        return

    # 解析章节范围
    sections = None
    if args.sections:
        parts = args.sections.split('-')
        if len(parts) == 2:
            sections = (int(parts[0]), int(parts[1]))

    output_dir = os.path.join(COURSES_DIR, course_code, OUTPUT_DIR)

    flashcards = generate_flashcards(course_code, pdf_path, sections)
    if flashcards:
        save_flashcards(course_code, output_dir, flashcards)
    else:
        print("No flashcards extracted. Try a different section range.")


if __name__ == "__main__":
    main()
