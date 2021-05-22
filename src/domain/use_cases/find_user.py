from abc import ABC, abstractclassmethod
from typing import Dict, List
from src.domain.models import Users


class FindUser(ABC):  # Herdando de ABC
    """Interface do Find User use Case"""

    @abstractclassmethod
    def by_id(cls, user_id: int) -> Dict[bool, List[Users]]:
        """Specific Case"""
        raise Exception("This method should be Implemented: by_id")

    @abstractclassmethod
    def by_name(cls, name: str) -> Dict[bool, List[Users]]:
        """Specific Case"""
        raise Exception("This method should be Implemented: by_name")

    @abstractclassmethod
    def by_name_and_id(cls, name: str, user_id: int) -> Dict[bool, List[Users]]:
        """Specific Case"""
        raise Exception("This method should be Implemented: by_name_and_user_id")


# Classe abstrata serve como base para outras classes herdarem seus métodos.
