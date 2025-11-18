from abc import abstractmethod
from typing import Any, Optional, Protocol
from api_consumer_project.models.ResponseModel import ResponseModel


class ApiClientStrategy(Protocol):
    @abstractmethod
    def fetch(
        self,
        endpoint: Optional[str] = None,
        params: Optional[dict[str, Any]] = None
    ) -> ResponseModel:
        pass
