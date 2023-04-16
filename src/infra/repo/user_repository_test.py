from faker import Faker
from sqlalchemy import text

from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository

faker = Faker()
user_repository = UserRepository()

db_connection = DBConnectionHandler()


def test_insert_user():
    """Should insert user"""

    name = faker.name()
    password = faker.word()
    engine = db_connection.get_engine()

    # SQL Test Commands
    with engine.connect() as conn:
        new_user = user_repository.insert_user(name, password)
        query_user = conn.execute(
            text(f"SELECT * FROM users WHERE id='{new_user.id}';")
        ).fetchone()

        deleted_user = user_repository.delete_user(new_user.id)

        print(deleted_user)
        assert new_user.id == query_user.id
        assert new_user.name == query_user.name
        assert new_user.password == query_user.password
