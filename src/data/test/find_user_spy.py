# auxiliador de teste para find user (service mock)

from typing import Dict, List
from src.domain.models import Users
from src.domain.test import mock_users


class FindUserSpy:
    """define mock use case: Select user"""

    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.by_id_params = {}
        self.by_name_params = {}
        self.by_id_and_name_params = {}

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Find user by id mock"""

        self.by_id_params["user_id"] = user_id

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = [mock_users(user_id)]  # Não utiliza o repositório para buscar

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Find user by name mock"""

        self.by_name_params["user_name"] = name

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = [mock_users()]  # Não utiliza o repositório para buscar

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Find user by id and name mock"""

        self.by_id_and_name_params["user_id"] = user_id
        self.by_id_and_name_params["user_name"] = name

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(name, str)

        if validate_entry:
            response = [mock_users(user_id)]  # Não utiliza o repositório para buscar

        return {"Success": validate_entry, "Data": response}
