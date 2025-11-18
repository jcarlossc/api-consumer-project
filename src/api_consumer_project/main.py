from api_consumer_project.core.ApiClientFactory import ApiClientFactory


def main():
    # =====================================================================
    # REST

    base = "https://servicodados.ibge.gov.br/api/v1/localidades"
    rest_client = ApiClientFactory.create("rest", base)
    response = rest_client.fetch("estados")

    if response.success:
        print(f"{len(response.data)} informações obtidas com sucesso!")
    else:
        print(f"Erro ({response.status_code}): {response.message}")

    print("=" * 60)
    print(response.to_dict())
    print("=" * 60)
    # =====================================================================

    '''
    # =====================================================================
    # GRAPHQL

    base = "https://countries.trevorblades.com/"
    graphql_client = ApiClientFactory.create("graphql", base)
    query = """
    {
    countries {
        code
        name
        capital
        }
    }
    """
    response = graphql_client.fetch(endpoint="", params={"query": query})
    print("=" * 60)
    print(f"Sucesso: {response.success}")
    print(f"Status: {response.status_code}")
    print(f"Mensagem: {response.message}")
    print(f"Dados:")
    print(response.data)
    print("=" * 60)
    # =====================================================================

    '''

    '''
    # =====================================================================
    # SOAP

    base = "http://www.dneonline.com/calculator.asmx?wsdl"
    soap_client = ApiClientFactory.create("soap", base)

    endpoint = "Add"

    params = {"intA": 15, "intB": 5}

    response = soap_client.fetch(endpoint, params)

    print("=" * 60)
    print(f"Sucesso: {response.success}")
    print(f"Status: {response.status_code}")
    print(f"Mensagem: {response.message}")
    print(f"Dados:")
    print(response.data)
    print("=" * 60)
    # =====================================================================
    '''

    '''
    # =====================================================================
    # WEBSOCKET

    web_socket_client = ApiClientFactory.create(
        "websocket",
        "wss://ws.postman-echo.com/raw"
    )

    params = {"message": "Olá, Carlos da Costa!"}

    response = web_socket_client.fetch(params=params)

    print("=" * 60)
    print(f"Sucesso: {response.success}")
    print(f"Status: {response.status_code}")
    print(f"Mensagem: {response.message}")
    print(f"Dados recebidos: {response.data}")
    print("=" * 60)
    # =====================================================================

    '''

    '''
    # =====================================================================
    # ODATA

    base = "https://services.odata.org/V4/TripPinServiceRW"
    client = ApiClientFactory.create("odata", base)

    response = client.fetch("People", params={"$top": 5})

    print("=" * 60)
    print(f"Sucesso: {response.success}")
    print(f"Status: {response.status_code}")
    print(f"Mensagem: {response.message}")
    print(f"Dados:")
    print(json.dumps(response.data, indent=2, ensure_ascii=False))
    print("=" * 60)
    # =====================================================================

    '''


if __name__ == "__main__":
    main()
