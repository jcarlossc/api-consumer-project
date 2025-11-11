from app.strategies.rest_client import RestClient

class APIClientFactory:
    @staticmethod
    def create(api_type: str, base_url: str):
        match api_type.lower():
            case "rest":
                return RestClient(base_url)
            case _:
                raise ValueError(f"Tipo de API desconhecido: {api_type}")
