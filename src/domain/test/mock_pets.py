from faker import Faker
from src.domain.models import Pets

faker = Faker()


def mock_pets() -> Pets:
    """Mock Pets"""
    return Pets(
        id=faker.random_number(digits=5),
        name=faker.name(),
        age=faker.random_number(digits=1),
        specie="dog",
        user_id=faker.random_number(digits=5),
    )
