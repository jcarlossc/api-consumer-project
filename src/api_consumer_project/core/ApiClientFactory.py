from api_consumer_project.strategies.RestClient import RestClient

class ApiClientFactory:
    @staticmethod
    def create(api_type: str, base_url: str):
        match api_type.lower():
            case "rest":
                return RestClient(base_url)
            case _:
                raise ValueError(f"Tipo de API desconhecido: {api_type}")
