# src/api_consumer_project/strategies/SoapClient.py
from typing import Optional, Any
from zeep import Client
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy
from api_consumer_project.models.ResponseModel import ResponseModel

class SoapClient(ApiClientStrategy):
    def __init__(self, wsdl_url: str) -> None:
        self.client = Client(wsdl=wsdl_url)

    def fetch(
        self,
        endpoint: Optional[str] = None,
        params: Optional[dict[str, Any]] = None
    ) -> ResponseModel:

        try:
            if endpoint is None:
                return ResponseModel(
                    success=False,
                    status_code=400,
                    message="SOAP endpoint cannot be None"
                )
            method = getattr(self.client.service, endpoint)
            result = method(**(params or {}))

            return ResponseModel(
                success=True,
                status_code=200,
                data=result,
                message="SOAP OK"
            )
        except Exception as e:
            return ResponseModel(
                success=False,
                status_code=500,
                message=str(e)
            )

