from faker import Faker
from src.infra.test import PetsRepositorySpy, UserRepositorySpy
from src.data.test import FindUserSpy
from .register import RegisterPet


faker = Faker()


def test_registry():
    """Testing register pet funcionality"""
    pet_repo = PetsRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_user)

    attributes = {
        "name": faker.name(),
        "specie": faker.name(),
        "age": faker.random_number(digits=1),
        "user_info": {
            "user_name": faker.name(),
            "user_id": faker.random_number(digits=5),
        },
    }
    response = register_pet.register(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_info=attributes["user_info"],
    )
    # Testing Inputs
    assert pet_repo.insert_pets_params["name"] == attributes["name"]
    assert pet_repo.insert_pets_params["specie"] == attributes["specie"]
    assert pet_repo.insert_pets_params["age"] == attributes["age"]

    print(response)
