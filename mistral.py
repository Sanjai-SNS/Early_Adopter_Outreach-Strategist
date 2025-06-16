# 📁 early_user_outreach_app/mistral.py

import requests
import json

def generate_with_context(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"
    response = requests.post(url, json={"model": "mistral", "prompt": prompt}, stream=True)
    
    collected = ""
    for chunk in response.iter_lines():
        if chunk:
            try:
                data = json.loads(chunk.decode("utf-8"))
                if "response" in data:
                    collected += data["response"]
            except Exception as e:
                continue

    return collected.strip().replace("\n\n", "\n")
