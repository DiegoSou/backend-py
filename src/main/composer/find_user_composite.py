from src.data.find_user import FindUser as FindUserUseCase
from src.infra.repo import UserRepository
from src.presenters.controllers import FindUserController
from src.main.interface import RouteInterface


def find_user_composer() -> RouteInterface:
    """Composing Find User route
    :params - None
    :return - Object with Find User route
    """

    # define as rotas que utilizamos nas operações
    # | as implementações

    user_repository = UserRepository()
    find_user_use_case = FindUserUseCase(user_repository)

    find_user_route = FindUserController(find_user_use_case)

    return find_user_route
