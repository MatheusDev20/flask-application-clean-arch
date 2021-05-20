from faker import Faker
from src.infra.test import UserRepositorySpy
from .register import RegisterUser

faker = Faker()


def test_register():
    """Test Registry method"""
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.name(), "password": faker.name()}
    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    # Testing Input

    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    # Testing Output
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Test Registry method"""
    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.random_number(digits=2), "password": faker.name()}
    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    print(response)
    # Testing Input
    assert user_repo.insert_user_params == {}
    # Testing Output
    assert response["Success"] is False
    assert response["Data"] is None
