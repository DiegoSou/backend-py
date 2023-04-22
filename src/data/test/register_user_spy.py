from typing import Type, Dict
from src.domain.models import Users
from src.domain.test import mock_users
from src.data.interfaces import UserRepositoryInterface


class RegisterUserSpy:
    """define mock use case: Register User"""

    # use mock instances/implementation
    def __init__(self, user_repository: Type[UserRepositoryInterface]) -> None:
        self.user_repository = user_repository
        self.register_params = {}

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """register use case mock"""

        self.register_params["name"] = name
        self.register_params["password"] = password

        response = None

        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = mock_users()

        return {"Success": validate_entry, "Data": response}
