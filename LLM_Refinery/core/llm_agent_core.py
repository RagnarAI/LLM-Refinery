import os
import requests

BRANIAC_API = os.getenv("BRANIAC_API", "http://localhost:8000/generate")
BRANIAC_TOKEN = os.getenv("BRANIAC_TOKEN", "46897e73-ae97-4c20-8b23-305bb0504bc6")

def call_llm(prompt: str, system_prompt: str = "You are a helpful assistant.") -> str:
    headers = {
        "Authorization": BRANIAC_TOKEN,  # ✅ Braniac expects raw token (not "Bearer ...")
        "Content-Type": "application/json"
    }

    data = {
        "prompt": f"{system_prompt}\n{prompt}"
    }

    try:
        response = requests.post(BRANIAC_API, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        return response.json().get("response", "[NO OUTPUT]")
    except requests.exceptions.HTTPError as http_err:
        try:
            error_detail = response.json().get("detail", str(http_err))
        except:
            error_detail = str(http_err)
        print(f"⚠️ LLM HTTP Error: {error_detail}")
        return "[ERROR] Could not reach Braniac"
    except Exception as e:
        print(f"⚠️ LLM Core Error: {e}")
        return "[ERROR] Could not reach Braniac"
