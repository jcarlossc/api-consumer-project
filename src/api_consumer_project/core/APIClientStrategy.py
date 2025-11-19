from abc import abstractmethod
from typing import Any, Optional, Protocol
from api_consumer_project.models.ResponseModel import ResponseModel


class ApiClientStrategy(Protocol):
    """
    Interface para estratégias de clientes de API dentro do sistema.

    Esta classe utiliza o padrão Strategy para permitir que diferentes
    clientes (por exemplo, requisições HTTP, leitura de arquivos
    locais, mocks para testes, consumidores de APIs específicas, etc.)
    possam ser utilizados de forma intercambiável, desde que implementem
    o método 'fetch'.

    Qualquer classe concreta que implemente esta estratégia deve
    fornecer uma implementação do método 'fetch', garantindo que o
    retorno seja um objeto do tipo 'ResponseModel'.
    """

    @abstractmethod
    def fetch(
        self,
        endpoint: Optional[str] = None,
        params: Optional[dict[str, Any]] = None
    ) -> ResponseModel:
        """
        Executa uma operação de busca (fetch) em uma API, retornando
        um objeto "ResponseModel" contendo os dados estruturados da
        resposta.

        Parameters
        ----------
        endpoint : str, optional
            Caminho ou recurso específico da API a ser consultado.
            Caso não seja fornecido, a implementação pode assumir um
            endpoint padrão.
        params : dict[str, Any], optional
            Parâmetros adicionais enviados na requisição, como filtros,
            paginação ou autenticação.

        Returns
        -------
        ResponseModel
            Objeto contendo a resposta tratada.

        Raises
        ------
        ValueError
            Caso o endpoint seja inválido ou não possa ser processado.
        ConnectionError
            Caso haja falha de comunicação com a API.
        RuntimeError
            Para outros erros inesperados durante a execução da estratégia.
        """
        pass
