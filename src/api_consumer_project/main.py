from api_consumer_project.core.ApiClientFactory import ApiClientFactory

def main():
    rest_client = ApiClientFactory.create("rest", "https://servicodados.ibge.gov.br/api/v1/localidades")
    response = rest_client.fetch("estados")

    if response.success:
        print(f"✅ {len(response.data)} informações obtidas com sucesso!")
    else:
        print(f"❌ Erro ({response.status_code}): {response.message}")

    print(response.to_dict()) 
