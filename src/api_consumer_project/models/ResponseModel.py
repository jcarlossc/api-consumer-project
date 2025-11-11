from dataclasses import dataclass, field
from typing import Any, Optional, Dict
import datetime

@dataclass
class ResponseModel:
    success: bool
    status_code: int
    data: Optional[Any] = None
    message: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory = dict)
    timestamp: str = field(default_factory=lambda: datetime.datetime.utcnow().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "status_code": self.status_code,
            "data": self.data,
            "message": self.message,
            "metadata": self.metadata,
            "timestamp": self.timestamp,
        }