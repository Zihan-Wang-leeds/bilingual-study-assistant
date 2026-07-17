# CLAUDE.md

本文件为 Claude Code 提供项目指引。这是一个**双语（中文英文）大学自学助手**项目，帮助留学生基于课件自主学习。

## 项目概述

核心定位：**AI导师**。四大功能：

1. **章节教材生成** — 将课件转化为中英双语自学教材（含定义、证明、例题）
2. **习题解答生成** — 提取课件中的Problem Sheet，给出详细逐步解题过程
3. **Coursework 辅助** — 解析课程作业(Practical/Coursework)要求，生成分步工作计划
4. **互动问答** — 基于课程内容的检索增强问答，5种模式

## 项目结构

```
学习帮助/
├── 课程/                  # 课程PDF课件存放
│   ├── MATH2702/          # 随机过程（已生成教材+习题）
│   └── MATH2703/          # 时间序列（含coursework）
│       ├── 课件.pdf / practical.pdf / ...
│       └── guides/         # （自动生成）教材 + 习题解答 + Coursework计划
├── scripts/               # 核心代码
│   ├── config.py          # 全局配置（API、路径、参数）
│   ├── pdf_loader.py      # PDF文本提取
│   ├── chunker.py         # 智能分块（按页面范围 + 章节标注）
│   ├── rag_engine.py      # RAG核心引擎（TF-IDF检索 + LLM生成，5种模式）
│   ├── build_index.py     # 扫描课程目录，构建TF-IDF索引
│   ├── generate_guide.py  # 批量生成章节自学教材
│   ├── solve_problems.py  # 提取并解答Problem Sheet
│   └── coursework_helper.py # Coursework需求分析+分步工作计划
├── prompts/
│   └── study_modes.py     # 五种学习模式的详细Prompt模板
├── knowledge_index.json   # 知识库索引（持久化）
├── chat.py                # 交互式对话界面（5种模式，双语，终端版）
├── web_app.py             # Web 应用版本（Flask 后端）
└── CLAUDE.md              # 本文件
```

## 常用命令

```bash
# === 添加新课程 ===
# 1. 将课件PDF放入 课程/课程代码/ 文件夹
# 2. 生成教材 + 习题解答
python scripts/generate_guide.py --all
python scripts/solve_problems.py --all

# === Coursework 辅助 ===
python scripts/coursework_helper.py --course MATHXXXX    # 自动检测coursework PDF
python scripts/coursework_helper.py --course MATHXXXX --file practical.pdf
python scripts/coursework_helper.py --scan               # 扫描课程文件夹

# === 生成自学教材 ===
python scripts/generate_guide.py --all                   # 全部章节
python scripts/generate_guide.py --section 1             # 单章测试

# === 生成习题解答 ===
python scripts/solve_problems.py --all                   # 全部Problem Sheet
python scripts/solve_problems.py --sheet 1               # 单个Problem Sheet测试

# === 互动问答 ===
python scripts/build_index.py                            # 先构建索引
python chat.py                                           # 启动对话(5种模式，终端版)
python web_app.py                                        # 启动Web网页版 (浏览器 http://localhost:5000)

# === 调试测试 ===
python scripts/chunker.py                                # 测试分块效果
python scripts/rag_engine.py                             # 测试RAG引擎
```

## 添加新课件的完整步骤

1. 在 `课程/` 下新建文件夹，命名为课程代码（如 `COMP2000`）
2. 将PDF课件放入该文件夹：
   - `课件.pdf` → 课程讲义/Slides
   - `practical.pdf` 或 `coursework.pdf` → 课程作业
3. 运行 `python scripts/generate_guide.py --all` 生成自学教材
4. 运行 `python scripts/solve_problems.py --all` 生成习题解答
5. 运行 `python scripts/coursework_helper.py` 生成课程作业计划（如有）
6. 运行 `python scripts/build_index.py` 构建检索索引
7. 通过 `python chat.py` 进行互动提问
8. 生成的文档在 `课程/课程代码/guides/` 下

## 五种学习模式（chat.py）

| # | 模式 | 用途 | 风格 |
|---|------|------|------|
| 1 | `teach` | **自学教学**（默认） | 从零教起：目标→直觉→定义→例题→误区→自测；中英双语 |
| 2 | `concept` | 概念解释 | 快速定义 + 公式符号解释 + 关联知识 |
| 3 | `homework` | 作业辅导 | 引导思考，分步提示，不直接给答案 |
| 4 | `review` | 考前复习 | 知识框架 + 重要公式 + 常见题型 + 自测题 |
| 5 | `coursework` | **课程作业辅助** | 需求拆解 + 方法建议 + 代码框架 + 报告结构 |

### 各模式的回答结构

| 模式 | 结构 |
|------|------|
| `teach` | 学习目标 → 前置知识 → 直觉理解 → 形式化定义 → 关键性质 → 例题 → 常见误区 → 知识关联 → 自测题 → 要点总结 |
| `concept` | 核心定义 → 详细解释 → 公式符号 → 例子 → 关联知识 |
| `homework` | 考查知识点 → 相关理论 → 解题思路框架 → 注意事项 |
| `review` | 知识框架 → 重要公式 → 逻辑关系 → 常见题型 → 自测题 |
| `coursework` | 需求分析 → 任务拆分 → 方法建议 → 代码框架 → 报告结构 → 检查清单 |

## Coursework 辅助详解

### coursework_helper.py 自动生成

输入：coursework PDF（如 `practical.pdf`）
输出：`guides/Coursework_xxx.md`

包含7个部分：
1. **快速分析** — JSON格式：作业类型、占比、截止日期、工具、核心任务、评分重点、常见遗漏
2. **需求拆解** — 每个子任务的目标、相关知识、难度评级
3. **分步分析计划** — 每步有：目标/理论/方法/代码框架/注意事项/预期输出
4. **报告结构** — 标题页 + 摘要结构 + 逐节大纲 + 图表位置
5. **代码组织** — 脚本结构 + 所需库 + 可重现分析技巧
6. **提交检查清单** — 逐项核对
7. **时间规划** — 从当前到截止日期的周计划

### chat.py coursework 模式

在 chat.py 选 `[5]` 进入 coursework 模式，典型用法：
- "这个要求是什么意思？" → 拆解说明
- "我应该怎么入手分析？" → 分步分析计划
- "如何写这部分R/Python代码？" → 带注释的代码框架
- "报告怎么组织结构？" → 逐节大纲
- "这个诊断图/结果怎么解读？" → 解读指南
- "我的分析方法对吗？" → 评估 + 改进建议

## 自学教材结构（generate_guide.py）

每个章节的Markdown文件包含：
- Section Overview / 章节概览
- Learning Objectives / 学习目标
- Prerequisites / 前置知识
- Core Content / 核心内容（每小节：直觉+定义+性质+例题）
- Connections / 知识关联
- Common Mistakes / 常见误区
- Practice / 练习
- Key Takeaways / 要点总结

## 习题解答结构（solve_problems.py）

每个Problem Sheet的Markdown文件包含：
- 问题概览（题数、考查章节）
- 每道题：题目原文 + 中文翻译 + 考查知识点 + 逐步详解 + 最终答案 + 解题要点

## API配置

- API Key 存放在项目 `.env` 文件的 `DEEPSEEK_API_KEY` 中
- 如Key失效，运行旧项目的 `check_key.py` 检查

## 当前已导入课程

- **MATH2702** - Stochastic Processes (University of Leeds, 2025-2026)
  - 105页课件 → 21章教材 (425KB) + 11套习题解答 (204KB)
  - 内容：离散/连续时间Markov链、随机游走、鞅、Gambler's Ruin、Poisson过程、排队论

- **MATH2703** - Time Series Analysis (University of Leeds, 2025-2026)
  - Practical coursework: 数据分析 + 报告（20%权重）
  - 已生成详细 Coursework 工作计划
