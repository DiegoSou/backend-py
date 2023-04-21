from typing import Type, Dict, List
from src.domain.use_cases import FindPet as FindPetInterface
from src.domain.models import Pets  # For methods return
from src.data.interfaces import PetRepositoryInterface  # For typing


class FindPet(FindPetInterface):
    """Define use case find pet"""

    def __init__(self, pet_repository: Type[PetRepositoryInterface]):
        self.pet_repository = pet_repository

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Select by pet id implementation
        :params - pet_id: the pet id
        :return - Dictionary with the process informations
        """

        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """Select pet by user id implementation
        :params - user_id: pet owner id
        :return - Dictionary with the process informations
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Pets]]:
        """Select by name implementation
        :params - name: the pet name
        :return - Dictionary with the process informations
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.pet_repository.select_pet(name=name)

        return {"Success": validate_entry, "Data": response}

    def by_user_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Pets]]:
        """Select by user id and name implementation
        :params - user_id: the pet owner id
                - name: the pet name
        :return - Dictionary with the process informations
        """

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(name, str)

        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id, name=name)

        return {"Success": validate_entry, "Data": response}
