import requests
from typing import Optional, Any
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy
from api_consumer_project.models.ResponseModel import ResponseModel


class GraphQLClient(ApiClientStrategy):
    """
        Cliente responsável por consumir APIs GraphQL utilizando requisições HTTP POST.

        Esta classe implementa a estratégia "ApiClientStrategy" para chamadas GraphQL,
        enviando consultas ("query") ou mutações para o endpoint configurado. A resposta
        é padronizada no formato "ResponseModel", garantindo consistência em todo o sistema.

        Parameters
        ----------
        base_url : str
            URL do endpoint GraphQL que será consumido.
    """
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def fetch(
        self,
        endpoint: Optional[str] = None,
        params: Optional[dict[str, Any]] = None
    ) -> ResponseModel:
        """
            Executa uma requisição GraphQL enviando a consulta fornecida em "params".

            Esta implementação exige que o parâmetro "params" contenha a chave "query",
            que deve conter uma string representando a consulta GraphQL. Caso a consulta
            não seja fornecida, o método retorna um "ResponseModel" indicando erro
            (status 400).

            Parameters
            ----------
            endpoint : str, optional
                Ignorado nesta implementação, pois APIs GraphQL utilizam um único endpoint.
                Mantido apenas por compatibilidade com a interface "ApiClientStrategy".
            params : dict[str, Any], optional
                Dicionário contendo pelo menos a chave "query", representando a consulta
                GraphQL a ser enviada no corpo da requisição.

            Returns
            -------
            ResponseModel
                Objeto contendo o resultado da operação, incluindo:
                - "success": sucesso ou falha
                - "status_code": status HTTP retornado
                - "data": corpo JSON da resposta, quando disponível
                - "message": descrição da operação
                - "metadata": inclui a própria consulta enviada

            Raises
            ------
            Nenhuma exceção é propagada. Qualquer erro interno ou HTTP é capturado e
            transformado em um "ResponseModel" padronizado.
        """
        try:
            if not params or "query" not in params:
                return ResponseModel(
                    success=False,
                    status_code=400,
                    message="Missing GraphQL query"
                )
            query = params["query"]
            response = requests.post(self.base_url, json={"query": query})
            response.raise_for_status()
            return ResponseModel(
                success=True,
                status_code=response.status_code,
                data=response.json(),
                message="GraphQL OK",
                metadata={"query": query},
            )
        except requests.RequestException as e:
            return ResponseModel(
                success=False,
                status_code=getattr(e.response, "status_code", 500),
                message=str(e),
            )
