# para criar uma interface usa métodos abstratos
from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Users


# classe abstrata -> nunca pode ser instanciada, somente herdada
class UserRepositoryInterface(ABC):
    """Interface pet repository"""

    # método abstrato -> sempre deve ser implementado por quem herda
    @abstractmethod
    def insert_user(self, name: str, password: str) -> Users:
        """abstract method"""

        raise Exception("Not implemented")

    @abstractmethod
    def delete_user(self, user_id: int = None) -> Users:
        """abstract method"""

        raise Exception("Not implemented")

    @abstractmethod
    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:
        """abstract method"""

        raise Exception("Not implemented")
