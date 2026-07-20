"""
学习助手 - Web 应用
Bilingual Study Assistant - Web Application

将终端版 chat.py 转换为 Flask Web 应用。
Run: python web_app.py  →  open http://localhost:5000
"""
import sys
import os
import io
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

# 修复 Windows GBK 终端下 emoji 打印问题
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

from rag_engine import CourseRAG
try:
    from flask import Flask, render_template, request, jsonify, Response, stream_with_context
except ModuleNotFoundError:
    Flask = None

from config import COURSES_DIR
from pdf_loader import extract_text_from_pdf
from chunker import chunk_pdf
from progress_tracker import ProgressTracker, get_all_progress
from generate_flashcards import generate_flashcards, save_flashcards

app = Flask(__name__) if Flask else None

# 全局 RAG 实例（启动时加载索引）
rag = CourseRAG()

MODE_NAMES = {
    "teach": "🧑‍🏫 自学教学 Self-Study Teaching",
    "concept": "📖 概念解释 Concept Explain",
    "homework": "✏️ 作业辅导 Homework Help",
    "review": "📝 考前复习 Exam Review",
    "coursework": "📋 课程作业 Coursework Help",
    "quiz": "📝 模拟测验 Quiz Mode",
}

MODE_DESCRIPTIONS = {
    "teach": "从零开始系统教学：目标→直觉→定义→例题→自测",
    "concept": "快速解释特定概念，公式符号详解",
    "homework": "引导思考，分步提示，不直接给答案",
    "review": "知识框架梳理 + 重要公式 + 自测题",
    "coursework": "需求拆解 + 方法建议 + 代码框架 + 报告结构",
    "quiz": "生成练习题 + 自动批改 + 薄弱点分析",
}


def get_port(default=5001):
    """Read --port N from argv, falling back to PORT env or the default."""
    if "--port" in sys.argv:
        try:
            return int(sys.argv[sys.argv.index("--port") + 1])
        except (IndexError, ValueError):
            print("Invalid --port value, using default 5001.")
            return default
    return int(os.getenv("PORT", default))


# ================================================================
# 页面路由
# ================================================================

if app:
    @app.route('/')
    def index():
        """主页面"""
        return render_template('index.html')


# ================================================================
# API 路由
# ================================================================

def api_stats():
    """获取知识库统计信息"""
    stats = rag.get_course_stats()
    courses = []
    for code in rag.list_courses():
        chunk_count = stats.get(code.upper(), stats.get(code, 0))
        courses.append({
            "code": code.upper() if code else code,
            "chunks": chunk_count
        })
    return {
        "total_courses": len(courses),
        "total_chunks": sum(c["chunks"] for c in courses),
        "courses": courses,
        "index_loaded": len(courses) > 0
    }


def api_courses():
    """列出所有可用课程"""
    stats = rag.get_course_stats()
    courses = []
    for code in rag.list_courses():
        courses.append({
            "code": code.upper() if code else code,
            "chunks": stats.get(code.upper(), stats.get(code, 0))
        })
    return courses


def api_modes():
    """返回所有学习模式的信息"""
    modes = {}
    for key, name in MODE_NAMES.items():
        modes[key] = {
            "name": name,
            "description": MODE_DESCRIPTIONS.get(key, "")
        }
    return modes


def build_chat_response(data):
    """聊天接口 — 返回 JSON（支持对话历史）"""
    if not data:
        return {"error": "Request body required"}, 400

    question = data.get('question', '').strip()
    course_code = data.get('course_code') or None
    mode = data.get('mode', 'teach')
    history = data.get('history') or None

    if not question:
        return {"error": "Question is empty"}, 400

    if mode not in MODE_NAMES:
        mode = 'teach'

    result = rag.ask(question, course_code=course_code, mode=mode, history=history)

    return {
        "answer": result['answer'],
        "sources": result['sources'],
        "mode": mode,
        "course_code": course_code
    }, 200


def api_upload():
    """上传 PDF 课件 — 自动提取 → 分块 → 索引"""
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    course_code = request.form.get('course_code', '').strip().upper()

    if not file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "Only PDF files supported"}), 400
    if not course_code:
        return jsonify({"error": "course_code is required (e.g. MATH2702)"}), 400

    # 创建课程目录
    course_dir = os.path.join(COURSES_DIR, course_code)
    os.makedirs(course_dir, exist_ok=True)

    # 保存文件
    pdf_filename = file.filename
    pdf_path = os.path.join(course_dir, pdf_filename)
    file.save(pdf_path)

    # 处理: 提取 → 分块 → 索引
    try:
        pages = extract_text_from_pdf(pdf_path)
        chunks = chunk_pdf(pages)
        course_name = course_code
        rag.add_chunks(course_code, course_name, chunks)

        # 尝试语义索引
        try:
            from semantic_search import SemanticSearch
            sem = SemanticSearch()
            if sem.is_ready:
                sem.add_chunks(course_code, chunks)
        except Exception:
            pass

        return jsonify({
            "success": True,
            "course_code": course_code,
            "filename": pdf_filename,
            "pages": len(pages),
            "chunks": len(chunks),
            "message": f"✅ {course_code} indexed: {len(pages)} pages, {len(chunks)} chunks"
        }), 200
    except Exception as e:
        return jsonify({"error": f"Processing failed: {str(e)}"}), 500


def api_guides():
    """列出课程的所有教材文件"""
    course_code = request.args.get('course', '').strip().upper()
    if not course_code:
        return {"error": "course parameter required"}, 400
    guides_dir = os.path.join(COURSES_DIR, course_code, "guides")
    if not os.path.exists(guides_dir):
        return {"guides": [], "course": course_code}
    files = []
    for f in sorted(os.listdir(guides_dir)):
        if f.endswith('.md'):
            path = os.path.join(guides_dir, f)
            size = os.path.getsize(path)
            files.append({"name": f, "size": size, "size_kb": round(size/1024, 1)})
    return {"guides": files, "course": course_code, "count": len(files)}


def api_flashcards_generate():
    """生成闪卡"""
    data = request.get_json() or {}
    course_code = data.get('course_code', '').strip().upper()
    if not course_code:
        return {"error": "course_code required"}, 400
    pdf_path = os.path.join(COURSES_DIR, course_code, "课件.pdf")
    if not os.path.exists(pdf_path):
        return {"error": f"课件.pdf not found for {course_code}"}, 404
    try:
        cards = generate_flashcards(course_code, pdf_path)
        output_dir = os.path.join(COURSES_DIR, course_code, "guides")
        save_flashcards(course_code, output_dir, cards)
        return {"success": True, "count": len(cards), "message": f"Generated {len(cards)} flashcards"}
    except Exception as e:
        return {"error": str(e)}, 500


def api_flashcards_list():
    """获取已生成的闪卡内容"""
    course_code = request.args.get('course', '').strip().upper()
    if not course_code:
        return {"error": "course parameter required"}, 400
    md_path = os.path.join(COURSES_DIR, course_code, "guides", "Flashcards.md")
    if not os.path.exists(md_path):
        return {"cards": [], "exists": False}
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Parse cards from markdown
    cards = []
    import re
    for m in re.finditer(r'## Card (\d+): (.+?)\n\n\*\*Front.+\*\*: (.+?)\n\n\*\*Back.+\*\*: (.+?)\n\n\*\*中文\*\*: (.+?)\n\n', content):
        cards.append({"id": m.group(1), "title": m.group(2), "front": m.group(3), "back": m.group(4), "cn": m.group(5)})
    return {"cards": cards, "exists": True, "count": len(cards)}


def api_progress():
    """获取课程学习进度"""
    course_code = request.args.get('course', '').strip().upper()
    if not course_code:
        all_p = get_all_progress(COURSES_DIR)
        return {"all": all_p}
    course_dir = os.path.join(COURSES_DIR, course_code)
    if not os.path.exists(course_dir):
        return {"error": "Course not found"}, 404
    tracker = ProgressTracker(course_dir)
    guides_dir = os.path.join(course_dir, "guides")
    total_sections = 0
    total_problems = 0
    if os.path.exists(guides_dir):
        for f in os.listdir(guides_dir):
            if f.startswith("Section_") and f.endswith(".md"):
                total_sections += 1
            if f.startswith("Problem_Sheet_") and f.endswith(".md"):
                total_problems += 1
    report = tracker.get_report(total_sections)
    report["total_problems"] = total_problems
    return report


def api_progress_mark():
    """标记学习进度"""
    data = request.get_json() or {}
    course_code = data.get('course_code', '').strip().upper()
    action = data.get('action', '')
    if not course_code:
        return {"error": "course_code required"}, 400
    course_dir = os.path.join(COURSES_DIR, course_code)
    if not os.path.exists(course_dir):
        return {"error": "Course not found"}, 404
    tracker = ProgressTracker(course_dir)
    if action == 'section_read' and data.get('number'):
        tracker.mark_section_read(int(data['number']), data.get('title', ''))
        return {"success": True, "sections_read": tracker.get_sections_read()}
    elif action == 'problem_solved' and data.get('number'):
        tracker.mark_problem_solved(int(data['number']))
        return {"success": True, "problems_solved": tracker.data["problems_solved"]}
    elif action == 'study_session' and data.get('minutes'):
        tracker.add_study_session(int(data['minutes']))
        return {"success": True, "stats": tracker.get_study_stats()}
    elif action == 'quiz_score' and data.get('score') is not None:
        tracker.add_quiz_score(data.get('topic', 'Web Quiz'), int(data['score']), int(data.get('total', 10)))
        return {"success": True, "quiz_stats": tracker.get_quiz_stats()}
    else:
        return {"error": f"Unknown action: {action}"}, 400


def api_export_pdf():
    """导出教材为 PDF"""
    data = request.get_json() or {}
    course_code = data.get('course_code', '').strip().upper()
    section = data.get('section')
    if not course_code:
        return {"error": "course_code required"}, 400
    guides_dir = os.path.join(COURSES_DIR, course_code, "guides")
    if not os.path.exists(guides_dir):
        return {"error": "No guides found"}, 404
    try:
        from export_pdf import export_to_pdf
        if section:
            import re
            pattern = re.compile(rf'Section_{section:02d}_.*\.md')
            for f in os.listdir(guides_dir):
                if pattern.match(f):
                    md_path = os.path.join(guides_dir, f)
                    output = export_to_pdf(md_path)
                    return {"success": True, "output": output, "filename": os.path.basename(output)}
            return {"error": f"Section {section} not found"}, 404
        else:
            return {"error": "Specify --section or use --all in CLI"}, 400
    except Exception as e:
        return {"error": str(e)}, 500


if app:
    # GET routes
    app.add_url_rule('/api/stats', 'api_stats', lambda: jsonify(api_stats()))
    app.add_url_rule('/api/courses', 'api_courses', lambda: jsonify(api_courses()))
    app.add_url_rule('/api/modes', 'api_modes', lambda: jsonify(api_modes()))
    app.add_url_rule('/api/guides', 'api_guides', lambda: (
        lambda r: jsonify(r[0]) if isinstance(r, tuple) else jsonify(r)
    )(api_guides()))
    app.add_url_rule('/api/flashcards', 'api_flashcards', lambda: jsonify(api_flashcards_list()))
    app.add_url_rule('/api/progress', 'api_progress', lambda: jsonify(api_progress()))

    # POST routes
    @app.route('/api/upload', methods=['POST'])
    def upload_route():
        payload, status = api_upload()
        return jsonify(payload), status

    @app.route('/api/flashcards/generate', methods=['POST'])
    def flashcards_generate_route():
        payload, status = api_flashcards_generate()
        return jsonify(payload), status

    @app.route('/api/progress/mark', methods=['POST'])
    def progress_mark_route():
        payload, status = api_progress_mark()
        return jsonify(payload), status

    @app.route('/api/export', methods=['POST'])
    def export_route():
        payload, status = api_export_pdf()
        return jsonify(payload), status

    @app.route('/api/chat', methods=['POST'])
    def api_chat():
        payload, status = build_chat_response(request.get_json())
        return jsonify(payload), status

    @app.route('/api/chat/stream', methods=['POST'])
    def api_chat_stream():
        """聊天接口 — 真正的 SSE 流式返回"""
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body required"}), 400

        question = data.get('question', '').strip()
        course_code = data.get('course_code') or None
        mode = data.get('mode', 'teach')
        history = data.get('history') or None

        if not question:
            return jsonify({"error": "Question is empty"}), 400

        if mode not in MODE_NAMES:
            mode = 'teach'

        def generate():
            try:
                for kind, value in rag.ask_stream(question, course_code=course_code, mode=mode, history=history):
                    if kind == "meta":
                        # 元数据直接发送，不用 token 包装
                        yield f"data: {json.dumps(value, ensure_ascii=False)}\n\n"
                    else:
                        # 文本 token
                        yield f"data: {json.dumps({'token': value}, ensure_ascii=False)}\n\n"
                yield "data: [DONE]\n\n"
            except Exception as e:
                import traceback
                traceback.print_exc()
                yield f"data: {json.dumps({'token': f'❌ 服务器错误: {str(e)}'}, ensure_ascii=False)}\n\n"
                yield "data: [DONE]\n\n"

        return Response(
            stream_with_context(generate()),
            mimetype='text/event-stream',
            headers={
                'Cache-Control': 'no-cache',
                'X-Accel-Buffering': 'no'
            }
        )


class StudyAssistantHandler(BaseHTTPRequestHandler):
    """Small no-dependency fallback server for machines without Flask."""

    def log_message(self, format, *args):
        print("%s - %s" % (self.address_string(), format % args))

    def _send_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, path):
        with open(path, 'rb') as f:
            body = f.read()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == '/':
            self._send_html(os.path.join(os.path.dirname(__file__), 'templates', 'index.html'))
        elif path == '/api/stats':
            self._send_json(api_stats())
        elif path == '/api/courses':
            self._send_json(api_courses())
        elif path == '/api/modes':
            self._send_json(api_modes())
        else:
            self._send_json({"error": "Not found"}, 404)

    def do_POST(self):
        path = urlparse(self.path).path
        if path != '/api/chat':
            self._send_json({"error": "Not found"}, 404)
            return

        length = int(self.headers.get('Content-Length', 0))
        raw_body = self.rfile.read(length).decode('utf-8') if length else ''
        try:
            data = json.loads(raw_body) if raw_body else None
        except json.JSONDecodeError:
            self._send_json({"error": "Invalid JSON"}, 400)
            return

        payload, status = build_chat_response(data)
        self._send_json(payload, status)


# ================================================================
# 启动
# ================================================================

if __name__ == '__main__':
    port = get_port()

    print(r"""
  ╔══════════════════════════════════════════════════╗
  ║   🧑‍🏫 Bilingual Study Assistant / 双语学习助手     ║
  ║              Web Version / 网页版                  ║
  ╚══════════════════════════════════════════════════╝
    """)

    stats = rag.get_course_stats()
    if not stats:
        print("\n⚠️  知识库为空！请先运行: python scripts/build_index.py")
        print("   Knowledge base is empty! Run build_index.py first.\n")

    print(f"📚 已加载 {len(stats)} 门课程")
    for code, count in stats.items():
        print(f"   🎓 {code}: {count} 个文档块")

    print("\n🌐 启动 Web 服务器...")
    print(f"   Open in browser / 浏览器打开: http://localhost:{port}\n")

    if app:
        app.run(debug=True, host='0.0.0.0', port=port)
    else:
        print("   Flask 未安装，已使用 Python 标准库服务器启动。")
        server = ThreadingHTTPServer(('0.0.0.0', port), StudyAssistantHandler)
        server.serve_forever()
