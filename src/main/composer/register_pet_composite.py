from src.data.find_user import FindUser
from src.data.register_pet import RegisterPet as RegisterPetUseCase
from src.infra.repo import PetRepository
from src.infra.repo import UserRepository
from src.presenters.controllers import RegisterPetController
from src.main.interface import RouteInterface


def register_pet_composer() -> RouteInterface:
    """Composing Regiter Pet route
    :params - None
    :return - Object with Register Pet route
    """

    # define as rotas que utilizamos nas operações
    # | as implementações

    repository = PetRepository()
    find_user_use_case = FindUser(UserRepository())

    register_pet_use_case = RegisterPetUseCase(
        pet_repository=repository, find_user=find_user_use_case
    )

    register_pet_route = RegisterPetController(register_pet_use_case)

    return register_pet_route
