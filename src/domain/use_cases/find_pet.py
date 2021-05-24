from abc import ABC, abstractclassmethod
from typing import Dict, List
from src.domain.models import Pets


class FindPet(ABC):
    """Use case Interface for FindPet"""

    @abstractclassmethod
    def by_id(cls, pet_id: int) -> Dict[bool, List[Pets]]:
        """user case method interface for id"""

        raise Exception("This method should be implmenthed")

    @abstractclassmethod
    def by_user_id(cls, user_id: int) -> Dict[bool, List[Pets]]:
        """Specific case"""
        raise Exception("This method should be implementhed")

    @abstractclassmethod
    def by_pet_id_and_user_id(cls, pet_id: int, user_id: int) -> Dict[bool, List[Pets]]:
        """Specific case"""
        raise Exception("This method should be implemenhted")
