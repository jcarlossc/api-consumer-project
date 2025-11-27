import os
from api_consumer_project.core.ApiClientFactory import ApiClientFactory


def main():

    # Método para limpar tela.
    def clean_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    # Menu principal.
    def menu_main():
        print(f"\n {20 * '-'} PROJETO APIs {20 * '-'}")
        print('[1] - REST API')
        print('[2] - GRAPHQL API')
        print('[3] - SOAP API')
        print('[4] - WEB SOCKET API')
        print('[5] - ODATA API')
        print('[6] - SAIR')
        print(f"{55 * '-'}")    

    # Menu Rest.
    def menu_rest():
        print(f"\n {17 * '-'} TIPO DE INFORMAÇÃO {17 * '-'}")
        print('[1] - ESTADOS')
        print('[2] - REGIÕES')
        print('[3] - PAÍSES')
        print('[4] - VOLTAR')
        print(f"{55 * '-'}")    

    # Menu GraphQL.
    def menu_graphql():
        print(f"\n {17 * '-'} TIPO DE INFORMAÇÃO {17 * '-'}")
        print('[1] - PAISES')
        print('[2] - CONTINENTES')
        print('[3] - LINGUAGENS')
        print('[4] - VOLTAR')
        print(f"{55 * '-'}")    

    # Menu Soap.
    def menu_soap():
        print(f"\n {17 * '-'} TIPO DE CÁLCULO {17 * '-'}")
        print('[1] - SOMA')
        print('[2] - SUBTRAÇÃO')
        print('[3] - MULTIPLICAÇÃO')
        print('[4] - DIVISÃO')
        print('[5] - VOLTAR')
        print(f"{55 * '-'}")    

    # Chama método para limpar tela.
    clean_screen()  

    # While principal.
    while True:
        # Menu principal.
        menu_main()
        api_type = input(f"🔍 ESCOLHA O TIPO DE API: ")

        # Condicional Rest.
        if api_type == '1':
            clean_screen()
            api_type_rest_name = ''

            # While Rest.
            while True:
                menu_rest()
                api_type_rest = input(f"🔍 ESCOLHA O TIPO DE INFORMAÇÃO: ")

                if api_type_rest == '1':
                    api_type_rest_name = 'estados'

                elif api_type_rest == '2':
                    api_type_rest_name = 'regioes'
        
                elif api_type_rest == '3':
                    api_type_rest_name = 'paises'

                elif api_type_rest == '4':
                    clean_screen()
                    break

                else:
                    clean_screen()
                    print('❌ OPÇÃO INVÁLIDA!')  
                    break  

                clean_screen()
                print("POR FAVOR, AGUARDE...")
                # =====================================================================
                # REST
                base = "https://servicodados.ibge.gov.br/api/v1/localidades/"
                rest_client = ApiClientFactory.create("rest", base)
                response = rest_client.fetch(api_type_rest_name)

                if response.success:
                    print(f"{len(response.data)} informações obtidas com sucesso!")
                else:
                    print(f"Erro ({response.status_code}): {response.message}")

                print("=" * 60)
                print(response.to_dict())
                print("=" * 60)
                # =====================================================================

        # Condicional GraphQL.
        elif api_type == '2':
            clean_screen()

            # While GraphQL.
            while True:
                menu_graphql()
                api_type_graphql = input(f"🔍 ESCOLHA O TIPO DE INFORMAÇÃO: ")

                if api_type_graphql == '1':
                    query = """
                    {
                    countries {
                        code
                        name
                        }
                    }
                    """

                elif api_type_graphql == '2':
                    query = """
                    {
                    continents {
                        code
                        name
                        }
                    }
                    """
        
                elif api_type_graphql == '3':
                    query = """
                    {
                    languages {
                        name
                        rtl
                        }
                    }
                    """

                elif api_type_graphql == '4':
                    clean_screen()
                    break

                else:
                    clean_screen()
                    print('❌ OPÇÃO INVÁLIDA!')  
                    break 

                clean_screen()
                print("POR FAVOR, AGUARDE...")    
                # =====================================================================
                # GRAPHQL

                base = "https://countries.trevorblades.com/"
                graphql_client = ApiClientFactory.create("graphql", base)

                response = graphql_client.fetch(endpoint="", params={"query": query})
                print("=" * 60)
                print(f"Sucesso: {response.success}")
                print(f"Status: {response.status_code}")
                print(f"Mensagem: {response.message}")
                print(f"Dados:")
                print(response.data)
                print("=" * 60)
                # =====================================================================

        # Condicional Soap.
        elif api_type == '3':
            clean_screen()

            # While Soap.
            while True:
                menu_soap()
                api_type_soap = input(f"🔍 ESCOLHA O TIPO DE INFORMAÇÃO: ")

                if api_type_soap == '1':
                    number_01 = input(f"\nDIGITE O PRIMEIRO NÚMERO: ")
                    number_02 = input(f"DIGITE O SEGUNDO NÚMERO: ")

                    if number_01.isdigit() and number_02.isdigit():
                        endpoint = "Add"
                        params = {"intA": number_01, "intB": number_02}

                    else:
                        clean_screen()
                        print('❌ INTRADA INVÁLIDA. POR FAVOR, DIGITE SOMENTE NÚMEROS INTEIROS')  
                        break 

                elif api_type_soap == '2':
                    number_01 = input(f"\nDIGITE O PRIMEIRO NÚMERO: ")
                    number_02 = input(f"DIGITE O SEGUNDO NÚMERO: ")

                    if number_01.isdigit() and number_02.isdigit():
                        endpoint = "Subtract"
                        params = {"intA": number_01, "intB": number_02}

                    else:
                        clean_screen()
                        print('❌ INTRADA INVÁLIDA. POR FAVOR, DIGITE SOMENTE NÚMEROS INTEIROS')  
                        break 
        
                elif api_type_soap == '3':
                    number_01 = input(f"\nDIGITE O PRIMEIRO NÚMERO: ")
                    number_02 = input(f"DIGITE O SEGUNDO NÚMERO: ")

                    if number_01.isdigit() and number_02.isdigit():
                        endpoint = "Multiply"
                        params = {"intA": number_01, "intB": number_02}

                    else:
                        clean_screen()
                        print('❌ INTRADA INVÁLIDA. POR FAVOR, DIGITE SOMENTE NÚMEROS INTEIROS')  
                        break 

                elif api_type_soap == '4':
                    number_01 = input(f"\nDIGITE O PRIMEIRO NÚMERO: ")
                    number_02 = input(f"DIGITE O SEGUNDO NÚMERO: ")

                    if number_01.isdigit() and number_02.isdigit():
                        endpoint = "Divide"
                        params = {"intA": number_01, "intB": number_02}

                    else:
                        clean_screen()
                        print('❌ INTRADA INVÁLIDA. POR FAVOR, DIGITE SOMENTE NÚMEROS INTEIROS')  
                        break 

                elif api_type_soap == '5':
                    clean_screen()
                    break

                else:
                    clean_screen()
                    print('❌ OPÇÃO INVÁLIDA!')  
                    break  

                clean_screen()
                print("POR FAVOR, AGUARDE...")
                # =====================================================================
                # SOAP

                base = "http://www.dneonline.com/calculator.asmx?wsdl"
                soap_client = ApiClientFactory.create("soap", base)

                response = soap_client.fetch(endpoint, params)

                print("=" * 60)
                print(f"Sucesso: {response.success}")
                print(f"Status: {response.status_code}")
                print(f"Mensagem: {response.message}")
                print(f"Dados:")
                print(f"RESULTADO DO CÁLCULO: {response.data}")
                print("=" * 60)
                # =====================================================================

        elif api_type == '4':
            pass
        elif api_type == '5': 
            pass
        elif api_type == '6':
            clean_screen()
            print("SAIR, ATÉ A PRÓXIMA!")
            exit()
        else:
            clean_screen()
            print("❌ OPÇÃO INVÁLIDA!")


    """
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

    """

    """
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

    """


if __name__ == "__main__":
    main()
