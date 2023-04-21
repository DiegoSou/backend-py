# (espião)
# possui a mesma coisa que o repositório, criando saída mock

from typing import List
from src.domain.models import Pets
from src.domain.test import mock_pets


class PetRepositorySpy:
    """Spy to pet repository"""

    def __init__(self):
        self.insert_pet_params = {}
        self.select_pet_params = {}

    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """Spy to all attributes"""

        self.insert_pet_params["name"] = name
        self.insert_pet_params["specie"] = specie
        self.insert_pet_params["age"] = age
        self.insert_pet_params["user_id"] = user_id

        # retornar um usuário totalmente aleatório
        return mock_pets()

    def select_pet(
        self, pet_id: int = None, user_id: int = None, name: str = None
    ) -> List[Pets]:
        """Spy to all attributes"""

        self.select_pet_params["pet_id"] = pet_id
        self.select_pet_params["user_id"] = user_id
        self.select_pet_params["name"] = name

        return [mock_pets(pet_id=pet_id)]
