from abc import ABC, abstractclassmethod
from typing import Dict, List
from src.domain.models import Users


class FindUser(ABC):
    """Interface to Find Pet user case"""

    @abstractclassmethod
    def by_id(cls, user_id: int) -> Dict[bool, List[Users]]:
        """use case"""

        raise Exception("Not implemented: by_id")

    @abstractclassmethod
    def by_name(cls, name: str) -> Dict[bool, List[Users]]:
        """use case"""

        raise Exception("Not implemented: by_name")

    @abstractclassmethod
    def by_id_and_name(cls, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """use case"""

        raise Exception("Not implemented: by_id_and_name")
