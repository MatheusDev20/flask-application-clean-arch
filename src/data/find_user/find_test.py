from faker import Faker
from .find import FindUser
from src.infra.test import UserRepositorySpy

faker = Faker()


def test_select_by_id():
    """Test Method"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_user.by_id(user_id=attributes["id"])

    # Testing
    assert response["Success"] is True
    assert user_repo.select_user_params["user_id"] == attributes["id"]


def test_select_by_name():
    """Test Method"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"name": faker.name()}
    response = find_user.by_name(name=attributes["name"])

    # Testing
    assert response["Success"] is True
    assert user_repo.select_user_params["name"] == attributes["name"]


def test_select_by_name_and_id():
    """Test Method"""
    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"name": faker.name(), "id": faker.random_number(digits=2)}
    response = find_user.by_name_and_id(
        name=attributes["name"], user_id=attributes["id"]
    )

    # Testing
    assert response["Success"] is True
    assert user_repo.select_user_params["name"] == attributes["name"]
    assert user_repo.select_user_params["user_id"] == attributes["id"]
