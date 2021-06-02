from src.presenters.helpers.http_models import HttpRequest
from faker import Faker
from src.infra.test.users_repository_spy import UserRepositorySpy
from .register_user_controller import RegisterUserController
from src.data.test.register_user_spy import RegisterUserSpy

faker = Faker()


def test_register_user():
    """Test register User"""
    register_user = RegisterUserSpy(UserRepositorySpy)
    register_user_controller = RegisterUserController(register_user)
    attributes = {"name": faker.word(), "password": faker.word()}
    response = register_user_controller.handle(HttpRequest(body=attributes))

    assert register_user.registry_params["name"] == attributes["name"]
    assert register_user.registry_params["password"] == attributes["password"]

    assert "error" not in response.body
    assert response.status_code == 200
