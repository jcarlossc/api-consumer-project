# src/api_consumer_project/strategies/SoapClient.py
from zeep import Client
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy
from api_consumer_project.models.ResponseModel import ResponseModel

class SoapClient(ApiClientStrategy):
    def __init__(self, wsdl_url: str) -> None:
        self.wsdl_url = wsdl_url
        self.client = Client(wsdl = wsdl_url)

    def fetch(self, endpoint: str, params = None) -> ResponseModel:
        try:
            method = getattr(self.client.service, endpoint)
            result = method(**(params or {}))

            return ResponseModel(
                success=True,
                status_code=200,
                data=result,
                message="Consulta SOAP realizada com sucesso",
                metadata={"endpoint": endpoint, "params": params},
            )

        except Exception as e:
            return ResponseModel(
                success=False,
                status_code=500,
                data=None,
                message=f"Erro ao consumir serviço SOAP: {e}",
                metadata={"endpoint": endpoint, "params": params},
            )
