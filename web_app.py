"""
学习助手 - Web 应用
Bilingual Study Assistant - Web Application

将终端版 chat.py 转换为 Flask Web 应用。
Run: python web_app.py  →  open http://localhost:5000
"""
import sys
import os
import json
import io

# 修复 Windows GBK 终端下 emoji 打印问题
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from rag_engine import CourseRAG
from config import TOP_K

app = Flask(__name__)

# 全局 RAG 实例（启动时加载索引）
rag = CourseRAG()

MODE_NAMES = {
    "teach": "🧑‍🏫 自学教学 Self-Study Teaching",
    "concept": "📖 概念解释 Concept Explain",
    "homework": "✏️ 作业辅导 Homework Help",
    "review": "📝 考前复习 Exam Review",
    "coursework": "📋 课程作业 Coursework Help",
}

MODE_DESCRIPTIONS = {
    "teach": "从零开始系统教学：目标→直觉→定义→例题→自测",
    "concept": "快速解释特定概念，公式符号详解",
    "homework": "引导思考，分步提示，不直接给答案",
    "review": "知识框架梳理 + 重要公式 + 自测题",
    "coursework": "需求拆解 + 方法建议 + 代码框架 + 报告结构",
}


# ================================================================
# 页面路由
# ================================================================

@app.route('/')
def index():
    """主页面"""
    return render_template('index.html')


# ================================================================
# API 路由
# ================================================================

@app.route('/api/stats')
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
    return jsonify({
        "total_courses": len(courses),
        "total_chunks": sum(c["chunks"] for c in courses),
        "courses": courses,
        "index_loaded": len(courses) > 0
    })


@app.route('/api/courses')
def api_courses():
    """列出所有可用课程"""
    stats = rag.get_course_stats()
    courses = []
    for code in rag.list_courses():
        courses.append({
            "code": code.upper() if code else code,
            "chunks": stats.get(code.upper(), stats.get(code, 0))
        })
    return jsonify(courses)


@app.route('/api/modes')
def api_modes():
    """返回所有学习模式的信息"""
    modes = {}
    for key, name in MODE_NAMES.items():
        modes[key] = {
            "name": name,
            "description": MODE_DESCRIPTIONS.get(key, "")
        }
    return jsonify(modes)


@app.route('/api/chat', methods=['POST'])
def api_chat():
    """聊天接口 — 返回 JSON"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body required"}), 400

    question = data.get('question', '').strip()
    course_code = data.get('course_code') or None
    mode = data.get('mode', 'teach')

    if not question:
        return jsonify({"error": "Question is empty"}), 400

    if mode not in MODE_NAMES:
        mode = 'teach'

    result = rag.ask(question, course_code=course_code, mode=mode)

    return jsonify({
        "answer": result['answer'],
        "sources": result['sources'],
        "mode": mode,
        "course_code": course_code
    })


@app.route('/api/chat/stream', methods=['POST'])
def api_chat_stream():
    """聊天接口 — SSE 流式返回（给未来扩展用，目前回退到非流式）"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body required"}), 400

    question = data.get('question', '').strip()
    course_code = data.get('course_code') or None
    mode = data.get('mode', 'teach')

    if not question:
        return jsonify({"error": "Question is empty"}), 400

    if mode not in MODE_NAMES:
        mode = 'teach'

    def generate():
        result = rag.ask(question, course_code=course_code, mode=mode)
        yield f"data: {json.dumps({'answer': result['answer'], 'sources': result['sources'], 'mode': mode, 'course_code': course_code}, ensure_ascii=False)}\n\n"
        yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no'
        }
    )


# ================================================================
# 启动
# ================================================================

if __name__ == '__main__':
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
    print("   Open in browser / 浏览器打开: http://localhost:5000\n")

    app.run(debug=True, host='0.0.0.0', port=5000)
