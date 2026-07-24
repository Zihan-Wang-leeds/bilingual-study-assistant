"""
学习助手 - 全局配置
"""
import os
from dotenv import load_dotenv

load_dotenv()

# ============================================================
# API 配置
# ============================================================
API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
BASE_URL = "https://api.deepseek.com/v1"
MODEL_NAME = "deepseek-chat"

# ============================================================
# 向量数据库配置
# ============================================================
CHROMA_DB_PATH = "./chroma_db"
EMBEDDING_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"

# ============================================================
# 文档分块配置
# ============================================================
CHUNK_SIZE = 800       # 每块最大字符数
CHUNK_OVERLAP = 100    # 块之间重叠字符数

# ============================================================
# 检索配置
# ============================================================
TOP_K = 5              # 默认检索文档数
TEMPERATURE = 0.3      # RAG 对话生成温度
MAX_TOKENS = 6000      # RAG 对话最大输出长度
CHAT_HISTORY_LENGTH = 6  # 对话历史保留轮数

# 各模式最大输出 token 数（教学模式需要更多空间）
MODE_MAX_TOKENS = {
    "teach": 8000,       # 自学教学：目标→直觉→定义→例题→误区→自测→总结
    "concept": 3000,     # 概念解释：定义+公式+例子+关联
    "homework": 3000,    # 作业辅导：分步引导
    "review": 6000,      # 考前复习：框架+公式+题型+自测
    "coursework": 8000,  # 课程作业：需求拆解+方法+代码+报告
    "quiz": 6000,        # 模拟测验：出题+批改+分析
}

# ============================================================
# 教材/习题生成配置
# ============================================================
GENERATION_TEMPERATURE = 0.3   # 教材/习题解答生成温度
GENERATION_MAX_TOKENS = 6000   # 教材/习题解答最大输出长度
GENERATION_SLEEP = 2           # API 调用间隔（秒），避免限流

# ============================================================
# 路径配置
# ============================================================
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSES_DIR = os.path.join(PROJECT_ROOT, "课程")
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, "scripts")
PROMPTS_DIR = os.path.join(PROJECT_ROOT, "prompts")
