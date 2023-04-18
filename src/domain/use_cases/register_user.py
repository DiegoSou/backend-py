# pylint: disable=W0719

from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models import Users


class RegisterUser(ABC):
    """Interface to RegisterUser use case"""

    @abstractclassmethod
    def register(cls, name: str, password: str) -> Dict[bool, Users]:
        """use case"""

        raise Exception("Not implemented: register")
