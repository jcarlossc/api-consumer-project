import pytest
from unittest.mock import patch, MagicMock

from api_consumer_project.strategies.RestClient import RestClient
from api_consumer_project.models.ResponseModel import ResponseModel
import requests


def test_rest_client_success():
    """Testa uma requisição REST que retorna sucesso."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "ok"}
    mock_response.raise_for_status.return_value = None

    with patch("api_consumer_project.strategies.RestClient.requests.get", return_value=mock_response):
        client = RestClient("https://api.test")
        response = client.fetch("users")

        assert isinstance(response, ResponseModel)
        assert response.success is True
        assert response.status_code == 200
        assert response.data == {"message": "ok"}
        assert response.message == "OK"