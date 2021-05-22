from faker import Faker
from src.infra.test import PetsRepositorySpy
from .find import FindPet

faker = Faker()


def test_select_by_id():
    """Test Method"""
    pet_repo = PetsRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_pet.by_id(pet_id=attributes["id"])

    # Testing
    assert response["Success"] is True
    assert pet_repo.select_pets_params["pet_id"] == attributes["id"]


def test_select_by_user_id():
    """Test Method"""
    pet_repo = PetsRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {"user_id": faker.random_number(digits=5)}
    response = find_pet.by_user_id(user_id=attributes["user_id"])

    assert response["Success"] is True
    assert pet_repo.select_pets_params["user_id"] == attributes["user_id"]


# o que esse assert me garante afinal?
# que meu use case da camada data está implementando corretamente a interface do use do domain
# que o meu repositorio na camada de infra ta implementando minha interface na camada de data.


def test_select_by_user_id_and_pet_id():
    """Test Method"""
    pet_repo = PetsRepositorySpy()
    find_pet = FindPet(pet_repo)

    attributes = {
        "user_id": faker.random_number(digits=5),
        "pet_id": faker.random_number(digits=2),
    }
    response = find_pet.by_pet_id_and_user_id(
        user_id=attributes["user_id"], pet_id=attributes["pet_id"]
    )

    assert response["Success"] is True
    assert pet_repo.select_pets_params["user_id"] == attributes["user_id"]
    assert pet_repo.select_pets_params["pet_id"] == attributes["pet_id"]
