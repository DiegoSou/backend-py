from faker import Faker
from src.infra.test import PetRepositorySpy
from .find import FindPet

# o método não pretende testar a funcionalidade de select, uma vez que ela já foi testada no repository_test
# dessa forma, o método pretende testar os agentes de validação, que impedem/permitem a seleção correta do nosso modelo
faker = Faker()


def test_by_id():
    """Testing find by id"""

    pet_repo = PetRepositorySpy()
    find_pet_use_case = FindPet(pet_repository=pet_repo)

    attributes = {"pet_id": faker.random_number(digits=2)}
    response = find_pet_use_case.by_pet_id(attributes["pet_id"])

    # THEN
    print(response)
    assert pet_repo.select_pet_params["pet_id"] == attributes["pet_id"]

    assert response["Success"] is True
    assert response["Data"] is not None


def test_by_id_fail():
    """Testing fail find by id"""

    pet_repo = PetRepositorySpy()
    find_pet_use_case = FindPet(pet_repository=pet_repo)

    attributes = {"pet_id": faker.name()}
    response = find_pet_use_case.by_pet_id(attributes["pet_id"])

    # THEN
    print(response)
    assert not pet_repo.select_pet_params

    assert response["Success"] is False
    assert response["Data"] is None


def test_by_user_id():
    """Testing find by pet owner id (user)"""

    pet_repo = PetRepositorySpy()
    find_pet_use_case = FindPet(pet_repository=pet_repo)

    attributes = {"user_id": faker.random_number(digits=2)}
    response = find_pet_use_case.by_user_id(attributes["user_id"])

    # THEN
    print(response)
    assert pet_repo.select_pet_params["user_id"] == attributes["user_id"]

    assert response["Success"] is True
    assert response["Data"] is not None


def test_by_user_id_fail():
    """Testing fail find by pet owner id (user)"""

    pet_repo = PetRepositorySpy()
    find_pet_use_case = FindPet(pet_repository=pet_repo)

    attributes = {"user_id": faker.name()}
    response = find_pet_use_case.by_user_id(attributes["user_id"])

    # THEN
    print(response)
    assert not pet_repo.select_pet_params

    assert response["Success"] is False
    assert response["Data"] is None


def test_by_name():
    """Testing find by pet name"""

    pet_repo = PetRepositorySpy()
    find_pet_use_case = FindPet(pet_repository=pet_repo)

    attributes = {"name": faker.name()}
    response = find_pet_use_case.by_name(attributes["name"])

    # THEN
    print(response)
    assert pet_repo.select_pet_params["name"] == attributes["name"]

    assert response["Success"] is True
    assert response["Data"] is not None


def test_by_name_fail():
    """Testing fail find by pet name"""

    pet_repo = PetRepositorySpy()
    find_pet_use_case = FindPet(pet_repository=pet_repo)

    attributes = {"name": faker.random_number(digits=2)}
    response = find_pet_use_case.by_name(attributes["name"])

    # THEN
    print(response)
    assert not pet_repo.select_pet_params

    assert response["Success"] is False
    assert response["Data"] is None


def test_by_user_id_and_name():
    """Testing find by user id and name"""

    pet_repo = PetRepositorySpy()
    find_pet_use_case = FindPet(pet_repository=pet_repo)

    attributes = {"user_id": faker.random_number(digits=2), "name": faker.name()}
    response = find_pet_use_case.by_user_id_and_name(
        user_id=attributes["user_id"], name=attributes["name"]
    )

    # THEN
    print(response)
    assert (
        pet_repo.select_pet_params["user_id"] == attributes["user_id"]
        and pet_repo.select_pet_params["name"] == attributes["name"]
    )

    assert response["Success"] is True
    assert response["Data"] is not None


def test_by_user_id_and_name_fail():
    """Testing find by user id and name"""

    pet_repo = PetRepositorySpy()
    find_pet_use_case = FindPet(pet_repository=pet_repo)

    attributes = {
        "user_id": faker.random_number(digits=2),
        "name": faker.random_number(digits=2),
    }
    response = find_pet_use_case.by_user_id_and_name(
        user_id=attributes["user_id"], name=attributes["name"]
    )

    # THEN
    print(response)
    assert not pet_repo.select_pet_params

    assert response["Success"] is False
    assert response["Data"] is None
