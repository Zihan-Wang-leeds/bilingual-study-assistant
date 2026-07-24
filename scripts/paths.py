"""
项目路径工具 — 确保所有脚本可以从 scripts/ 目录或项目根目录导入。
在脚本开头用: import paths; paths.setup()
"""
import sys
import os


def setup():
    """将项目根目录和 scripts 目录添加到 sys.path。"""
    _script_dir = os.path.dirname(os.path.abspath(__file__))
    _project_root = os.path.dirname(_script_dir)

    if _script_dir not in sys.path:
        sys.path.insert(0, _script_dir)
    if _project_root not in sys.path:
        sys.path.insert(0, _project_root)
