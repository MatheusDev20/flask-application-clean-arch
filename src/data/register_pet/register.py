from typing import Type, Dict, List
from src.domain.models import Pets, Users
from src.domain.use_cases.find_user import FindUser
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.use_cases import RegisterPet as RegisterPetInterface


class RegisterPet(RegisterPetInterface):
    """Use case da camada de Data"""

    def __init__(self, pet_repository: Type[PetRepository], find_user: Type[FindUser]):
        self.pet_repository = pet_repository
        self.find_user = find_user

    def register(
        self, name: str, specie: str, user_info: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """Registry pet
        ::param
            - name: pet name
            - specie: type of the specie
            - age: age of pet
            - user_informatio: user_id or name
        """
        response = None
        # Validating entrys

        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_info(user_info)
        print(user)
        checker = validate_entry and user["Success"]

        if checker:
            response = self.pet_repository.insert_pet(
                name, specie, age, user_info["user_id"]
            )

        return {"Success": checker, "Data": response}

    def __find_user_info(self, user_info: Dict[int, str]) -> Dict[bool, List[Users]]:
        """Check users info and select user"""

        user_founded = None
        user_params = user_info.keys()

        if "user_id" in user_params and "user_name" in user_params:
            print("Aqui ele tá")
            user_founded = self.find_user.by_name_and_id(
                user_info["user_name"], user_info["user_id"]
            )
            print(user_founded)

        elif "user_id" not in user_params and "user_name" in user_params:
            user_founded = self.find_user.by_name(user_info["user_name"])

        elif "user_id" in user_params and "user_name" not in user_params:
            user_founded = self.find_user.by_id(user_info["user_id"])

        else:
            return {"Success": False, "Data": None}

        return user_founded
