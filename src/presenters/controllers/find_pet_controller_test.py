from faker import Faker
from src.infra.test import PetRepositorySpy
from src.data.test import FindPetSpy
from src.presenters.helpers import HttpRequest
from .find_pet_controller import FindPetController


faker = Faker()


# Testa Entrada (http_request) e Testa Saída (http_response)
def test_handle():
    """Handle method"""

    find_pet_use_case = FindPetSpy(pet_repository=PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    http_request = HttpRequest(
        query={"user_id": faker.random_number(digits=5), "name": faker.word()}
    )

    response = find_pet_controller.handle(http_request)

    # Test inputs
    print(response)

    assert (
        find_pet_use_case.by_user_id_and_name_params["user_id"]
        == http_request.query["user_id"]
    )
    assert (
        find_pet_use_case.by_user_id_and_name_params["name"]
        == http_request.query["name"]
    )

    # Test outputs
    assert response.status_code == 200
    assert response.body


def test_handle_fail_bad_request():
    """Fail handle method"""

    find_pet_use_case = FindPetSpy(pet_repository=PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    http_request = HttpRequest(query={})

    response = find_pet_controller.handle(http_request)

    # Test inputs
    print(response)
    assert not find_pet_use_case.by_pet_id_params
    assert not find_pet_use_case.by_name_params
    assert not find_pet_use_case.by_user_id_params
    assert not find_pet_use_case.by_user_id_and_name_params

    # Test outputs
    assert response.status_code == 400
    assert response.body["error"]


def test_handle_fail_unprocessable_entry():
    """Fail handle method"""

    find_pet_use_case = FindPetSpy(pet_repository=PetRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)

    http_request = HttpRequest(query={"pet_id": faker.word()})

    response = find_pet_controller.handle(http_request)

    # Test inputs
    print(response)
    assert find_pet_use_case.by_pet_id_params["pet_id"] == http_request.query["pet_id"]

    # Test outputs
    assert response.status_code == 422
    assert response.body
