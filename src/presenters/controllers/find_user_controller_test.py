from faker import Faker
from src.presenters.helpers import HttpRequest
from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from .find_user_controller import FindUserController

faker = Faker()


# Testa entrada (HttpRequest) e Testa saída (HttpResponse)
def test_handle():
    """Handle method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(
        query={"user_id": faker.random_number(digits=2), "name": faker.word()}
    )

    response = find_user_controller.handle(http_request)

    # Testing inputs
    print(response)
    assert (
        find_user_use_case.by_id_and_name_params["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_user_use_case.by_id_and_name_params["user_name"]
        == http_request.query["name"]
    )

    # Testing outputs
    assert response.status_code == 200
    assert response.body


def test_handle_fail_bad_request():
    """Fail Handle method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest()

    response = find_user_controller.handle(http_request)

    # Testing inputs
    print(response)
    assert not find_user_use_case.by_id_and_name_params
    assert not find_user_use_case.by_id_params
    assert not find_user_use_case.by_name_params

    # Testing outputs
    assert response.status_code == 400
    assert response.body["error"]


def test_handle_fail_unprocessable_entry():
    """Fail Handle method"""

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)

    http_request = HttpRequest(query={"user_id": faker.word()})

    response = find_user_controller.handle(http_request)

    # Testing inputs
    print(response)
    assert find_user_use_case.by_id_params["user_id"] == http_request.query["user_id"]

    # Testing outputs
    assert response.status_code == 422
    assert response.body["error"]
