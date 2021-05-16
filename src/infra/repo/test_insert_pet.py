from faker import Faker
from .pet_repository import PetRepository
from src.infra.config import DBConnectionHandler

faker = Faker()
pet_repository = PetRepository()
db_conn = DBConnectionHandler()


def test_insert_pet():
    """Should insert a new Pet"""
    name = faker.name()
    specie = "dog"
    age = "2"
    user_id = faker.random_number()

    new_pet = pet_repository.insert_pet(name, specie, age, user_id)
    engine = db_conn.get_engine()

    query_pet = engine.execute(
        "SELECT * FROM pets WHERE id='{}';".format(new_pet.id)
    ).fetchone()

    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.specie == query_pet.specie
    assert new_pet.age == query_pet.age
    assert new_pet.user_id == query_pet.user_id

    engine.execute("DELETE FROM pets WHERE id='{}';".format(new_pet.id))
