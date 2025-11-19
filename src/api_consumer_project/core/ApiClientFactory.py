from api_consumer_project.strategies.RestClient import RestClient
from api_consumer_project.strategies.GraphQLClient import GraphQLClient
from api_consumer_project.strategies.SoapClient import SoapClient
from api_consumer_project.strategies.WebSocketClient import WebSocketClient
from api_consumer_project.strategies.ODataClient import ODataClient


class ApiClientFactory:
    """
        Fábrica responsável por criar instâncias de clientes de API 
        conforme o tipo solicitado.

        Esta classe implementa o padrão Factory Method para encapsular a lógica de criação
        de diferentes tipos de clientes de API (REST, GraphQL, SOAP, WebSocket, OData).
        O objetivo é centralizar a construção desses clientes, evitando que o restante do
        sistema precise conhecer detalhes específicos de cada implementação.
    """
    @staticmethod
    def create(api_type: str, base_url: str):
        """
            Cria e retorna um cliente de API apropriado com base no tipo informado.

            Parameters
            ----------
            api_type : str
                O tipo da API desejada. Valores aceitos incluem:
                "rest", "graphql", "soap", "websocket", "odata".
                A comparação é case-insensitive.
            base_url : str
                URL base da API que será utilizada pelo cliente criado.

            Returns
            -------
            ApiClientStrategy
                Uma instância concreta que implementa a interface "ApiClientStrategy",
                como "RestClient", "GraphQLClient", "SoapClient", "WebSocketClient" ou "ODataClient".

            Raises
            ------
            ValueError
                Se o tipo de API informado não for reconhecido.
        """
        match api_type.lower():
            case "rest":
                return RestClient(base_url)
            case "graphql":
                return GraphQLClient(base_url)
            case "soap":
                return SoapClient(base_url)
            case "websocket":
                return WebSocketClient(base_url)
            case "odata":
                return ODataClient(base_url)
            case _:
                raise ValueError(f"Tipo de API desconhecido: {api_type}")
