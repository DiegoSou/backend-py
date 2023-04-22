from faker import Faker
from src.data.test import RegisterUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest
from .register_user_controller import RegisterUserController


faker = Faker()


def test_handle():
    """Test handle method"""

    # mocks
    register_user_use_case = RegisterUserSpy(user_repository=UserRepositorySpy())

    register_user_controller = RegisterUserController(register_user_use_case)

    # define entries
    attributes = {"name": faker.name(), "password": faker.word()}

    response = register_user_controller.handle(
        http_request=HttpRequest(body=attributes)
    )

    # Test inputs
    print(response)
    assert register_user_use_case.register_params["name"] == attributes["name"]
    assert register_user_use_case.register_params["password"] == attributes["password"]

    # Test output
    assert response.status_code == 200
    assert response.body


def test_handle_fail_bad_request():
    """Test fail handle method"""

    # mocks
    register_user_use_case = RegisterUserSpy(user_repository=UserRepositorySpy())

    register_user_controller = RegisterUserController(register_user_use_case)

    # define entries
    attributes = {}

    response = register_user_controller.handle(
        http_request=HttpRequest(body=attributes)
    )

    # Test inputs
    print(response)
    assert not register_user_use_case.register_params

    # Test output
    assert response.status_code == 400
    assert response.body["error"]


def test_handle_fail_unprocessable_entry():
    """Test handle method"""

    # mocks
    register_user_use_case = RegisterUserSpy(user_repository=UserRepositorySpy())

    register_user_controller = RegisterUserController(register_user_use_case)

    # define entries
    attributes = {"name": faker.random_number(digits=5), "password": faker.word()}

    response = register_user_controller.handle(
        http_request=HttpRequest(body=attributes)
    )

    # Test inputs
    print(response)
    assert register_user_use_case.register_params["name"] == attributes["name"]
    assert register_user_use_case.register_params["password"] == attributes["password"]

    # Test output
    assert response.status_code == 422
    assert response.body["error"]
