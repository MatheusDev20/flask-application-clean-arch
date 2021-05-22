from src.domain.models.users import Users
from typing import Dict, List, Type
from src.domain.use_cases import FindUser as FindUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository


class FindUser(FindUserInterface):
    """Class to define use cases Find user"""

    def __init__(self, user_repository: Type[UserRepository]):
        self.user_repository = user_repository

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select User By id
        :param user_id: id of the user
        :response Dict with the informations and response"""
        response = None
        validate = isinstance(user_id, int)

        if validate:
            response = self.user_repository.select_user(user_id=user_id)

        return {"Success": validate, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select User By Name
        :param name: Name of the user
        :response Dict with the informations and response"""
        response = None
        validate = isinstance(name, str)

        if validate:
            response = self.user_repository.select_user(name=name)

        return {"Success": validate, "Data": response}

    def by_name_and_id(self, name: str, user_id: int) -> Dict[bool, List[Users]]:
        """Select User By Name and user
        :param user_id: id of the user
        :param name: Name of the user
        :response Dict with the informations and response"""
        response = None
        validate = isinstance(name, str) and isinstance(user_id, int)

        if validate:
            response = self.user_repository.select_user(name=name, user_id=user_id)

        return {"Success": validate, "Data": response}
