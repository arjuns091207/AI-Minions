
from unittest.mock import Mock, patch

from backend.app.engine.model_client import ModelClient


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
