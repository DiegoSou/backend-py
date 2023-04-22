from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers import HttpRequest, HttpResponse


class RouteInterface(ABC):
    """Interface to routes"""

    @abstractmethod
    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining route"""

        raise Exception("Should implement method: route")
