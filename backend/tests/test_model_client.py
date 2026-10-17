import requests
from unittest.mock import Mock, patch

from fastapi.testclient import TestClient

from backend.app.engine.model_client import ModelClient
from backend.app.main import app


@patch("backend.app.engine.model_client.requests.post")
def test_generate_returns_model_response(mock_post):
    mock_response = Mock()
    mock_response.json.return_value = {
        "message": {
            "content": "AI MINIONS ONLINE"
        }
    }
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response

    client = ModelClient()
    result = client.generate("Test prompt")

    assert result == "AI MINIONS ONLINE"
    mock_post.assert_called_once()
    mock_response.raise_for_status.assert_called_once()


def test_health_endpoint():
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "app": "AI Minions",
        "version": "0.1.0",
    }


@patch("backend.app.main.requests.get")
def test_ollama_health_endpoint(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "models": [
            {"name": "qwen3.5:4b"}
        ]
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    client = TestClient(app)
    response = client.get("/health/ollama")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["models_available"] == 1
    mock_get.assert_called_once()

@patch("backend.app.main.requests.get")
def test_ollama_health_endpoint_when_unavailable(mock_get):
    mock_get.side_effect = requests.ConnectionError(
        "Ollama server is unavailable"
    )

    client = TestClient(app)
    response = client.get("/health/ollama")

    assert response.status_code == 200
    assert response.json()["status"] == "unavailable"
    assert response.json()["models_available"] == 0