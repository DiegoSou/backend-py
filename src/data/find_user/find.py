from typing import Type, Dict, List
from src.domain.use_cases import FindUser as FindUserInterface
from src.domain.models import Users  # For methods return
from src.data.interfaces import UserRepositoryInterface  # For typing


class FindUser(FindUserInterface):
    """Define use case find user"""

    def __init__(self, user_repository: Type[UserRepositoryInterface]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select by id implementation
        :params - user_id: user id
        :return - Dictionary with the process informations
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select by name implementation
        :params - name: user's name
        :return - Dictionary with the process informations
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(name=name)

        return {"Success": validate_entry, "Data": response}

    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Select by id and name implementation
        :params - user_id: user's id
                - name: user's name
        :return - Dictionary with the process informations
        """

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(name, str)

        if validate_entry:
            response = self.user_repository.select_user(user_id=user_id, name=name)

        return {"Success": validate_entry, "Data": response}
