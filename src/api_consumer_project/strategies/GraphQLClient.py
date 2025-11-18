import requests
from typing import Optional, Any
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy
from api_consumer_project.models.ResponseModel import ResponseModel


class GraphQLClient(ApiClientStrategy):
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def fetch(
        self,
        endpoint: Optional[str] = None,
        params: Optional[dict[str, Any]] = None
    ) -> ResponseModel:
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
