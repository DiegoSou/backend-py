# auxiliador de teste para find pet (service mock)

from typing import Dict, List
from src.domain.models import Pets
from src.domain.test import mock_pets


class FindPetSpy:
    """define mock use case: Select pet"""

    def __init__(self, pet_repository: any):
        self.pet_repository = pet_repository
        self.by_pet_id_params = {}
        self.by_user_id_params = {}
        self.by_name_params = {}
        self.by_user_id_and_name_params = {}

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Find pet by id mock"""

        self.by_pet_id_params["pet_id"] = pet_id

        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = [
                mock_pets(pet_id=pet_id)
            ]  # Não utiliza o repositório para buscar

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Find pet by user id mock"""

        self.by_user_id_params["user_id"] = user_id

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = [mock_pets()]  # Não utiliza o repositório para buscar

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Pets]]:
        """Find pet by name mock"""

        self.by_name_params["name"] = name

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = [mock_pets()]  # Não utiliza o repositório para buscar

        return {"Success": validate_entry, "Data": response}

    def by_user_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Pets]]:
        """Find pet by id mock"""

        self.by_user_id_and_name_params["user_id"] = user_id
        self.by_user_id_and_name_params["name"] = name

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(name, str)

        if validate_entry:
            response = [mock_pets()]  # Não utiliza o repositório para buscar

        return {"Success": validate_entry, "Data": response}
