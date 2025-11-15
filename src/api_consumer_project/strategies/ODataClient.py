from typing import Any, Dict
import requests
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy
from api_consumer_project.models.ResponseModel import ResponseModel

class ODataClient(ApiClientStrategy):
    def __init__(self, base_url: str, default_headers: Dict[str, str] | None = None) -> None:
        self.base_url = base_url.rstrip("/")
        self.headers = default_headers or {"Accept": "application/json"}

    def fetch(self, endpoint: str, params: Dict[str, Any] | None = None) -> ResponseModel:
        try:
            url = f"{self.base_url}/{endpoint.lstrip('/')}" if endpoint else self.base_url
            resp = requests.get(url, headers=self.headers, params=params, timeout=15)
            resp.raise_for_status()

            payload = resp.json()
            data = payload.get("value", payload)

            return ResponseModel(
                success=True,
                status_code=resp.status_code,
                data=data,
                message="Requisição OData realizada com sucesso",
                metadata={"url": resp.url, "raw": payload}
            )
        except requests.RequestException as e:
            status = getattr(e.response, "status_code", 500)
            body = None
            try:
                body = e.response.json()
            except Exception:
                body = getattr(e.response, "text", None)

            return ResponseModel(
                success=False,
                status_code=status,
                data=None,
                message=f"Erro OData: {str(e)}",
                metadata={"url": getattr(e.response, "url", None), "body": body}
            )