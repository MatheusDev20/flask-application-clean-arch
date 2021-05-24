from typing import Dict, List
from src.domain.models import Users
from src.domain.test import mock_users


class FindUserSpy:
    """Class to define use case select user"""

    def __init__(self, user_repository: any):
        self.user_repository = user_repository
        self.id_param = {}
        self.by_id_param = {}
        self.by_name_param = {}
        self.by_id_and_name_param = {}

    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select User by id"""
        self.by_id_param["user_id"] = user_id
        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = [mock_users()]

        return {"Sucess": validate_entry, "Data": response}

    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """Select User by id"""
        self.by_id_param["name"] = name
        response = None
        validate_entry = isinstance(name, int)

        if validate_entry:
            response = [mock_users()]

        return {"Sucess": validate_entry, "Data": response}

    def by_name_and_id(self, name: str, user_id: int) -> Dict[bool, List[Users]]:
        """Select User By Name and user_id"""
        self.by_id_and_name_param["user_id"] = user_id
        self.by_id_and_name_param["name"] = name
        response = None
        print(type(name))
        print(name)
        print(user_id)
        print(type(user_id))
        validate = isinstance(name, str) and isinstance(user_id, int)

        if validate:
            print("Validou o user")
            response = [mock_users()]

        return {"Success": validate, "Data": response}
