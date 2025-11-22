from unittest.mock import AsyncMock, patch

from api_consumer_project.models.ResponseModel import ResponseModel
from api_consumer_project.strategies.WebSocketClient import WebSocketClient


def test_websocket_client_success() -> None:

    async_ws = AsyncMock()
    async_ws.send.return_value = None
    async_ws.recv.return_value = "OK"

    class MockWS:
        async def __aenter__(self):
            return async_ws

        async def __aexit__(self, exc_type, exc, tb):
            pass

    with patch(
        "api_consumer_project.strategies.WebSocketClient.websockets.connect",
        return_value=MockWS(),
    ):
        client = WebSocketClient("ws://localhost")
        response: ResponseModel = client.fetch(params={"message": "hello"})

        assert response.success
        assert response.status_code == 200
        assert response.data == "OK"
