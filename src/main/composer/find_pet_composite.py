from src.data.find_pet import FindPet as FindPetUseCase
from src.infra.repo import PetRepository
from src.presenters.controllers import FindPetController
from src.main.interface import RouteInterface


def find_pet_composer() -> RouteInterface:
    """Composing Find Pet route
    :params - None
    :return - Object with Find Pet route
    """

    # define as rotas que utilizamos nas operações
    # | as implementações

    repository = PetRepository()
    find_pet_use_case = FindPetUseCase(repository)

    find_pet_route = FindPetController(find_pet_use_case)

    return find_pet_route
