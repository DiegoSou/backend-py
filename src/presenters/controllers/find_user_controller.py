from typing import Type
from src.domain.use_cases import FindUser as FindUserInterface
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class FindUserController:
    """Define controller to find_user use case"""

    def __init__(self, find_user_use_case: Type[FindUserInterface]):
        self.find_user_use_case = find_user_use_case

    def handle(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """call find user use case - get"""

        response = None

        if http_request.query:
            # If query

            query_string_params = http_request.query.keys()

            if "user_id" in query_string_params and "name" in query_string_params:
                user_id = http_request.query["user_id"]
                name = http_request.query["name"]

                response = self.find_user_use_case.by_id_and_name(
                    user_id=user_id, name=name
                )

            elif "user_id" in query_string_params and "name" not in query_string_params:
                user_id = http_request.query["user_id"]

                response = self.find_user_use_case.by_id(user_id=user_id)

            elif "name" in query_string_params and "user_id" not in query_string_params:
                name = http_request.query["name"]

                response = self.find_user_use_case.by_name(name=name)

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                # call to errors - static method

                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If no query in http request - bad request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )
