import asyncio
import websockets
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
                    message="Mensagem enviada e resposta recebida com sucesso via WebSocket",
                    data=response,
                    metadata={"sent": message}
                )
        except Exception as e:
            return ResponseModel(
                success=False,
                status_code=500,
                message=f"Erro na comunicação WebSocket: {str(e)}",
                data=None,
                metadata={"sent": message}
            )

    def fetch(self, endpoint: str = None, params=None) -> ResponseModel:
        message = params.get("message") if params else ""

        return asyncio.run(self._async_fetch(message))


