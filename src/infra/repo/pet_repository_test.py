from sqlalchemy import text
from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel
from src.infra.entities.pets import AnimalTypes
from .pet_repository import PetRepository

faker = Faker()
pet_repository = PetRepository()
db_connection = DBConnectionHandler()

def test_insert_pet():
    """ Insert pet in Pet repository """

    name = faker.name()
    specie = "FISH" # mock 'fish' once it is enum type
    age = faker.random_number(digits=1)
    user_id = faker.random_number(digits=4)

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

def test_select_pet():
    """ Select a pet in Pets table and compare it """

    pet_id = faker.random_number(digits=4)
    name = faker.name()
    specie = "FISH" # mock 'fish' once it is enum type
    age = faker.random_number(digits=1)
    user_id = faker.random_number(digits=4)

    specie_mock = AnimalTypes("fish")
    data = PetsModel(id=pet_id, name=name, specie=specie_mock, age=age, user_id=user_id)

    engine = db_connection.get_engine()
    # SQL Commands
    with engine.connect() as engine:
        engine.execute(
            text(f"INSERT INTO pets (id, name, specie, age, user_id) VALUES ('{pet_id}','{name}','{specie}','{age}','{user_id}');")
        )
        engine.commit()

        query_pet1 = pet_repository.select_pet(pet_id=pet_id)
        query_pet2 = pet_repository.select_pet(user_id=user_id)
        query_pet3 = pet_repository.select_pet(name=name)
        query_pet4 = pet_repository.select_pet(user_id=user_id, name=name)

        engine.execute(
            text(f"DELETE FROM pets WHERE id={pet_id};")
        )
        engine.commit()

    assert data in query_pet1
    assert data in query_pet2
    assert data in query_pet3
    assert data in query_pet4
