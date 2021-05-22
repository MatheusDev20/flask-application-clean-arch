from src.domain.models.pets import Pets
from typing import List
from src.domain.test import mock_pets


class PetsRepositorySpy:
    """Repositorio para testes ( Elimina a necessidade de escrever no banco
    para testar os use cases"""

    def __init__(self):
        self.insert_pets_params = {}
        self.select_pets_params = {}

    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """Spy Attributtes"""
        self.insert_pets_params["name"] = name
        self.insert_pets_params["specie"] = specie
        self.insert_pets_params["age"] = age
        self.insert_pets_params["user_id"] = user_id

        return mock_pets()

    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """Spy to all the attributes"""
        self.select_pets_params["pet_id"] = pet_id
        self.select_pets_params["user_id"] = user_id

        return [mock_pets()]
