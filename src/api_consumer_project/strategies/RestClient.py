from typing import Any, Optional
import requests
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy
from api_consumer_project.models.ResponseModel import ResponseModel

class RestClient(ApiClientStrategy):
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def fetch(
        self,
        endpoint: Optional[str] = None,
        params: Optional[dict[str, Any]] = None
    ) -> ResponseModel:
        try:
            url = f"{self.base_url}/{endpoint}" if endpoint else self.base_url
            response = requests.get(url, params=params)
            response.raise_for_status()
            return ResponseModel(
                success=True,
                status_code=response.status_code,
                data=response.json(),
                message="OK"
            )
        except requests.RequestException as e:
            return ResponseModel(
                success=False,
                status_code=getattr(e.response, "status_code", 500),
                message=str(e)
            )
  