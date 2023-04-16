from faker import Faker
from sqlalchemy import text
from src.infra.entities import Users as UsersModel

from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository


faker = Faker()
db_connection = DBConnectionHandler()
user_repository = UserRepository()


def test_insert_user():
    """Insert user and assert it"""

    name = faker.name()
    password = faker.word()
    engine = db_connection.get_engine()

    # SQL Test Commands
    with engine.connect() as engine:
        new_user = user_repository.insert_user(name, password)

        query_user = engine.execute(
            text(f"SELECT * FROM users WHERE id='{new_user.id}';")
        ).fetchone()

        user_repository.delete_user(new_user.id)

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password


def test_select_user():
    """Select a user in Users table and compare it"""

    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()

    data = UsersModel(id=user_id, name=name, password=password)
    engine = db_connection.get_engine()

    with engine.connect() as engine:
        engine.execute(
            text(
                f"INSERT INTO users (id, name, password) VALUES ('{user_id}', '{name}', '{password}');"
            )
        )
        engine.commit()

        query_user1 = user_repository.select_user(user_id=user_id)
        query_user2 = user_repository.select_user(name=name)
        query_user3 = user_repository.select_user(user_id=user_id, name=name)

        user_repository.delete_user(user_id=user_id)

    assert data in query_user1
    assert data in query_user2
    assert data in query_user3
