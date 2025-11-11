from api_consumer_project.core.ApiClientFactory import ApiClientFactory

def main():
    rest_client = ApiClientFactory.create("rest", "https://jsonplaceholder.typicode.com")
    response = rest_client.fetch("posts")

    if response.success:
        print(f"✅ {len(response.data)} posts obtidos com sucesso!")
    else:
        print(f"❌ Erro ({response.status_code}): {response.message}")

    print(response.to_dict())  # Para debug/log