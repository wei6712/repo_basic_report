import os
from openai import OpenAI

def call_llm(prompt: str) -> str:
    api_key = os.environ.get("DEEPSEEK_API_KEY")

    if not api_key:
        raise ValueError("未找到环境变量 DEEPSEEK_API_KEY，请先配置 DeepSeek API Key")

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": "你是一名专业的 Python 项目分析助手。"},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    return response.choices[0].message.content