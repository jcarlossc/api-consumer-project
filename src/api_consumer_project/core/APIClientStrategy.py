from abs import ABC, abstractmethod
from typing import Any, Dict

class APIClientStrategy(ABC):
    @abstractmethod
    def fetch(self, endpoint: str, params: Dict[str, Any] = None) -> Any:
        pass

