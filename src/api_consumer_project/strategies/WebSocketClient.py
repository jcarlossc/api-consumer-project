import websockets
from typing import Any, Optional
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy
from api_consumer_project.models.ResponseModel import ResponseModel


class WebSocketClient(ApiClientStrategy):
    """
    Cliente para comunicação com servidores WebSocket.

    Esta classe implementa a interface ``ApiClientStrategy`` e fornece suporte
    a chamadas assíncronas utilizando o protocolo WebSocket. A comunicação é
    realizada por meio do envio de uma mensagem e recebimento de uma resposta,
    encapsulando tudo no modelo de resposta unificado ``ResponseModel``.

    Attributes:
        url (str):
            URL completa do servidor WebSocket.
    """

    def __init__(self, url: str) -> None:
        """
        Inicializa o cliente WebSocket com a URL fornecida.

        Args:
            url (str):
                Endpoint WebSocket que será utilizado para enviar e
                receber mensagens.
                Pode ser ``ws://`` ou ``wss://``.
        """
        self.url = url

    async def _async_fetch(self, message: str) -> ResponseModel:
        """
        Executa a operação assíncrona de envio e recebimento de
        dados no WebSocket.

        Args:
            message (str):
                Mensagem a ser enviada ao servidor WebSocket.
                Exemplo: "Hello WebSocket!".
                Caso vazio, o servidor retornará a resposta
                padrão (se suportado).

        Returns:
            ResponseModel:
                Objeto contendo:
                - "success": indica se a transação ocorreu sem erros.
                - "status_code": sempre "200" para sucesso, "500" para falha.
                - "data": mensagem recebida do servidor WebSocket.
                - "message": mensagem descritiva ("WebSocket OK" ou erro).

        Notes:
            - O método utiliza "websockets.connect" para estabelecer a conexão.
            - Erros de rede, timeouts ou falhas no handshake são capturados
            e convertidos em um "ResponseModel" padronizado.
        """
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
                message=str(e)
            )

    def fetch(
        self,
        endpoint: Optional[str] = None,
        params: Optional[dict[str, Any]] = None
    ) -> ResponseModel:
        import asyncio

        msg = params.get("message", "") if params else ""
        return asyncio.run(self._async_fetch(msg))
