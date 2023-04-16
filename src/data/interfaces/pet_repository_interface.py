# para criar uma interface usa métodos abstratos
from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pets


# classe abstrata -> nunca pode ser instanciada, somente herdada
class PetRepositoryInterface(ABC):
    """Interface pet repository"""

    # método abstrato -> sempre deve ser implementado por quem herda
    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """abstract method"""

        raise Exception("Not implemented")

    @abstractmethod
    def select_pet(
        self, pet_id: int = None, user_id: int = None, name: str = None
    ) -> List[Pets]:
        """abstract method"""

        raise Exception("Not implemented")
