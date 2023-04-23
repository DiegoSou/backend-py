from typing import Type, Dict, List
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pets, Users
from src.domain.use_cases import FindUser as FindUserInterface
from src.domain.use_cases import RegisterPet as RegisterPetInterface


class RegisterPet(RegisterPetInterface):
    """define use case: Register Pet"""

    def __init__(
        self,
        pet_repository: Type[PetRepositoryInterface],
        find_user: Type[FindUserInterface],
    ):
        self.pet_repository = pet_repository
        self.find_user = find_user

    def register(
        self, name: str, specie: str, user_information: Dict[str, str], age: int = 0
    ) -> Dict[bool, Pets]:
        """
        Register pet use case
        :params - name: pet name
                - specie: pet specie type
                - age: pet age
                - user_information: Dictionary with user id and/or user name (pet owner)
        :return - Dictionary with process informations
        """

        response = None

        # validação das entradas para proteger a operação
        # | o tratamento da informação é feito uma camada acima do repositório
        # - single responsability
        validade_entry = (
            isinstance(name, str) and isinstance(specie, str) and isinstance(age, int)
        )
        pet_owner_information = self.__find_user_information(user_information)

        checker = validade_entry and pet_owner_information["Success"]

        if checker:
            response = self.pet_repository.insert_pet(
                name=name,
                specie=specie,
                age=age,
                user_id=int(pet_owner_information["Data"][0].id),
            )

        return {"Success": checker, "Data": response}

    def __find_user_information(
        self, user_information: Dict[str, str]
    ) -> Dict[bool, List[Users]]:
        """
        Check user infos and select user
        :params - user_information: Dictionary with user_id and/or user_name
        :return - Dictionary with the find_user use case response
        """

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
