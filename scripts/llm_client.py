"""
统一 LLM 客户端 — 提供带重试、流式支持的 LLM 调用

所有脚本通过此模块获取 LLM 客户端，避免重复创建 OpenAI 实例。
"""
import time
import os
import httpx
from openai import OpenAI
from dotenv import load_dotenv

from config import (
    API_KEY, BASE_URL, MODEL_NAME,
)

load_dotenv()

_client = None


def get_client() -> OpenAI:
    """获取单例 OpenAI 客户端实例。"""
    global _client
    if _client is None:
        _client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY", API_KEY),
            base_url=BASE_URL,
        )
    return _client


def _is_retryable(error: Exception) -> bool:
    """判断是否为可重试的错误（网络/超时），不重试认证/参数错误。"""
    if isinstance(error, httpx.NetworkError):
        return True
    if isinstance(error, httpx.TimeoutException):
        return True
    if isinstance(error, httpx.RemoteProtocolError):
        return True
    # API 返回的 429 / 5xx 也重试
    if hasattr(error, 'status_code'):
        code = error.status_code
        return code in (429, 500, 502, 503, 504)
    # 连接错误通常也临时
    msg = str(error).lower()
    if any(kw in msg for kw in ('timeout', 'connection', 'reset', 'refused', 'network')):
        return True
    return False


def call_llm(
    messages: list[dict],
    temperature: float = 0.3,
    max_tokens: int = 2000,
    retries: int = 3,
) -> str:
    """
    调用 LLM，带自动重试。

    Args:
        messages: OpenAI 格式的消息列表 [{"role": "...", "content": "..."}]
        temperature: 生成温度
        max_tokens: 最大输出 token 数
        retries: 最大重试次数（仅网络/超时可重试）

    Returns:
        LLM 生成的文本内容。如果所有重试均失败，返回 "API调用失败: ..." 错误信息。
    """
    client = get_client()
    last_error = None

    for attempt in range(retries + 1):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            content = response.choices[0].message.content
            if content is None:
                raise ValueError("LLM returned empty content (可能被安全过滤截断)")
            return content
        except Exception as e:
            last_error = e
            if attempt < retries and _is_retryable(e):
                wait = 2 ** attempt  # 1s → 2s → 4s
                print(f"  ⚠️ LLM 调用失败 (attempt {attempt + 1}/{retries + 1}): {e}")
                print(f"     等待 {wait}s 后重试...")
                time.sleep(wait)
            else:
                break

    error_msg = f"API调用失败: {last_error}"
    print(f"  ❌ {error_msg}")
    return error_msg


def call_llm_stream(
    messages: list[dict],
    temperature: float = 0.3,
    max_tokens: int = 2000,
):
    """
    流式调用 LLM，逐个 token 产出。

    Args:
        messages: OpenAI 格式的消息列表
        temperature: 生成温度
        max_tokens: 最大输出 token 数

    Yields:
        str: 每个增量文本片段（delta）。
        如果出错，yield 一个错误信息后终止。
    """
    client = get_client()
    try:
        stream = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
        )
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta:
                delta = chunk.choices[0].delta.content
                if delta:
                    yield delta
    except Exception as e:
        yield f"\n\n❌ API调用失败: {e}"


# ================================================================
# 便捷封装：system + user 消息
# ================================================================

def call_llm_with_prompts(
    system_prompt: str,
    user_prompt: str,
    temperature: float = 0.3,
    max_tokens: int = 2000,
    retries: int = 3,
) -> str:
    """单轮对话便捷方法：传入 system 和 user 字符串，返回 LLM 响应文本。"""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    return call_llm(messages, temperature=temperature, max_tokens=max_tokens, retries=retries)


def call_llm_stream_with_prompts(
    system_prompt: str,
    user_prompt: str,
    temperature: float = 0.3,
    max_tokens: int = 2000,
):
    """单轮对话便捷方法（流式版）。"""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    yield from call_llm_stream(messages, temperature=temperature, max_tokens=max_tokens)
