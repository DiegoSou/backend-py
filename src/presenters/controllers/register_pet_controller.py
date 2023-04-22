from typing import Type
from src.domain.use_cases import RegisterPet as RegisterPetInterface
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class RegisterPetController:
    """Define controller to register_pet use case"""

    def __init__(self, register_pet_use_case: Type[RegisterPetInterface]):
        self.register_pet_use_case = register_pet_use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """call register pet use case - post"""

        response = None

        if http_request.body:
            # If body

            body_params = http_request.body.keys()

            if (
                ("name" in body_params)
                and ("specie" in body_params)
                and ("user_information" in body_params)
            ):
                user_information_params = http_request.body["user_information"].keys()

                if ("user_id" in user_information_params) or (
                    "user_name" in user_information_params
                ):
                    name = http_request.body["name"]
                    specie = http_request.body["specie"]
                    user_information = http_request.body["user_information"]
                    age = http_request.body["age"] if "age" in body_params else 0

                    response = self.register_pet_use_case.register(
                        name=name,
                        specie=specie,
                        user_information=user_information,
                        age=age,
                    )
                else:
                    response = {"Success": False, "Data": None}
            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                http_error = HttpErrors.error_422()

                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        http_error = HttpErrors.error_400()

        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
