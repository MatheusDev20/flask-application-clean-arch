from typing import Dict, List, Type
from src.domain.models.pets import Pets
from src.domain.use_cases import FindPet as FindPetInterface
from src.data.interfaces import PetRepositoryInterface


class FindPet(FindPetInterface):
    """Use case for Find pet"""

    def __init__(self, pets_repository: Type[PetRepositoryInterface]):
        self.pets_repository = pets_repository

    def by_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Method By id"""
        response = None
        validate = isinstance(pet_id, int)

        if validate:
            response = self.pets_repository.select_pet(pet_id=pet_id)

        return {"Success": validate, "Data": response}

    def by_user_id(self, user_id: str) -> Dict[bool, List[Pets]]:
        """Get pet by name"""
        response = None
        validate = isinstance(user_id, int)

        if validate:
            response = self.pets_repository.select_pet(user_id=user_id)

        return {"Success": validate, "Data": response}

    def by_pet_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        """Get pet by name"""
        response = None
        validate = isinstance(user_id, int) and isinstance(pet_id, int)

        if validate:
            response = self.pets_repository.select_pet(user_id=user_id, pet_id=pet_id)

        return {"Success": validate, "Data": response}
