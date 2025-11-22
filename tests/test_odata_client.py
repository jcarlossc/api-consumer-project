from unittest.mock import patch, MagicMock
from api_consumer_project.strategies.ODataClient import ODataClient
from api_consumer_project.models.ResponseModel import ResponseModel


@patch("api_consumer_project.strategies.ODataClient.requests.get")
def test_odata_client_success(mock_get) -> None:
    # cria resposta falsa
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "value": [{"id": 1, "name": "Product A"}]}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    client = ODataClient("https://example.com/odata")
    result: ResponseModel = client.fetch("Products")

    assert result.success is True
    assert result.status_code == 200
    assert result.data == {"value": [{"id": 1, "name": "Product A"}]}
    assert result.message == "OData OK"

    mock_get.assert_called_once_with(
        "https://example.com/odata/Products", params=None)
