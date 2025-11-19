import websockets
from typing import Any, Optional
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy
from api_consumer_project.models.ResponseModel import ResponseModel


class WebSocketClient(ApiClientStrategy):
    def __init__(self, url: str) -> None:
        self.url = url

    async def _async_fetch(self, message: str) -> ResponseModel:
        try:
            async with websockets.connect(self.url) as ws:
                await ws.send(message)
                response = await ws.recv()
                return ResponseModel(
                    success=True,
                    status_code=200,
                    data=response,
                    message="WebSocket OK"
                )
        except Exception as e:
            return ResponseModel(
                success=False,
                status_code=500,
                message=str(e))

    def fetch(
        self,
        endpoint: Optional[str] = None,
        params: Optional[dict[str, Any]] = None
    ) -> ResponseModel:
        import asyncio

        msg = params.get("message", "") if params else ""
        return asyncio.run(self._async_fetch(msg))
