"""
Coursework 辅助工具 — 解析课程作业要求，生成分步工作计划
"""
import os
import sys
import re
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import API_KEY, BASE_URL, MODEL_NAME, COURSES_DIR
from pdf_loader import extract_text_from_pdf

load_dotenv()

OUTPUT_DIR = "guides"


class CourseworkHelper:
    """解析coursework PDF，生成结构化工作计划"""

    def __init__(self, course_code: str, pdf_path: str):
        self.course_code = course_code
        self.pdf_path = pdf_path
        self.pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        self.output_dir = os.path.join(os.path.dirname(pdf_path), OUTPUT_DIR)

        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY", API_KEY),
            base_url=BASE_URL
        )

        print(f"Loading coursework: {pdf_path}")
        self.pages = extract_text_from_pdf(pdf_path)
        self.full_text = "\n\n".join(
            f"[Page {p['page']}]\n{p['text']}" for p in self.pages
        )
        print(f"  {len(self.pages)} pages, {len(self.full_text)} chars")

    # ================================================================
    # Step 1: Analyze coursework requirements
    # ================================================================

    def analyze(self) -> dict:
        """分析coursework的核心信息。"""
        print("\n--- Step 1: Analyzing coursework requirements ---")

        prompt = f"""Analyze this university coursework assignment. Extract structured information.

Coursework text:
{self.full_text[:8000]}

Return a JSON-like analysis with these fields:

1. COURSEWORK_TYPE: e.g., "Data Analysis + Report", "Mathematical Proof", "Programming", "Literature Review", "Presentation", "Mixed"
2. WEIGHT: What percentage of the module grade?
3. DEADLINE: Due date
4. PAGE_LIMIT: Report length limit (if any)
5. REQUIRED_TOOLS: R, Python, MATLAB, LaTeX, Word, etc.
6. DATA_PROVIDED: Yes/No, what data?
7. CORE_TASKS: List each main task in order
8. METHODS_REQUIRED: List specific methods/techniques to use
9. GRADING_EMPHASIS: What does the brief emphasize? (e.g., "clear explanation", "correct method", "presentation")
10. PITFALLS: Requirements that students might overlook

Format your response cleanly so it can be parsed."""

        analysis = self._call_llm(
            "You are an expert at analyzing university assignment briefs. Be precise and thorough.",
            prompt
        )
        return {"analysis": analysis}

    # ================================================================
    # Step 2: Generate work plan (structured by task)
    # ================================================================

    def generate_work_plan(self) -> str:
        """生成完整的课程作业工作计划。"""
        print("--- Step 2: Generating detailed work plan ---")

        prompt = f"""You are helping a university student complete a coursework assignment.
Generate a COMPREHENSIVE, STRUCTURED work plan based on the assignment below.

Course: {self.course_code}
Coursework text:
{self.full_text[:10000]}

Generate a detailed work plan with the following sections. Use bilingual format (English + Chinese).

---

# Coursework Analysis & Work Plan / 课程作业分析与工作计划

## 1. Overview / 概览
- Coursework type, weight, deadline, page limit
- Tools needed
- Data provided

## 2. Requirements Breakdown / 需求拆解
Break the assignment into numbered sub-tasks. For each:
- What to do (English + Chinese)
- Which course sections/knowledge points are relevant
- Estimated difficulty (Easy / Medium / Hard)

## 3. Step-by-Step Analysis Plan / 分步分析计划
For EACH sub-task:
### Task X: [Name]
**Goal / 目标**: One sentence
**Relevant Theory / 相关理论**: Course sections and key concepts
**Approach / 方法**: How to tackle this task
**Code Framework / 代码框架** (if applicable): Provide pseudocode or R/Python template with comments
**What to Look For / 注意事项**: Common issues, interpretation tips
**Expected Output / 预期输出**: What should be produced (plot, table, paragraph)

## 4. Report Structure / 报告结构
If the coursework requires a report, provide a detailed outline:
- Title page requirements
- Abstract/Summary structure
- Section-by-section outline with what to include in each
- Figure/table placement suggestions

## 5. Code Organization / 代码组织 (if applicable)
- Suggested script structure
- Key libraries needed
- Tips for reproducible analysis

## 6. Submission Checklist / 提交检查清单
- [ ] Each required element
- [ ] Formatting checks
- [ ] File naming

## 7. Time Management / 时间规划
Suggest a week-by-week plan from now until the deadline.

---

RULES:
1. Be SPECIFIC - reference exact tasks from the coursework
2. Be PRACTICAL - give actionable guidance, not vague advice
3. DO NOT write the full report or complete code - provide frameworks and guidance
4. Use bilingual format throughout
5. Every task should map to course knowledge"""

        work_plan = self._call_llm(
            "You are an experienced university teaching assistant. You help students plan and structure their coursework without doing the work for them. You are practical, specific, and thorough.",
            prompt
        )
        return work_plan

    # ================================================================
    # Step 3: Save
    # ================================================================

    def generate_full_plan(self, save: bool = True) -> str:
        """运行完整分析并保存。"""
        # Step 1: Quick analysis
        analysis_result = self.analyze()

        # Step 2: Detailed work plan
        work_plan = self.generate_work_plan()

        # Combine
        header = f"""# {self.course_code} Coursework Plan / 课程作业计划

> **来源 / Source**: {self.pdf_name}.pdf
> **生成时间 / Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## Quick Analysis / 快速分析

{analysis_result['analysis']}

---

"""
        full_content = header + work_plan

        if save:
            os.makedirs(self.output_dir, exist_ok=True)
            filename = f"Coursework_{self.pdf_name}.md"
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_content)
            print(f"\nSaved: {filepath}")
            print(f"Length: {len(full_content)} chars")

        return full_content

    def _call_llm(self, system_prompt: str, user_prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,
                max_tokens=6000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"API Error: {e}"


# ================================================================
# Find coursework PDFs in a course folder
# ================================================================

def find_coursework_pdfs(course_dir: str) -> list[str]:
    """在一个课程文件夹中找coursework相关的PDF。"""
    coursework_files = []
    if not os.path.exists(course_dir):
        return coursework_files

    for f in os.listdir(course_dir):
        if f.lower().endswith('.pdf'):
            lower = f.lower()
            # 判断是否是coursework: 文件名含有这些关键词
            cw_keywords = ['practical', 'coursework', 'assignment', 'project', '作业', '课程设计']
            # 排除课件和problem sheet
            exclude = ['problem', 'sheet', '课件', 'lecture', 'note', '习题']
            is_cw = any(kw in lower for kw in cw_keywords)
            is_excluded = any(kw in lower for kw in exclude)
            if is_cw and not is_excluded:
                coursework_files.append(os.path.join(course_dir, f))
            # 如果文件名无法判断，只要是PDF且不是课件，也包含
            elif not is_excluded:
                # 不自动包含 - 需要明确表明是coursework
                pass

    return coursework_files


# ================================================================
# Main
# ================================================================

def main():
    import argparse

    ap = argparse.ArgumentParser(description="Coursework helper - analyze and plan")
    ap.add_argument("--course", type=str, default="MATH2702",
                    help="Course code (default: MATH2702)")
    ap.add_argument("--file", type=str, default=None,
                    help="Specific coursework PDF filename (auto-detect if not specified)")
    ap.add_argument("--scan", action="store_true",
                    help="Scan course folder for coursework PDFs")
    args = ap.parse_args()

    course_dir = os.path.join(COURSES_DIR, args.course)
    print(f"Course directory: {course_dir}")

    if args.scan:
        cw_files = find_coursework_pdfs(course_dir)
        print(f"\nFound {len(cw_files)} coursework file(s):")
        for f in cw_files:
            print(f"  {os.path.basename(f)}")
        return

    # Determine which PDF to process
    if args.file:
        pdf_path = os.path.join(course_dir, args.file)
    else:
        cw_files = find_coursework_pdfs(course_dir)
        if not cw_files:
            print("\nNo coursework PDFs found.")
            print("Put your coursework PDF in the course folder (e.g., 课程/MATH2702/practical.pdf)")
            print("Or use --file to specify the PDF filename")
            return
        pdf_path = cw_files[0]
        print(f"Auto-detected: {os.path.basename(pdf_path)}")

    if not os.path.exists(pdf_path):
        print(f"ERROR: {pdf_path} not found")
        return

    helper = CourseworkHelper(args.course, pdf_path)
    helper.generate_full_plan()


if __name__ == "__main__":
    main()
