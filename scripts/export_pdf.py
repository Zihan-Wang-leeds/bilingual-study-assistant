"""
PDF 导出工具 — 将生成的 Markdown 教材转换为排版精美的 PDF

依赖: pip install markdown weasyprint (可选，首次运行会提示)
回退方案: 如果 weasyprint 不可用，使用 pandoc (需系统安装)
"""
import os
import sys
import re
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import COURSES_DIR

OUTPUT_DIR = "guides"


def md_to_html(md_content: str) -> str:
    """将 Markdown 转为带样式的 HTML。"""
    try:
        import markdown
        md = markdown.Markdown(extensions=['tables', 'fenced_code', 'codehilite', 'toc'])
        body = md.convert(md_content)
    except ImportError:
        # 基本回退：保留纯文本
        body = f"<pre>{md_content}</pre>"

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<style>
  body {{ font-family: 'Helvetica Neue', Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif;
         max-width: 800px; margin: 0 auto; padding: 40px 20px; line-height: 1.8; color: #1d1d1f; }}
  h1 {{ font-size: 1.8em; border-bottom: 2px solid #2563eb; padding-bottom: 8px; }}
  h2 {{ font-size: 1.4em; margin-top: 30px; color: #2563eb; }}
  h3 {{ font-size: 1.1em; margin-top: 24px; }}
  blockquote {{ border-left: 4px solid #e5e7eb; margin: 16px 0; padding: 8px 16px;
                background: #f9fafb; color: #6b7280; }}
  table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
  th, td {{ border: 1px solid #d1d5db; padding: 8px 12px; text-align: left; }}
  th {{ background: #f3f4f6; }}
  code {{ background: #f3f4f6; padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }}
  pre {{ background: #1e1e1e; color: #d4d4d4; padding: 16px; border-radius: 8px; overflow-x: auto; }}
  .math {{ font-style: italic; }}
  @media print {{ body {{ font-size: 11pt; }} }}
</style>
</head>
<body>
{body}
</body>
</html>"""
    return html


def export_to_pdf(md_path: str, output_path: str = None) -> str:
    """
    将 Markdown 文件导出为 PDF。

    尝试 weasyprint → pandoc → 报错。
    """
    if output_path is None:
        output_path = md_path.replace('.md', '.pdf')

    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 尝试 weasyprint
    try:
        from weasyprint import HTML
        html = md_to_html(md_content)
        HTML(string=html).write_pdf(output_path)
        print(f"✅ PDF exported (weasyprint): {output_path}")
        return output_path
    except ImportError:
        pass
    except Exception as e:
        print(f"⚠️  weasyprint failed: {e}")

    # 回退：pandoc
    import subprocess
    try:
        result = subprocess.run(
            ['pandoc', md_path, '-o', output_path,
             '--pdf-engine=xelatex', '-V', 'mainfont=PingFang SC',
             '-V', 'CJKmainfont=PingFang SC'],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0:
            print(f"✅ PDF exported (pandoc): {output_path}")
            return output_path
        else:
            print(f"⚠️  pandoc failed: {result.stderr[:200]}")
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"⚠️  pandoc failed: {e}")

    # 无法导出
    print("❌ PDF export requires one of: pip install weasyprint  OR  brew install pandoc")
    print("   HTML preview saved instead.")
    html_path = output_path.replace('.pdf', '.html')
    html = md_to_html(md_content)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"   HTML file: {html_path}")
    return html_path


def export_course_guides(course_code: str, output_format: str = "pdf"):
    """导出课程所有教材。"""
    course_dir = os.path.join(COURSES_DIR, course_code)
    guides_dir = os.path.join(course_dir, OUTPUT_DIR)
    export_dir = os.path.join(guides_dir, "exports")
    os.makedirs(export_dir, exist_ok=True)

    if not os.path.exists(guides_dir):
        print(f"No guides found for {course_code}")
        return

    md_files = sorted([
        f for f in os.listdir(guides_dir)
        if f.endswith('.md') and f != 'README.md'
    ])

    print(f"\n📦 Exporting {len(md_files)} guides for {course_code}...")

    for md_file in md_files:
        md_path = os.path.join(guides_dir, md_file)
        output_name = md_file.replace('.md', f'.{output_format}')
        output_path = os.path.join(export_dir, output_name)
        export_to_pdf(md_path, output_path)

    print(f"\n✅ Exports saved to: {export_dir}")


def main():
    import argparse

    ap = argparse.ArgumentParser(description="Export study guides to PDF")
    ap.add_argument("--course", type=str, required=True, help="Course code")
    ap.add_argument("--section", type=int, default=None, help="Single section number")
    ap.add_argument("--all", action="store_true", help="Export all guides")
    args = ap.parse_args()

    course_code = args.course.upper()
    guides_dir = os.path.join(COURSES_DIR, course_code, OUTPUT_DIR)

    if not os.path.exists(guides_dir):
        print(f"No guides found for {course_code}")
        return

    if args.section:
        # Find matching section file
        pattern = re.compile(rf'Section_{args.section:02d}_.*\.md')
        for f in os.listdir(guides_dir):
            if pattern.match(f):
                md_path = os.path.join(guides_dir, f)
                export_to_pdf(md_path)
                return
        print(f"Section {args.section} not found")
        return

    if args.all:
        export_course_guides(course_code)
        return

    print("Usage: --section N (single) or --all (all guides)")
    print(f"Example: python scripts/export_pdf.py --course MATH2702 --section 1")


if __name__ == "__main__":
    main()
