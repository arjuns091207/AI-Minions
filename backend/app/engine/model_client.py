
import requests

from backend.app.config.settings import OLLAMA_BASE_URL, OLLAMA_MODEL


class ModelClient:
    def __init__(self):
        self.base_url = OLLAMA_BASE_URL
        self.model = OLLAMA_MODEL

    def generate(self, prompt: str, system_prompt: str = "") -> str:
        url = f"{self.base_url}/api/chat"

        messages = []

        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })

        messages.append({
            "role": "user",
            "content": prompt
        })

        response = requests.post(
            url,
            json={
                "model": self.model,
                "messages": messages,
                "stream": False,
                "think": False,
                "options": {
                    "num_predict": 256
                }
            },
            timeout=(10, 180)
        )

        response.raise_for_status()

        result = response.json()
        return result["message"]["content"]
