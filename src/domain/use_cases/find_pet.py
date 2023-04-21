from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Pets


class FindPet(ABC):
    """Interface to Find Pet use case"""

    @abstractmethod
    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """use case"""

        raise Exception("Not implemented: by_pet_id")

    @abstractmethod
    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """use case"""

        raise Exception("Not implemented: by_user_id")

    @abstractmethod
    def by_name(self, name: str) -> Dict[bool, List[Pets]]:
        """use case"""

        raise Exception("Not implemented: by_name")

    @abstractmethod
    def by_user_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Pets]]:
        """use case"""

        raise Exception("Not implemented: by_user_id_and_name")
