from src.main.interface import RouteInterface
from src.data.register_user import RegisterUser
from src.presenters.controllers import RegisterUserController
from src.infra.repo import UserRepository


def register_user_composer() -> RouteInterface:
    """Composing Register User route
    :param - None
    :return - Object with Register User Route
    """

    # define as rotas que utilizamos nas operações
    # | as implementações

    repository = UserRepository()
    use_case = RegisterUser(repository)
    register_user_route = RegisterUserController(use_case)

    return register_user_route
