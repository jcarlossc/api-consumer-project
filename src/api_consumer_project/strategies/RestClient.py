from typing import Any, Optional
import requests
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy
from api_consumer_project.models.ResponseModel import ResponseModel


class RestClient(ApiClientStrategy):
    """
    Cliente para consumo de APIs RESTful utilizando requisições HTTP GET.

    Esta classe implementa a interface ``ApiClientStrategy`` e fornece
    uma implementação concreta para requisições REST. O retorno das operações
    é sempre encapsulado em um objeto ``ResponseModel``, garantindo um padrão
    uniforme de resposta em todo o projeto.

    Attributes:
        base_url (str): URL base da API REST, normalmente representando
        o endpoint raiz.
    """

    def __init__(self, base_url: str) -> None:
        """
        Inicializa o cliente REST com a URL base fornecida.

        Args:
            base_url (str):
                A URL raiz do serviço REST.
        """
        self.base_url = base_url

    def fetch(
        self,
        endpoint: Optional[str] = None,
        params: Optional[dict[str, Any]] = None
    ) -> ResponseModel:
        """
        Executa uma requisição REST utilizando o método HTTP GET.

        A requisição é construída dinamicamente com base na "base_url" e no
        "endpoint" (caso informado). Parâmetros adicionais podem ser enviados
        em "params" como parte da string de query.

        Args:
            endpoint (str | None):
                Caminho adicional da URL a ser anexado à "base_url".
                Exemplo: "users" ou "posts/10".
                Se "None", a requisição é feita diretamente na "base_url".

            params (dict[str, Any] | None):
                Parâmetros de consulta a serem enviados via URL.
                Exemplo: "{"page": 2, "limit": 50}".
                Pode ser "None" caso não haja parâmetros.

        Returns:
            ResponseModel:
                Objeto contendo:
                - "success": indica sucesso ou falha.
                - "status_code": código HTTP retornado.
                - "data": corpo JSON retornado pela API (em caso de sucesso).
                - "message": mensagem indicando resultado ou erro ocorrido.

        Raises:
            Nenhuma exceção é propagada.
            Todas as falhas de rede ou HTTP são interceptadas e convertidas
            em um "ResponseModel" com "success=False".
        """
        try:
            url = f"{self.base_url}/{endpoint}" if endpoint else self.base_url
            response = requests.get(url, params=params)
            response.raise_for_status()
            return ResponseModel(
                success=True,
                status_code=response.status_code,
                data=response.json(),
                message="OK",
            )
        except requests.RequestException as e:
            return ResponseModel(
                success=False,
                status_code=getattr(e.response, "status_code", 500),
                message=str(e),
            )
