from faker import Faker
from src.infra.test import UserRepositorySpy
from .register import RegisterUser

faker = Faker()


def test_register():
    """Registry method"""

    # o método não pretende testar a funcionalidade de inserir, uma vez que ela já foi testada no repository_test
    # dessa forma, o método pretende testar os agentes de validação, que impedem/permitem a inserção do nosso modelo

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.name(), "password": faker.name()}

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    # THEN - vai testar se as informções foram recebidas
    print(response)

    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """Fail registry method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    # the name must not be a number
    attributes = {"name": faker.random_number(digits=2), "password": faker.name()}

    response = register_user.register(
        name=attributes["name"], password=attributes["password"]
    )

    # THEN
    print(response)

    assert not user_repo.insert_user_params

    assert response["Success"] is False
    assert response["Data"] is None
