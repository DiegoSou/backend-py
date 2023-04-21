from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Users


class RegisterUser(ABC):
    """Interface to RegisterUser use case"""

    @abstractmethod
    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """use case"""

        raise Exception("Not implemented: register")
