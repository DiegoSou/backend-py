# (espião)
# possui a mesma coisa que o repositório e cria uma saída mock

from typing import List
from src.domain.models import Users
from src.domain.test import mock_users


class UserRepositorySpy:
    """Spy to User Repository"""

    def __init__(self):
        self.insert_user_params = {}
        self.delete_user_params = {}
        self.select_user_params = {}

    def insert_user(self, name: str, password: str) -> Users:
        """Spy to all the attributes"""

        self.insert_user_params["name"] = name
        self.insert_user_params["password"] = password

        # retornar um usuário totalmente aleatório
        return mock_users()

    def delete_user(self, user_id: int) -> Users:
        """Spy and return with same id"""

        self.delete_user_params["user_id"] = user_id

        # retornar um usuário totalmente aleatório
        return mock_users(user_id)

    def select_user(self, user_id: str = None, name: str = None) -> List[Users]:
        """Spy to all attributes"""

        self.select_user_params["user_id"] = user_id
        self.select_user_params["name"] = name

        return [mock_users()]
