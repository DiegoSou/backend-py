# Testar os agentes de validação para o caso de uso de registrar um novo pet
# Testar a validação de encontrar usuários pelas credenciais id ou name

from faker import Faker
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from src.data.test import FindUserSpy
from .register import RegisterPet

faker = Faker()


def test_register():
    """Registry method"""

    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())

    register_pet = RegisterPet(pet_repository=pet_repo, find_user=find_user)

    attributes = {
        "name": faker.name(),
        "specie": "DOG",
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "user_name": faker.name(),
        },
    }

    response = register_pet.register(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_information=attributes["user_information"],
    )

    # THEN
    print(pet_repo.insert_pet_params)
    assert pet_repo.insert_pet_params["name"] == attributes["name"]
    assert pet_repo.insert_pet_params["specie"] == attributes["specie"]
    assert pet_repo.insert_pet_params["age"] == attributes["age"]
    assert (
        pet_repo.insert_pet_params["user_id"]
        == attributes["user_information"]["user_id"]
    )

    assert (
        find_user.by_id_and_name_params["user_id"]
        == attributes["user_information"]["user_id"]
    )
    assert (
        find_user.by_id_and_name_params["user_name"]
        == attributes["user_information"]["user_name"]
    )

    assert response["Success"] is True
    assert response["Data"] is not None


def test_register_fail():
    """Registry method"""

    pet_repo = PetRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())

    register_pet = RegisterPet(pet_repository=pet_repo, find_user=find_user)

    attributes = {
        "name": faker.random_number(digits=2),
        "specie": "DOG",
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "user_name": faker.name(),
        },
    }

    response = register_pet.register(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_information=attributes["user_information"],
    )

    # THEN
    print(response)
    assert not pet_repo.insert_pet_params

    assert response["Success"] is False
    assert response["Data"] is None
