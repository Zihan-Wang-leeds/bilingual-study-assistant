# Bilingual Study Assistant / 双语学习助手

一个面向中文留学生的课程自学助手，基于课程资料做检索增强问答，并提供中英双语解释、概念讲解、作业辅导、考前复习和 coursework 辅助。

## Features

- 终端聊天入口：`chat.py`
- 网页聊天入口：`web_app.py` 或 `chat.py --web`
- TF-IDF 课程资料检索
- 五种学习模式：
  - Self-Study Teaching / 自学教学
  - Concept Explain / 概念解释
  - Homework Help / 作业辅导
  - Exam Review / 考前复习
  - Coursework Help / 课程作业辅助
- MathJax 数学公式渲染

## Setup

```bash
python3 -m pip install -r requirements.txt
```

Create a local `.env` file:

```bash
DEEPSEEK_API_KEY=your_api_key_here
```

`.env` is intentionally ignored by Git.

## Run

Terminal mode:

```bash
python3 chat.py
```

Web mode:

```bash
python3 chat.py --web --port 5002
```

Then open:

```text
http://localhost:5002
```

If you want to access it from your phone on the same network, open the LAN address printed by the server, for example:

```text
http://172.20.10.4:5002
```

## Build Knowledge Index

After adding course materials locally:

```bash
python3 scripts/build_index.py
```

Course source PDFs are ignored by Git by default because they may be copyrighted. Generated guides and code can be tracked.
