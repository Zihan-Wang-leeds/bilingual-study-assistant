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
TEMPERATURE = 0.3      # 生成温度
MAX_TOKENS = 2000      # 最大输出长度

# ============================================================
# 路径配置
# ============================================================
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSES_DIR = os.path.join(PROJECT_ROOT, "课程")
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, "scripts")
PROMPTS_DIR = os.path.join(PROJECT_ROOT, "prompts")
