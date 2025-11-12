from api_consumer_project.core.ApiClientFactory import ApiClientFactory
from api_consumer_project.strategies.GraphQLClient import GraphQLClient


def main():

    '''
    rest_client = ApiClientFactory.create("rest", "https://servicodados.ibge.gov.br/api/v1/localidades")
    response = rest_client.fetch("estados")

    if response.success:
        print(f"✅ {len(response.data)} informações obtidas com sucesso!")
    else:
        print(f"❌ Erro ({response.status_code}): {response.message}")

    print("=" * 60)    
    print(response.to_dict()) 
    print("=" * 60)
    '''

    '''
    base_url = "https://countries.trevorblades.com/"

    client = GraphQLClient(base_url)

    query = """
    {
    countries {
        code
        name
        capital
        }
    }
    """

    response = client.fetch(endpoint="", params={"query": query})

    print("=" * 60)
    print(f"✅ Sucesso: {response.success}")
    print(f"🌐 Status: {response.status_code}")
    print(f"📄 Mensagem: {response.message}")
    print(f"📊 Dados:")
    print(response.data)
    print("=" * 60) 
    '''



if __name__ == "__main__":
    main()