from sqlalchemy import text
from faker import Faker
from src.infra.config import DBConnectionHandler
from .pet_repository import PetRepository

faker = Faker()
pet_repository = PetRepository()
db_connection = DBConnectionHandler()

def test_insert_pet():
    """ Insert pet in Pet repository """

    name = faker.name()
    specie = "FISH" # mock 'fish' once it is enum type
    age = faker.random_number(digits=1)
    user_id = faker.random_number(digits=1)

    engine = db_connection.get_engine()

    # SQL Commands
    with engine.connect() as engine:
        new_pet = pet_repository.insert_pet(name=name, specie=specie, age=age, user_id=user_id)

        query_pet = engine.execute(
            text(f"SELECT * FROM pets WHERE id='{new_pet.id}';")
        ).fetchone()

        engine.execute(
            text(f"DELETE FROM pets WHERE id='{new_pet.id}';")
        )
        engine.commit()

    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.specie == str(query_pet.specie).lower()
    assert new_pet.age == query_pet.age
    assert new_pet.user_id == query_pet.user_id
