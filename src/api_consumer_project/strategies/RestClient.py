from typing import Any, Union
import requests
from api_consumer_project.core.APIClientStrategy import APIClientStrategy

class RestClient(APIClientStrategy):

    JSONType = Union[dict[str, Any], list[Any]]

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def fetch(self, endpoint: str, params: dict[str, Any] | None = None) -> JSONType:
        response = requests.get(f'{self.base_url}/{endpoint}', params = params)
        response.raise_for_status()
        return response.json()     