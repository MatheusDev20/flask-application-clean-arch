# INTERFACE DO MEU USE CASE
from abc import ABC, abstractclassmethod
from typing import Dict
from src.domain.models.pets import Pets


class RegisterPet(ABC):
    """Interface Class to be implmented in Data folder use_case"""

    @abstractclassmethod
    def register(
        cls, name: str, specie: str, user_info: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Método interface para use case de registrar PET"""

        raise Exception("This method should be implemented")
