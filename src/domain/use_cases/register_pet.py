from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Pets


class RegisterPet(ABC):
    """Interface to RegisterPet use case"""

    @abstractmethod
    def register(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = 0
    ) -> Dict[bool, Pets]:
        """use case"""

        raise Exception("Not implemented: register")
