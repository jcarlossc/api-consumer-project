from typing import Any, Optional
import requests
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy
from api_consumer_project.models.ResponseModel import ResponseModel


class ODataClient(ApiClientStrategy):
    """
        Cliente para consumo de APIs no padrão OData.

        Esta classe implementa a interface "ApiClientStrategy" e fornece
        suporte a operações de leitura em serviços compatíveis com o protocolo
        OData, utilizando requisições HTTP GET. O retorno das operações é sempre
        encapsulado em um objeto "ResponseModel", garantindo um padrão único
        de resposta em todo o projeto.

        Attributes:
            base_url (str): URL base do serviço OData, incluindo o endpoint raiz.
    """
    def __init__(self, base_url: str) -> None:
        """
            Inicializa um cliente OData com a URL base informada.

            Args:
                base_url (str):
                    A URL raiz do serviço OData.
        """
        self.base_url = base_url

    def fetch(
        self,
        endpoint: Optional[str] = None,
        params: Optional[dict[str, Any]] = None
    ) -> ResponseModel:
        """
            Executa uma requisição OData utilizando o método HTTP GET.

            A função constrói dinamicamente a URL com base na "base_url" e no
            "endpoint" (se fornecido). Parâmetros adicionais podem ser passados
            em "params" para suportar filtros OData como "$filter", "$select",
            "$orderby", entre outros.

            Args:
                endpoint (str | None):
                    Segmento adicional da URL do recurso OData.  
                    Exemplo: "Products" ou "Products(1)".  
                    Se "None", a requisição é feita diretamente na "base_url".
                
                params (dict[str, Any] | None):
                    Dicionário contendo parâmetros de consulta OData, como
                    "{"$filter": "Price gt 100", "$select": "ID,Name"}".
                    Pode ser "None" caso nenhuma query seja necessária.

            Returns:
                ResponseModel:
                    Objeto padronizado contendo:
                    - "success": indica sucesso ou falha da operação.
                    - "status_code": HTTP status da resposta.
                    - "data": dados retornados no formato JSON quando sucesso.
                    - "message": mensagem de status ou descrição do erro.

            Raises:
                Nenhuma exceção é propagada para fora.  
                Todas as falhas são capturadas e convertidas em um "ResponseModel" 
                com "success=False".
        """
        try:
            url = f"{self.base_url}/{endpoint}" if endpoint else self.base_url
            response = requests.get(url, params=params)
            response.raise_for_status()

            return ResponseModel(
                success=True,
                status_code=response.status_code,
                data=response.json(),
                message="OData OK",
            )
        except requests.RequestException as e:
            return ResponseModel(
                success=False,
                status_code=getattr(e.response, "status_code", 500),
                message=str(e),
            )
