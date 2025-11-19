from dataclasses import dataclass, field
from typing import Any, Optional, Dict
import datetime


@dataclass
class ResponseModel:
    """
        Modelo de resposta padronizado utilizado pelas estratégias de clientes de API.

        Esta classe representa uma estrutura consistente para respostas vindas de diferentes
        implementações de clientes (REST, GraphQL, SOAP, WebSocket, etc). Seu objetivo é
        garantir uniformidade no formato de retorno, independentemente da fonte dos dados.

        Atributos
        ---------
        success : bool
            Indica se a operação foi concluída com sucesso.
        status_code : int
            Código de status associado à resposta (HTTP ou equivalente).
        data : Any, optional
            Conteúdo retornado pela operação. Pode ser qualquer tipo de dado.
        message : str, optional
            Mensagem de contexto, como erro, aviso ou descrição adicional.
        metadata : dict[str, Any]
            Metadados adicionais fornecidos pela implementação concreta. Usado para
            informações auxiliares, como paginação ou cabeçalhos.
        timestamp : str
            Data e hora em formato ISO 8601 (UTC). Gerado automaticamente no momento
            da criação do objeto.
    """
    success: bool
    status_code: int
    data: Optional[Any] = None
    message: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(
        default_factory=lambda: datetime.datetime.utcnow().isoformat()
    )

    def to_dict(self) -> Dict[str, Any]:
        """
            Converte o modelo de resposta em um dicionário padrão.

            Returns
            -------
            dict[str, Any]
                Representação do objeto contendo todos os campos serializáveis.

            Examples
            --------
            {
                "success": True,
                "status_code": 200,
                "data": {"id": 1},
                "message": None,
                "metadata": {},
                "timestamp": "2025-11-18T12:34:56.789012"
            }
        """
        return {
            "success": self.success,
            "status_code": self.status_code,
            "data": self.data,
            "message": self.message,
            "metadata": self.metadata,
            "timestamp": self.timestamp,
        }
