from typing import Any, Union
import requests
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy
from api_consumer_project.models.ResponseModel import ResponseModel

class RestClient(ApiClientStrategy):

    JSONType = Union[dict[str, Any], list[Any]]

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def fetch(self, endpoint: str, params: dict[str, Any] | None = None) -> JSONType:
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()
            return ResponseModel(
                success=True,
                status_code=response.status_code,
                data=response.json(),
                message="Requisição REST realizada com sucesso",
                metadata={"endpoint": endpoint, "params": params},
            )
        except requests.RequestException as e:
            return ResponseModel(
                success=False,
                status_code=getattr(e.response, "status_code", 500),
                message=str(e),
                metadata={"endpoint": endpoint, "params": params},
            )    