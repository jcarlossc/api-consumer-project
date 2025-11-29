# src/api_consumer_project/strategies/SoapClient.py
from typing import Optional, Any
from zeep import Client
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy
from api_consumer_project.models.ResponseModel import ResponseModel


class SoapClient(ApiClientStrategy):
    """
    Cliente para consumo de serviços SOAP utilizando WSDL.

    Esta classe implementa a interface ``ApiClientStrategy`` e fornece
    uma implementação concreta para chamadas a métodos expostos via SOAP.
    Todas as respostas são encapsuladas em um ``ResponseModel`` para manter
    consistência com os demais clientes (REST, GraphQL, WebSocket, OData).

    Attributes:
        client (zeep.Client):
            Instância do cliente SOAP carregada a partir de um WSDL.
    """

    def __init__(self, wsdl_url: str) -> None:
        """
        Inicializa o cliente SOAP carregando o WSDL especificado.

        Args:
            wsdl_url (str):
                URL do arquivo WSDL que descreve o serviço SOAP.
        """
        self.client = Client(wsdl=wsdl_url)

    def fetch(
        self,
        endpoint: Optional[str] = None,
        params: Optional[dict[str, Any]] = None
    ) -> ResponseModel:
        """
        Executa uma chamada SOAP invocando o método definido por "endpoint".

        Args:
            endpoint (str | None):
                Nome do método SOAP a ser chamado.
                Exemplo: "Add" ou "Multiply".
                Se None, a operação é abortada e uma resposta de
                erro é retornada.

            params (dict[str, Any] | None):
                Parâmetros necessários pelo método SOAP.
                Exemplo: "{"intA": 10, "intB": 5}".
                Pode ser "None" caso o método não exija argumentos.

        Returns:
            ResponseModel:
                Contém:
                - "success": indica se a chamada foi bem-sucedida.
                - "status_code": valor HTTP simbólico (200 para sucesso,
                400/500 para falhas).
                - "data": resultado retornado pelo método SOAP.
                - "message": mensagem indicando sucesso ou erro.

        Notes:
            - SOAP não utiliza códigos HTTP reais em cada operação.
            Portanto, retornamos "200" para sucesso e "500" para exceções.
            - A biblioteca "zeep" lança exceções específicas, tratadas
            genericamente para garantir uniformidade no padrão Strategy.

        Raises:
            Nenhuma exceção é propagada ao chamador.
            Em caso de falha, um "ResponseModel" com "success=False"
            é retornado.
        """
        try:
            if endpoint is None:
                return ResponseModel(
                    success=False,
                    status_code=400,
                    message="SOAP endpoint cannot be None",
                )
            method = getattr(self.client.service, endpoint)
            result = method(**(params or {}))

            return ResponseModel(
                success=True,
                status_code=200,
                data=result,
                message="SOAP OK"
            )
        except Exception as e:
            return ResponseModel(
                success=False,
                status_code=500,
                message=str(e)
            )
