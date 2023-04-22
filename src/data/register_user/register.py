from typing import Type, Dict
from src.domain.models import Users
from src.domain.use_cases import RegisterUser as RegisterUserInterface
from src.data.interfaces import UserRepositoryInterface


class RegisterUser(RegisterUserInterface):
    """define usercase: Register User"""

    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self.user_repository = user_repository

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """
        Register user use case
        :params - name: person name
                - password: password of the person
        :return - Dictionary with process informations
        """

        response = None

        # validação para proteger a operação (o tratamento da informação é feito uma camada acima do repositório
        # - single responsability
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = self.user_repository.insert_user(name=name, password=password)

        return {"Success": validate_entry, "Data": response}
