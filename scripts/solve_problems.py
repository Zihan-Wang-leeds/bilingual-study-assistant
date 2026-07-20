"""
习题解答生成器 - 提取课件中的Problem Sheet并生成详细解题过程
"""
import os
import sys
import re
import time
import json
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import (
    API_KEY, BASE_URL, MODEL_NAME, COURSES_DIR,
    GENERATION_TEMPERATURE, GENERATION_MAX_TOKENS, GENERATION_SLEEP,
)
from pdf_loader import extract_text_from_pdf, extract_course_info

load_dotenv()

OUTPUT_DIR = "guides"


class ProblemSolver:
    """提取并解答课件中的Problem Sheet"""

    def __init__(self, course_code: str, pdf_path: str):
        self.course_code = course_code
        self.pdf_path = pdf_path
        self.output_dir = os.path.join(os.path.dirname(pdf_path), OUTPUT_DIR)

        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY", API_KEY),
            base_url=BASE_URL
        )

        print(f"Loading PDF: {pdf_path}")
        self.pages = extract_text_from_pdf(pdf_path)
        print(f"  {len(self.pages)} pages loaded")

    # ================================================================
    # Problem sheet detection
    # ================================================================

    def find_all_problem_sheets(self) -> list[dict]:
        """
        检测所有Problem Sheet的位置。

        返回: [{number, title, start_page, end_page}, ...]
        """
        ps_pattern = re.compile(r'^Problem\s*[Ss]heet\s*(\d+)', re.MULTILINE)
        problems = []

        for page in self.pages:
            text = page["text"]
            m = ps_pattern.search(text)
            if m:
                num = int(m.group(1))
                if page["page"] > 6:  # Skip TOC pages (first 6)
                    problems.append({
                        "number": num,
                        "start_page": page["page"],
                        "end_page": None,
                    })

        # Remove duplicates (same problem sheet on multiple pages)
        seen = set()
        unique = []
        for ps in problems:
            if ps["number"] not in seen:
                seen.add(ps["number"])
                unique.append(ps)
        unique.sort(key=lambda x: x["number"])

        # Also find section headers for end-page detection
        section_starts = self._find_section_pages()

        # Determine end page for each problem sheet
        for i, ps in enumerate(unique):
            candidates = []

            # Next problem sheet start
            if i + 1 < len(unique):
                candidates.append(unique[i + 1]["start_page"] - 1)

            # Next section start
            for sec_page in sorted(section_starts):
                if sec_page > ps["start_page"]:
                    candidates.append(sec_page - 1)
                    break

            # End of document
            candidates.append(len(self.pages))

            ps["end_page"] = min(candidates)

            # Problem sheets usually span 1-2 pages
            if ps["end_page"] - ps["start_page"] > 4:
                ps["end_page"] = ps["start_page"] + 2

        return unique

    def _find_section_pages(self) -> set:
        """找到所有section起始页。"""
        section_starts = set()
        for page in self.pages:
            text = page["text"]
            if page["page"] <= 6:
                continue
            # Look for patterns like "1 Title...", "12 Title..."
            m = re.search(r'(?:^|\n)\s*(\d{1,2})\s+([A-Z][^\n]{10,100})$', text, re.MULTILINE)
            if m:
                num = int(m.group(1))
                line = m.group(0)
                if 1 <= num <= 25 and '.....' not in line:
                    section_starts.add(page["page"])
        return section_starts

    # ================================================================
    # Solution generation
    # ================================================================

    def generate_all(self):
        """生成所有Problem Sheet的解答。"""
        problems = self.find_all_problem_sheets()
        print(f"\nFound {len(problems)} Problem Sheets")

        os.makedirs(self.output_dir, exist_ok=True)

        generated = []
        for ps in problems:
            print(f"\n{'='*60}")
            print(f"Solving Problem Sheet {ps['number']}")
            print(f"  Pages {ps['start_page']}-{ps['end_page']}")
            print(f"{'='*60}")

            try:
                # 提取题目文本
                problem_text = self._extract_problem_text(ps)
                print(f"  Text length: {len(problem_text)} chars")

                # 生成解答
                solution = self._generate_solution(ps, problem_text)

                # 保存
                filename = f"Problem_Sheet_{ps['number']:02d}.md"
                filepath = os.path.join(self.output_dir, filename)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(solution)

                print(f"  Saved: {filepath}")
                generated.append(ps)
                time.sleep(GENERATION_SLEEP)

            except Exception as e:
                print(f"  ERROR: {e}")

        print(f"\n{'='*60}")
        print(f"DONE! Generated {len(generated)}/{len(problems)} Problem Sheets")
        print(f"Output: {self.output_dir}")
        print(f"{'='*60}")

    def _extract_problem_text(self, ps: dict) -> str:
        """提取Problem Sheet的完整文本。"""
        texts = []
        for page in self.pages:
            if ps["start_page"] <= page["page"] <= ps["end_page"]:
                texts.append(page["text"])

        full = "\n\n".join(texts)

        # 尝试截取"Problem Sheet X"之后的内容
        pattern = re.compile(rf'Problem\s*[Ss]heet\s*{ps["number"]}', re.IGNORECASE)
        m = pattern.search(full)
        if m:
            full = full[m.start():]

        return full.strip()

    def _generate_solution(self, ps: dict, problem_text: str) -> str:
        """为单个Problem Sheet生成详细解答。"""
        # 截断过长的文本
        max_chars = 15000
        if len(problem_text) > max_chars:
            problem_text = problem_text[:max_chars] + "\n\n[Content truncated]"

        prompt = f"""You are a university tutor creating detailed solutions for a Problem Sheet from the course {self.course_code}: Stochastic Processes.

Below is the problem sheet content. Your task: generate COMPLETE, STEP-BY-STEP solutions for EVERY question.

---
PROBLEM SHEET:
{problem_text}
---

For EACH question, provide:

### Question X / 第X题

**Problem / 题目原文:**
(Copy the original English problem statement)

**中文翻译:**
(Chinese translation of the problem)

**Knowledge Points / 考查知识点:**
- Which sections/concepts from the course this tests

**Step-by-Step Solution / 逐步解答:**

For EACH step:
1. State what we're doing in this step
2. Show the mathematical working
3. Explain WHY we do this
4. Intermediate result

Use proper mathematical notation.
Explain every formula and every symbol.
For derivations, show ALL algebraic steps.
For probability questions, explicitly state which probability rules are used.

**Final Answer / 最终答案:**
Box the final answer clearly.

**Key Insight / 解题要点:**
One sentence summary of the most important idea.

---

RULES:
1. Solve EVERY question completely - no skipping
2. Show ALL working - partial credit matters in exams
3. Use bilingual format: English math + Chinese explanations
4. Reference course sections when using theorems
5. For proof questions, explain the logical structure
6. Double-check all calculations"""

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a university mathematics tutor specializing in stochastic processes. You create detailed, step-by-step solutions with bilingual (Chinese/English) explanations. You never skip steps and always explain the reasoning."},
                {"role": "user", "content": prompt}
            ],
            temperature=GENERATION_TEMPERATURE,
            max_tokens=GENERATION_MAX_TOKENS
        )

        content = response.choices[0].message.content

        header = f"""# Problem Sheet {ps['number']} - 详细解答 / Detailed Solutions

> {self.course_code} Stochastic Processes
> 生成时间 / Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
> 来源页 / Source Pages: {ps['start_page']}-{ps['end_page']}

---

"""
        return header + content


# ================================================================
# Main
# ================================================================

def main():
    import argparse

    ap = argparse.ArgumentParser(description="Generate solutions for Problem Sheets")
    ap.add_argument("--course", type=str, default=None,
                    help="Course code (e.g. MATH2702). Auto-detects if not specified.")
    ap.add_argument("--all", action="store_true", help="Solve ALL Problem Sheets")
    ap.add_argument("--sheet", type=int, default=1, help="Solve single Problem Sheet (default: 1)")
    args = ap.parse_args()

    # Auto-detect course if not specified
    if args.course:
        course_code = args.course
    else:
        courses = [
            d for d in os.listdir(COURSES_DIR)
            if os.path.isdir(os.path.join(COURSES_DIR, d))
        ]
        if not courses:
            print(f"ERROR: No course directories found in {COURSES_DIR}")
            return
        course_code = courses[0]
        if len(courses) > 1:
            print(f"Multiple courses found: {courses}")
            print(f"Using first: {course_code}. Use --course to specify.")

    pdf_path = os.path.join(COURSES_DIR, course_code, "课件.pdf")

    if not os.path.exists(pdf_path):
        print(f"ERROR: PDF not found: {pdf_path}")
        return

    solver = ProblemSolver(course_code, pdf_path)

    if args.all:
        solver.generate_all()
    else:
        # 单个Problem Sheet测试
        problems = solver.find_all_problem_sheets()
        target = None
        for ps in problems:
            if ps["number"] == args.sheet:
                target = ps
                break

        if not target:
            print(f"Problem Sheet {args.sheet} not found")
            print(f"Available: {[p['number'] for p in problems]}")
            return

        os.makedirs(solver.output_dir, exist_ok=True)

        problem_text = solver._extract_problem_text(target)
        print(f"Problem Sheet {target['number']}: pages {target['start_page']}-{target['end_page']}")
        print(f"Text length: {len(problem_text)} chars")

        solution = solver._generate_solution(target, problem_text)

        filename = f"Problem_Sheet_{target['number']:02d}.md"
        filepath = os.path.join(solver.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(solution)

        print(f"\nSaved: {filepath}")
        print(f"Length: {len(solution)} chars")


if __name__ == "__main__":
    main()
