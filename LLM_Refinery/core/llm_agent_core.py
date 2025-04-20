# LLM_Refinery/core/llm_agent_core.py

import os
import requests

BRANIAC_API = os.getenv("BRANIAC_API", "http://localhost:8000/generate")
BRANIAC_TOKEN = os.getenv("BRANIAC_TOKEN", "mistral-peter")

def call_llm(prompt: str, system_prompt: str = "You are a helpful assistant.") -> str:
    headers = {
        "Authorization": f"Bearer {BRANIAC_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral-7b",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }

    try:
        response = requests.post(BRANIAC_API, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"⚠️ LLM Core Error: {e}")
        return "[ERROR] Could not reach Braniac"
