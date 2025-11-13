from zeep import Client
from api_consumer_project.core.ApiClientStrategy import ApiClientStrategy

class SoapClient(ApiClientStrategy):
    def __init__(self, wsdl_url: str) -> None:
        self.client = Client(wsdl = wsdl_url)

    def fetch(self, endpoint: str, params = None):
        method = getattr(self.client.service, endpoint)
        return method(**(params or {}))