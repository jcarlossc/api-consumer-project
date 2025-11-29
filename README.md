# 📌 API Consumer Project

### Um projeto modular em Python para consumo de APIs com Strategy + Factory + Tipagem + Testes

Este projeto demonstra uma arquitetura profissional para consumo de diferentes tipos de APIs usando Python, seguindo princípios de SOLID, Clean Code, e Padrões de Projeto.

---

## 📌 O sistema permite consumir APIs:

- REST
- GraphQL
- SOAP
- WebSocket
- OData

---

## 📌 Tudo isso usando:

- ApiClientStrategy (Strategy Pattern)
- ApiClientFactory (Factory Method)
- ResponseModel (DTO padronizado)
- Testes com pytest e mocks
- Tipagem estática com mypy
- Estilo consistente com black + isort + flake8
- Estrutura de projeto moderna com Poetry

---

## 📌 Estrutura do Projeto
```
api_consumer_project/
│
├── src/
│   └── api_consumer_project/
│       ├── strategies/
│       │   ├── RestClient.py
│       │   ├── GraphQLClient.py
│       │   ├── SoapClient.py
│       │   ├── WebSocketClient.py
│       │   └── ODataClient.py
│       │
│       ├── core/
│       │   ├── ApiClientStrategy.py
│       │   └── ApiClientFactory.py
|       |
|       ├── models/
│       │    └── ResponseModel.py
|       |
│       └── __init__.py
├── tests/
│   ├── test_rest_client.py
│   ├── test_graphql_client.py
│   ├── test_odata_client.py
│   ├── test_soap_client.py
│   ├── test_websocket_client.py
│   ├── test_api_client_factory.py
│   └── test_response_model.py
│
├── poetry.lock
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## 📌 Padrões de Projetos

### 1. Strategy Pattern

Cada tipo de API implementa a interface ApiClientStrategy, garantindo:

- Mesma assinatura
- Comportamento polimórfico
- Facilidade de extensão

### 2. Factory Method

A classe ApiClientFactory gera dinamicamente:
```
client = ApiClientFactory.create("rest", "https://api.com")
```

### 3. DTO padronizado

ResponseModel garante que todos os clientes retornem:

```
{
  "success": true,
  "status_code": 200,
  "data": {...},
  "message": "OK",
  "metadata": {},
  "timestamp": "2025-11-20T12:30:00"
}
```
---

## 📌 Instalação

### 1. Clonar o repositório
```
git clone https://github.com/jcarlossc/api-consumer-project.git
cd api_consumer_project
```

### 2. Instalar dependências com Poetry
```
poetry install
```

### 2. Executar o projeto
```
poetry run api
```

---

## 📌 Interface CLI

### Menu principal
```
------------------
 PROJETO APIs
------------------
[1] - REST API
[2] - GRAPHQL API
[3] - SOAP API
[4] - WEB SOCKET API
[5] - ODATA API
[6] - SAIR
------------------
🔍 ESCOLHA O TIPO DE API:
```
### Menu Rest
```
-------------------------------
 TIPO DE INFORMAÇÃO (REST)
-------------------------------
[1] - ESTADOS
[2] - REGIÕES
[3] - PAÍSES
[4] - VOLTAR
-------------------------------
🔍 ESCOLHA O TIPO DE INFORMAÇÃO:
```
### Menu GraphQL
```
----------------------------------
 TIPO DE INFORMAÇÃO (GRAPHQL)
----------------------------------
[1] - PAISES
[2] - CONTINENTES
[3] - LINGUAGENS
[4] - VOLTAR
----------------------------------
🔍 ESCOLHA O TIPO DE INFORMAÇÃO:
```
### Menu Soap
```
----------------------------
 TIPO DE CÁLCULO (SOAP)
----------------------------
[1] - SOMA
[2] - SUBTRAÇÃO
[3] - MULTIPLICAÇÃO
[4] - DIVISÃO
[5] - VOLTAR
----------------------------
🔍 ESCOLHA O TIPO DE CÁLCULO:
```
### Menu Web Socket
```
---------------
 WEB SOCKET
---------------
DIGITE UMA FRASE:
```
### Menu OData
```
--------------------------------
 TIPO DE INFORMAÇÃO (ODATA)
--------------------------------
[1] - PESSOAS
[2] - COMPANHIAS AÉREAS
[3] - AEROPORTOS
[4] - VOLTAR
--------------------------------
🔍 ESCOLHA O TIPO DE INFORMAÇÃO:
```
---
## 📌 Testes

### 1. Testes (pytest)
```
poetry run pytest -v
```
### 2. Tipagem Estática (mypy)
```
poetry run mypy .
```
### 3. Checagens do flake8
```
poetry run flake8 .
```
---

## 📌 Tecnologias utilizadas

| Tecnologia |	Uso |
| ---------- | ---- |
| Python 3.12	| Linguagem principal |
| Requests	| Consumo de APIs REST/OData/GraphQL |
| Zeep |	Cliente SOAP |
| websockets |	Consumo WebSocket |
| Poetry |	Gerenciamento de dependências |
| pytest + mocks |	Testes automatizados |
| mypy |	Tipagem estática |
| flake8 |	Padronização de código |

---

## 📌 Objetivos do Projeto

* Demonstrar arquitetura escalável com Strategy
* Criar clientes plugáveis para múltiplos tipos de API
* Aplicar padrões profissionais de desenvolvimento
* Mostrar domínio de testes, tipagem e boas práticas
* Fornecer um projeto sólido para portfólio

---

## 📌 Licença

MIT — você pode usar e modificar livremente.

---

## 📌 Autor

📌Autor: Carlos da Costa<br>
📌Recife, PE - Brasil<br>
📌Telefone: +55 81 99712 9140<br>
📌Telegram: @jcarlossc<br>
📌Pypi: https://pypi.org/user/jcarlossc/<br>
📌Blogger linguagem R: https://informaticus77-r.blogspot.com/<br>
📌Blogger linguagem Python: https://informaticus77-python.blogspot.com/<br>
📌Email: jcarlossc1977@gmail.com<br>
📌LinkedIn: https://www.linkedin.com/in/carlos-da-costa-669252149/<br>
📌GitHub: https://github.com/jcarlossc<br>
📌Kaggle: https://www.kaggle.com/jcarlossc/<br>
📌Twitter/X: https://x.com/jcarlossc1977<br>

----

