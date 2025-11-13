from api_consumer_project.strategies.RestClient import RestClient
from api_consumer_project.strategies.GraphQLClient import GraphQLClient
from api_consumer_project.strategies.SoapClient import SoapClient

class ApiClientFactory:
    @staticmethod
    def create(api_type: str, base_url: str):
        match api_type.lower():
            case "rest":
                return RestClient(base_url)
            case "graphql":
                return GraphQLClient(base_url)
            case "soap":
                return SoapClient(base_url)
            case _:
                raise ValueError(f"Tipo de API desconhecido: {api_type}")
