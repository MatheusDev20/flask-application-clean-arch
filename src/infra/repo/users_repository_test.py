from faker import Faker
from src.infra.config import DBConnectionHandler
from .users_repository import UsersRepository


faker = Faker()
user_repository = UsersRepository()
db_conn = DBConnectionHandler()


def test_insert_user():
    """Should insert User"""
    name = faker.name()
    password = faker.word()
    engine = db_conn.get_engine()

    new_user = user_repository.insert_user(name, password)
    query_user = engine.execute(
        "SELECT * FROM users WHERE id='{}';".format(new_user.id)
    ).fetchone()
    engine.execute("DELETE FROM users WHERE id='{}';".format(new_user.id))

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password
