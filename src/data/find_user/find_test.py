from faker import Faker
from src.infra.test import UserRepositorySpy
from .find import FindUser

# o método não pretende testar a funcionalidade de select, uma vez que ela já foi testada no repository_test
# dessa forma, o método pretende testar os agentes de validação, que impedem/permitem a seleção correta do nosso modelo
faker = Faker()


def test_by_id():
    """Testing by_id method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.random_number(digits=2)}
    response = find_user.by_id(attributes["id"])

    # THEN
    print(response)
    assert user_repo.select_user_params["user_id"] == attributes["id"]
    assert response["Success"] is True
    assert response["Data"] is not None


def test_by_id_fail():
    """Testing fail by_id method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"id": faker.name()}
    response = find_user.by_id(attributes["id"])

    # THEN
    print(response)
    assert not user_repo.select_user_params

    assert response["Success"] is False
    assert response["Data"] is None


def test_by_name():
    """Testing by_name method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"name": faker.name()}
    response = find_user.by_name(attributes["name"])

    # THEN
    print(response)
    assert user_repo.select_user_params["name"] == attributes["name"]
    assert response["Success"] is True
    assert response["Data"] is not None


def test_by_name_fail():
    """Testing fail by_name method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"name": faker.random_number(digits=2)}
    response = find_user.by_name(attributes["name"])

    # THEN
    print(response)
    assert not user_repo.select_user_params

    assert response["Success"] is False
    assert response["Data"] is None


def test_by_id_and_name():
    """Testing by_id_and_name method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"user_id": faker.random_number(digits=2), "name": faker.name()}
    response = find_user.by_id_and_name(
        user_id=attributes["user_id"], name=attributes["name"]
    )

    # THEN
    print(response)
    assert user_repo.select_user_params["user_id"] == attributes["user_id"]
    assert user_repo.select_user_params["name"] == attributes["name"]

    assert response["Success"] is True
    assert response["Data"] is not None


def test_by_id_and_name_fail():
    """Testing fail by_id_and_name method"""

    user_repo = UserRepositorySpy()
    find_user = FindUser(user_repo)

    attributes = {"user_id": faker.name(), "name": faker.random_number(digits=2)}
    response = find_user.by_id_and_name(
        user_id=attributes["user_id"], name=attributes["name"]
    )

    # THEN
    print(response)
    assert not user_repo.select_user_params
    assert not user_repo.select_user_params

    assert response["Success"] is False
    assert response["Data"] is None
