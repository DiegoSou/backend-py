from faker import Faker
from src.data.test import RegisterPetSpy
from src.infra.test import PetRepositorySpy, UserRepositorySpy
from src.data.test import FindUserSpy
from src.presenters.helpers import HttpRequest
from .register_pet_controller import RegisterPetController


faker = Faker()


def test_route():
    """Test route method"""

    # mocks
    register_pet_use_case = RegisterPetSpy(
        pet_repository=PetRepositorySpy(), find_user=FindUserSpy(UserRepositorySpy())
    )

    register_pet_controller = RegisterPetController(register_pet_use_case)

    # define entries
    attributes = {
        "name": faker.name(),
        "specie": "DOG",
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            "user_name": faker.name(),
        },
    }

    response = register_pet_controller.route(http_request=HttpRequest(body=attributes))

    # Test inputs
    print(response)
    assert register_pet_use_case.register_params["name"] == attributes["name"]
    assert register_pet_use_case.register_params["specie"] == attributes["specie"]
    assert register_pet_use_case.register_params["age"] == attributes["age"]
    assert (
        register_pet_use_case.register_params["user_information"]
        == attributes["user_information"]
    )

    # Test output
    assert response.status_code == 200
    assert response.body


def test_route_fail_bad_request():
    """Fail route method"""

    # mocks
    register_pet_use_case = RegisterPetSpy(
        pet_repository=PetRepositorySpy(), find_user=FindUserSpy(UserRepositorySpy())
    )

    register_pet_controller = RegisterPetController(register_pet_use_case)

    # define entries
    attributes = {}

    response = register_pet_controller.route(http_request=HttpRequest(body=attributes))

    # Test inputs
    print(response)
    assert not register_pet_use_case.register_params

    # Test output
    assert response.status_code == 400
    assert response.body["error"]


def test_route_fail_unprocessable_entry():
    """Fail route method"""

    # mocks
    register_pet_use_case = RegisterPetSpy(
        pet_repository=PetRepositorySpy(), find_user=FindUserSpy(UserRepositorySpy())
    )

    register_pet_controller = RegisterPetController(register_pet_use_case)

    # define entries
    attributes = {"name": faker.random_number(digits=2)}

    response = register_pet_controller.route(http_request=HttpRequest(body=attributes))

    # Test inputs
    print(response)
    assert not register_pet_use_case.register_params

    # Test output
    assert response.status_code == 422
    assert response.body["error"]
