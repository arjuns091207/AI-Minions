
import requests
from fastapi import FastAPI

from backend.app.config.settings import (
    APP_NAME,
    APP_VERSION,
    OLLAMA_BASE_URL,
)

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="A local-first multi-agent AI workforce."
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "app": APP_NAME,
        "version": APP_VERSION
    }


@app.get("/health/ollama")
def ollama_health_check():
    try:
        response = requests.get(
            f"{OLLAMA_BASE_URL}/api/tags",
            timeout=5
        )
        response.raise_for_status()

        return {
            "status": "healthy",
            "ollama_url": OLLAMA_BASE_URL,
            "models_available": len(
                response.json().get("models", [])
            )
        }

    except requests.RequestException:
        return {
            "status": "unavailable",
            "ollama_url": OLLAMA_BASE_URL,
            "models_available": 0
        }
