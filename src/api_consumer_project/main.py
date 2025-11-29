import os
import json
from typing import Callable, Dict, Optional
from api_consumer_project.core.ApiClientFactory import ApiClientFactory


# -------------------
# Funções auxiliares
# -------------------
def clean_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def show_menu(title: str, options: Dict[str, str]) -> None:
    line = "-" * (len(title) + 6)
    print(f"\n{line}\n {title} \n{line}")
    for key, label in options.items():
        print(f"[{key}] - {label}")
    print(line)


def ask_option(prompt: str) -> str:
    return input(f"{prompt}: ").strip()


def wait() -> None:
    clean_screen()
    print("POR FAVOR, AGUARDE...\n")


# ------------------------------
# Lógica REST
# ------------------------------
MENU_REST_MAP = {"1": "estados", "2": "regioes", "3": "paises"}


def handle_rest() -> None:
    while True:
        show_menu(
            "TIPO DE INFORMAÇÃO (REST)",
            {"1": "ESTADOS", "2": "REGIÕES", "3": "PAÍSES", "4": "VOLTAR"},
        )
        option = ask_option("🔍 ESCOLHA O TIPO DE INFORMAÇÃO")

        if not option.isdigit() or option >= "5":
            clean_screen()
            print("❌ OPÇÃO INVÁLIDA!")
            continue

        elif option == "4":
            clean_screen()
            return

        api_name = MENU_REST_MAP.get(option)
        if not api_name:
            clean_screen()
            print("❌ OPÇÃO INVÁLIDA!")

        wait()

        client = ApiClientFactory.create(
            "rest", "https://servicodados.ibge.gov.br/api/v1/localidades/"
        )

        response = client.fetch(api_name)

        print("=" * 60)
        print(f"Sucesso: {response.success}")
        print(f"Status: {response.status_code}")
        print(f"Mensagem: {response.message}")
        print(f"Dados:\n{response.to_dict()}")
        print("=" * 60)


# ------------------------------
# Lógica GraphQL
# ------------------------------
GRAPHQL_QUERIES = {
    "1": """
        { countries { code name } }
    """,
    "2": """
        { continents { code name } }
    """,
    "3": """
        { languages { name rtl } }
    """,
}


def handle_graphql() -> None:
    while True:
        show_menu(
            "TIPO DE INFORMAÇÃO (GRAPHQL)",
            {
                "1": "PAISES",
                "2": "CONTINENTES",
                "3": "LINGUAGENS",
                "4": "VOLTAR"
            },
        )
        option = ask_option("🔍 ESCOLHA O TIPO DE INFORMAÇÃO")

        if not option.isdigit():
            clean_screen()
            print("❌ OPÇÃO INVÁLIDA!")
            continue

        elif option == "4":
            clean_screen()
            return

        query = GRAPHQL_QUERIES.get(option)
        if not query:
            clean_screen()
            print("❌ OPÇÃO INVÁLIDA!")
            continue

        wait()

        client = ApiClientFactory.create(
            "graphql", "https://countries.trevorblades.com/"
        )
        response = client.fetch(endpoint="", params={"query": query})

        print("=" * 60)
        print(json.dumps(response.to_dict(), indent=2, ensure_ascii=False))
        print("=" * 60)


# ------------------------------
# Lógica SOAP
# ------------------------------
SOAP_OPERATIONS = {
    "1": ("Add", "SOMA"),
    "2": ("Subtract", "SUBTRAÇÃO"),
    "3": ("Multiply", "MULTIPLICAÇÃO"),
    "4": ("Divide", "DIVISÃO"),
}


def get_two_numbers() -> Optional[Dict[str, str]]:
    n1 = input("\nDIGITE O PRIMEIRO NÚMERO: ")
    n2 = input("DIGITE O SEGUNDO NÚMERO: ")

    if n1.isdigit() and n2.isdigit():
        return {"intA": n1, "intB": n2}

    clean_screen()
    print("❌ ENTRADA INVÁLIDA. DIGITE SOMENTE NÚMEROS INTEIROS.")
    return None


def handle_soap() -> None:
    while True:
        show_menu(
            "TIPO DE CÁLCULO (SOAP)",
            {
                "1": "SOMA",
                "2": "SUBTRAÇÃO",
                "3": "MULTIPLICAÇÃO",
                "4": "DIVISÃO",
                "5": "VOLTAR",
            },
        )
        option = ask_option("🔍 ESCOLHA O TIPO DE CÁLCULO")

        if not option.isdigit():
            clean_screen()
            print("❌ OPÇÃO INVÁLIDA!")
            continue

        elif option == "5":
            clean_screen()
            return

        operation = SOAP_OPERATIONS.get(option)
        if not operation:
            clean_screen()
            print("❌ OPÇÃO INVÁLIDA!")
            continue

        params = get_two_numbers()
        if not params:
            continue

        endpoint, label = operation
        wait()

        client = ApiClientFactory.create(
            "soap", "http://www.dneonline.com/calculator.asmx?wsdl"
        )
        response = client.fetch(endpoint, params)

        print("=" * 60)
        print(f"RESULTADO ({label}): {response.data}")
        print("=" * 60)


# ------------------------------
# Lógica WebSocket
# ------------------------------
def handle_websocket() -> None:
    clean_screen()
    print(f'{"-" * 15}\n WEB SOCKET\n{"-" * 15}')
    text = input("\nDIGITE UMA FRASE: ")

    wait()

    client = ApiClientFactory.create(
        "websocket", "wss://ws.postman-echo.com/raw"
    )
    response = client.fetch(params={"message": text})

    print("=" * 60)
    print(json.dumps(response.to_dict(), indent=2, ensure_ascii=False))
    print("=" * 60)


# ------------------------------
# Lógica ODATA
# ------------------------------
ODATA_TYPES = {
    "1": ("People", {"$top": 2}),
    "2": ("Airlines", {"$top": 2}),
    "3": ("Airports", {"$top": 2}),
}


def handle_odata() -> None:
    while True:
        show_menu(
            "TIPO DE INFORMAÇÃO (ODATA)",
            {
                "1": "PESSOAS",
                "2": "COMPANHIAS AÉREAS",
                "3": "AEROPORTOS",
                "4": "VOLTAR",
            },
        )
        option = ask_option("🔍 ESCOLHA O TIPO DE INFORMAÇÃO")

        if not option.isdigit():
            clean_screen()
            print("❌ OPÇÃO INVÁLIDA!")
            continue

        if option == "4":
            clean_screen()
            return

        config = ODATA_TYPES.get(option)
        if not config:
            clean_screen()
            print("❌ OPÇÃO INVÁLIDA!")
            continue

        entity, params = config
        wait()

        client = ApiClientFactory.create(
            "odata", "https://services.odata.org/V4/TripPinServiceRW/"
        )
        response = client.fetch(entity, params=params)

        print("=" * 60)
        print(json.dumps(response.data, indent=2, ensure_ascii=False))
        print("=" * 60)


# ------------------------------
# Main Loop
# ------------------------------
def main() -> None:
    clean_screen()

    ACTIONS: Dict[str, Callable[[], None]] = {
        "1": handle_rest,
        "2": handle_graphql,
        "3": handle_soap,
        "4": handle_websocket,
        "5": handle_odata,
    }

    while True:
        show_menu(
            "PROJETO APIs",
            {
                "1": "REST API",
                "2": "GRAPHQL API",
                "3": "SOAP API",
                "4": "WEB SOCKET API",
                "5": "ODATA API",
                "6": "SAIR",
            },
        )

        option = ask_option("🔍 ESCOLHA O TIPO DE API")

        if option == "6":
            clean_screen()
            print("SAINDO... ATÉ A PRÓXIMA!")
            break

        action = ACTIONS.get(option)
        if action:
            clean_screen()
            action()
        else:
            clean_screen()
            print("❌ OPÇÃO INVÁLIDA!")


if __name__ == "__main__":
    main()
