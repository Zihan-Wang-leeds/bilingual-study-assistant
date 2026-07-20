"""
学习进度追踪 — 记录学生已完成的章节/习题/测验

存储: 课程/课程代码/progress.json
"""
import os
import json
from datetime import datetime, timedelta

PROGRESS_FILE = "progress.json"


class ProgressTracker:
    """跟踪单个课程的学习进度。"""

    def __init__(self, course_dir: str):
        self.course_dir = course_dir
        self.file_path = os.path.join(course_dir, PROGRESS_FILE)
        self.data = self._load()

    def _load(self) -> dict:
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "course_code": os.path.basename(self.course_dir),
            "started": datetime.now().isoformat(),
            "sections_read": [],
            "problems_solved": [],
            "quiz_scores": [],
            "study_sessions": [],
            "total_study_minutes": 0,
        }

    def _save(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    # --- 章节进度 ---

    def mark_section_read(self, section_number: int, section_title: str = ""):
        """标记章节为已读。"""
        if section_number not in self.data["sections_read"]:
            self.data["sections_read"].append(section_number)
            self.data["sections_read"].sort()
        self._save()

    def get_sections_read(self) -> list[int]:
        return sorted(self.data["sections_read"])

    def get_section_progress(self, total_sections: int) -> dict:
        """返回章节完成百分比。"""
        read = len(self.data["sections_read"])
        return {
            "read": read,
            "total": total_sections,
            "percent": round(read / total_sections * 100, 1) if total_sections > 0 else 0,
        }

    # --- 习题进度 ---

    def mark_problem_solved(self, sheet_number: int):
        """标记习题为已做。"""
        if sheet_number not in self.data["problems_solved"]:
            self.data["problems_solved"].append(sheet_number)
            self.data["problems_solved"].sort()
        self._save()

    # --- 测验成绩 ---

    def add_quiz_score(self, topic: str, score: int, total: int):
        """记录测验成绩。"""
        self.data["quiz_scores"].append({
            "date": datetime.now().isoformat(),
            "topic": topic,
            "score": score,
            "total": total,
            "percent": round(score / total * 100, 1) if total > 0 else 0,
        })
        self._save()

    def get_quiz_stats(self) -> dict:
        scores = self.data["quiz_scores"]
        if not scores:
            return {"attempts": 0, "average": 0, "best": 0}
        percents = [s["percent"] for s in scores]
        return {
            "attempts": len(scores),
            "average": round(sum(percents) / len(percents), 1),
            "best": max(percents),
        }

    # --- 学习时长 ---

    def add_study_session(self, minutes: int):
        """记录一次学习会话。"""
        self.data["study_sessions"].append({
            "date": datetime.now().isoformat(),
            "minutes": minutes,
        })
        self.data["total_study_minutes"] += minutes
        self._save()

    def get_study_stats(self) -> dict:
        total = self.data["total_study_minutes"]
        sessions = len(self.data["study_sessions"])
        week_ago = (datetime.now() - timedelta(days=7)).isoformat()
        this_week = sum(
            s["minutes"] for s in self.data["study_sessions"]
            if s["date"] >= week_ago
        )
        return {
            "total_minutes": total,
            "total_hours": round(total / 60, 1),
            "sessions": sessions,
            "this_week_minutes": this_week,
        }

    # --- 完整报告 ---

    def get_report(self, total_sections: int = 0) -> dict:
        """生成完整进度报告。"""
        return {
            "course_code": self.data["course_code"],
            "started": self.data["started"],
            "sections": self.get_section_progress(total_sections),
            "problems_solved": len(self.data["problems_solved"]),
            "quiz": self.get_quiz_stats(),
            "study": self.get_study_stats(),
        }


def get_all_progress(courses_dir: str) -> dict:
    """获取所有课程的进度概览。"""
    all_progress = {}
    if not os.path.exists(courses_dir):
        return all_progress

    for folder in os.listdir(courses_dir):
        folder_path = os.path.join(courses_dir, folder)
        if os.path.isdir(folder_path):
            progress_file = os.path.join(folder_path, PROGRESS_FILE)
            if os.path.exists(progress_file):
                tracker = ProgressTracker(folder_path)
                # 估算章节数（从 guides 目录）
                guides_dir = os.path.join(folder_path, "guides")
                total_sections = 0
                if os.path.exists(guides_dir):
                    import re
                    for f in os.listdir(guides_dir):
                        if f.startswith("Section_") and f.endswith(".md"):
                            total_sections += 1
                all_progress[folder] = tracker.get_report(total_sections)

    return all_progress


if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from config import COURSES_DIR

    print("学习进度总览 / Study Progress Overview")
    print("=" * 50)
    progress = get_all_progress(COURSES_DIR)
    if not progress:
        print("暂无进度数据。开始学习后会自动记录。")
        print("No progress data yet. Progress is tracked as you study.")
    else:
        for course, report in progress.items():
            print(f"\n🎓 {course}")
            print(f"  开始日期: {report['started'][:10]}")
            print(f"  章节进度: {report['sections']['read']}/{report['sections']['total']} ({report['sections']['percent']}%)")
            print(f"  已做习题: {report['problems_solved']} 套")
            q = report['quiz']
            print(f"  测验: {q['attempts']} 次, 平均 {q['average']}%, 最佳 {q['best']}%")
            s = report['study']
            print(f"  学习时长: {s['total_hours']}h ({s['sessions']} 次会话)")
