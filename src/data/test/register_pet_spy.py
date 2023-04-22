from typing import Type, Dict, List
from src.domain.models import Pets, Users
from src.data.interfaces import PetRepositoryInterface
from src.domain.use_cases import FindUser as FindUserInterface
from src.domain.test import mock_pets


class RegisterPetSpy:
    """define mock use case: Register Pet"""

    # use mock instances/implementations
    def __init__(
        self,
        pet_repository: Type[PetRepositoryInterface],
        find_user: Type[FindUserInterface],
    ):
        self.pet_repository = pet_repository
        self.find_user = find_user
        self.register_params = {}

    def register(
        self, name: str, specie: str, user_information: Dict[str, str], age: int = 0
    ) -> Dict[bool, Pets]:
        """register use case mock"""

        self.register_params["name"] = name
        self.register_params["specie"] = specie
        self.register_params["user_information"] = user_information
        self.register_params["age"] = age

        response = None

        # Valida entradas para register_pet e procura de usuário
        validate_entry = (
            isinstance(name, str) and isinstance(specie, str) and isinstance(age, int)
        )
        pet_owner_information = self.__find_user_information(user_information)
        checker = validate_entry and pet_owner_information["Success"]

        if checker:
            response = mock_pets()

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[str, str]
    ) -> Dict[bool, List[Users]]:
        """find user information mock"""

        user_founded = None
        user_params = user_information.keys()

        if "user_id" in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_id_and_name(
                user_id=int(user_information["user_id"]),
                name=user_information["user_name"],
            )

        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_name(name=user_information["user_name"])

        elif "user_name" not in user_params and "user_id" in user_params:
            user_founded = self.find_user.by_id(
                user_id=int(user_information["user_id"])
            )

        else:
            return {"Success": False, "Data": None}

        return user_founded
