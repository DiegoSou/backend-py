from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import FindPet as FindPetInterface
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class FindPetController(RouteInterface):
    """Define controller to find_pet use case"""

    def __init__(self, find_pet_use_case: Type[FindPetInterface]):
        self.find_pet_use_case = find_pet_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """call to find pet use case - get"""

        response = None

        if http_request.query:
            # If query

            query_string_params = (
                http_request.query.keys()
            )  # the adapters will ensure this as a dictionary

            if "pet_id" in query_string_params:
                pet_id = http_request.query["pet_id"]

                response = self.find_pet_use_case.by_pet_id(pet_id=pet_id)

            elif "user_id" in query_string_params and "name" in query_string_params:
                user_id = http_request.query["user_id"]
                name = http_request.query["name"]

                response = self.find_pet_use_case.by_user_id_and_name(
                    user_id=user_id, name=name
                )

            elif "user_id" in query_string_params:
                user_id = http_request.query["user_id"]

                response = self.find_pet_use_case.by_user_id(user_id=user_id)

            elif "name" in query_string_params:
                name = http_request.query["name"]

                response = self.find_pet_use_case.by_name(name=name)

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                # call to errors - static method

                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If no query - bad request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
