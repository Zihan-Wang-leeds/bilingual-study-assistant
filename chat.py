"""
学习助手 - 交互式对话界面
Bilingual Study Assistant - Interactive Chat
"""
import sys
import os
import runpy

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

from config import CHAT_HISTORY_LENGTH
from rag_engine import CourseRAG


def launch_web_app():
    """Start the browser-based app from this chat.py entry point."""
    web_app_path = os.path.join(os.path.dirname(__file__), 'web_app.py')
    runpy.run_path(web_app_path, run_name="__main__")


def print_banner():
    print(r"""
  ╔══════════════════════════════════════════════════╗
  ║     Bilingual Study Assistant / 双语学习助手       ║
  ║                                                  ║
  ║  🧑‍🏫 自学教学 | 📖 概念解释 | ✏️ 作业辅导 | 📝 考前复习 | 📋 Coursework  ║
  ╚══════════════════════════════════════════════════╝
    """)


def print_modes():
    print("""
  Select mode / 选择模式:
    [1] 🧑‍🏫 Self-Study Teaching / 自学教学 (recommended)
        → Teach you the topic from scratch, bilingual, step by step
        → 从零开始教你，中英双语，一步步来
    [2] 📖 Concept Explain / 概念解释
        → Quick explanation of a specific concept
        → 快速解释特定概念
    [3] ✏️ Homework Help / 作业辅导
        → Guide your thinking, don't give direct answers
        → 引导思考，不直接给答案
    [4] 📝 Exam Review / 考前复习
        → Summarize knowledge, generate self-test questions
        → 总结知识点，生成自测题
    [5] 📋 Coursework Help / 课程作业辅助
        → Break down coursework tasks, plan approach, report structure
        → 拆解作业要求，规划方法，报告结构
    [6] 📝 Quiz / 模拟测验
        → Generate practice quizzes + auto-grade your answers
        → 生成练习题 + 自动批改
    [7] 🗂️  View Knowledge Base / 查看知识库
  """)


def main():
    rag = CourseRAG()
    print_banner()

    # Check knowledge base
    stats = rag.get_course_stats()
    if not stats:
        print("Knowledge base is empty! Run build_index.py first.")
        print("  python scripts/build_index.py")
        return

    # Show available courses
    print("Courses indexed / 已导入课程:")
    for code, count in stats.items():
        print(f"  {code} ({count} blocks/chunks)")

    # Select course
    course = input("\nCourse code / 课程代码 (Enter = search all): ").strip()
    if not course:
        course = None
        print("  Will search all courses / 将搜索全部课程")

    # Select mode
    print_modes()
    mode_map = {"1": "teach", "2": "concept", "3": "homework", "4": "review", "5": "coursework", "6": "quiz", "7": "stats"}
    mode_choice = input("Select / 选择 (1-6, default/默认=1): ").strip() or "1"

    if mode_choice == "7":
        print("\nKnowledge Base / 知识库详情:")
        for code in rag.list_courses():
            stats = rag.get_course_stats(code.upper())
            print(f"  {code}: {stats.get(code.upper(), 0)} blocks")
        return

    mode = mode_map.get(mode_choice, "teach")
    mode_names = {
        "teach": "自学教学 Self-Study Teaching",
        "concept": "概念解释 Concept Explain",
        "homework": "作业辅导 Homework Help",
        "review": "考前复习 Exam Review",
        "coursework": "课程作业 Coursework Help",
        "quiz": "模拟测验 Quiz Mode",
    }
    print(f"\nCurrent mode / 当前模式: {mode_names[mode]}")
    print("Tips / 提示: /mode /course /progress /clear, exit to quit")

    # Conversation history
    history = []

    # Main chat loop
    while True:
        user_input = input("\nYou / 你: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("\nGood luck with your studies! / 学习加油！")
            break

        # Commands
        if user_input.startswith("/mode"):
            print_modes()
            new_choice = input("Select (1-5): ").strip()
            if new_choice in mode_map and new_choice != "6":
                mode = mode_map[new_choice]
                print(f"Switched to / 切换到: {mode_names[mode]}")
            continue

        if user_input.startswith("/course"):
            new_course = input("Course code (Enter=all): ").strip()
            course = new_course if new_course else None
            print(f"Switched to / 切换到: {course if course else 'All courses / 全部课程'}")
            continue

        if user_input.startswith("/clear"):
            history = []
            print("History cleared / 对话历史已清除")
            continue

        if user_input.startswith("/progress"):
            try:
                from progress_tracker import get_all_progress
                from config import COURSES_DIR
                all_p = get_all_progress(COURSES_DIR)
                if not all_p:
                    print("\n暂无进度数据。学习过程中会自动记录。")
                else:
                    for c, r in all_p.items():
                        print(f"\n🎓 {c}")
                        print(f"  📖 章节: {r['sections']['read']}/{r['sections']['total']} ({r['sections']['percent']}%)")
                        print(f"  ✏️ 习题: {r['problems_solved']} 套")
                        if r['quiz']['attempts'] > 0:
                            print(f"  📝 测验: {r['quiz']['attempts']} 次, 平均 {r['quiz']['average']}%, 最佳 {r['quiz']['best']}%")
                        print(f"  ⏱️ 学习: {r['study']['total_hours']}h")
            except Exception as e:
                print(f"进度加载失败: {e}")
            continue

        # Search + Generate
        print("\nSearching course materials / 正在检索课程资料...")
        result = rag.ask(user_input, course_code=course, mode=mode, history=history)

        # Save to history
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": result['answer']})
        # Trim to configured length (×2 for user+assistant pairs)
        max_msgs = CHAT_HISTORY_LENGTH * 2
        if len(history) > max_msgs:
            history = history[-max_msgs:]

        print(f"\n{'='*60}")
        print(result['answer'])
        print(f"{'='*60}")

        # Show sources
        if result['sources']:
            print("\nReference / 参考来源:")
            for i, src in enumerate(result['sources'], 1):
                where = f"{src['course']}" if src['course'] else ""
                if src['section_title']:
                    where += f" | Section {src['section']}: {src['section_title']}"
                elif src['section']:
                    where += f" | Section {src['section']}"
                print(f"  [{i}] {where}")


if __name__ == "__main__":
    if "--web" in sys.argv:
        launch_web_app()
    else:
        main()
