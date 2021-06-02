from faker import Faker
from src.presenters.helpers import HttpRequest
from src.data.test import RegisterPetSpy
from src.infra.test import PetsRepositorySpy, UserRepositorySpy
from .register_pet_controller import RegisterPetController

faker = Faker()


def test_route():
    """Testing route for register Pet"""

    register_pet_use_case = RegisterPetSpy(PetsRepositorySpy, UserRepositorySpy)

    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.word(),
        "specie": "dog",
        "age": faker.random_number(),
        "user_info": {"user_id": faker.random_number(), "user_name": faker.word()},
    }

    response = register_pet_route.route(HttpRequest(body=attributes))

    # Testing Input
    assert register_pet_use_case.registry_param["name"] == attributes["name"]
    assert register_pet_use_case.registry_param["specie"] == attributes["specie"]
    assert register_pet_use_case.registry_param["age"] == attributes["age"]
    assert register_pet_use_case.registry_param["user_info"] == attributes["user_info"]

    assert response.status_code == 200
    assert "error" not in response.body
