import requests
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy
from api_consumer_project.models.ResponseModel import ResponseModel

class GraphQLClient(ApiClientStrategy):
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def fetch(self, endpoint: str, params = None) -> ResponseModel: 
        try:
            query = params.get("query")
            response = requests.post(self.base_url, json = {"query": query})
            response.raise_for_status()
            return ResponseModel(
                success = True,
                status_code = response.status_code,
                data = response.json(),
                message = "Consulta GraphQL realizada com sucesso",
                metadata = {"endpoint": endpoint, "query": query},
            )  
        except requests.RequestException as e:
            return ResponseModel(
                success = False,
                status_code = getattr(e.response, "status_code", 500),
                message = str(e),
                metadata = {"endpoint": endpoint, "query": params.get("query")},
            )     