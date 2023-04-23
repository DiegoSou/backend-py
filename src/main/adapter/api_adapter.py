from typing import Type
from sqlalchemy.exc import IntegrityError
from src.main.interface import RouteInterface
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


def flask_adapter(request: any, api_route: Type[RouteInterface]) -> any:
    """Adapter pattern to flask
    :params - request: Flask request
            - api_route: Route controller
    :return - any
    """

    http_request = HttpRequest(body=request.json)

    try:
        response = api_route.route(http_request)
    except IntegrityError:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
