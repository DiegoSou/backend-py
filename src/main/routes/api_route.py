from flask import Blueprint, jsonify, request
from src.main.composer import (
    register_user_composer,
    register_pet_composer,
    find_user_composer,
    find_pet_composer,
)
from src.main.adapter import flask_adapter

api_routes_blueprint = Blueprint("api_routes", __name__)


@api_routes_blueprint.route("/api/users", methods=["POST"])
def register_user():
    """register user route"""

    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())

    # success codes
    if response.status_code < 300:
        message = {
            "id": response.body.id,
            "type": "users",
            "attributes": {"name": response.body.name},
        }

        return jsonify({"data": message}), response.status_code

    # error codes
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_blueprint.route("/api/pets", methods=["POST"])
def register_pet():
    """register pet route"""

    message = {}
    response = flask_adapter(request=request, api_route=register_pet_composer())

    # success codes
    if response.status_code < 300:
        message = {
            "id": response.body.id,
            "type": "pets",
            "attributes": {
                "name": response.body.name,
                "specie": response.body.specie,
                "age": response.body.age,
            },
            "relationships": {"owner": {"id": response.body.user_id, "type": "users"}},
        }

        return jsonify({"data": message}), response.status_code

    # error codes
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@api_routes_blueprint.route("/api/users", methods=["GET"])
def find_user():
    """find users route"""

    message = {}
    response = flask_adapter(request=request, api_route=find_user_composer())

    # success codes
    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "id": element.id,
                    "type": "users",
                    "attributes": {"name": element.name},
                }
            )

        return jsonify({"data": message}), response.status_code

    # error codes
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )


@api_routes_blueprint.route("/api/pets", methods=["GET"])
def find_pet():
    """find pet route"""

    message = {}
    response = flask_adapter(request=request, api_route=find_pet_composer())

    # success codes
    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "id": element.id,
                    "type": "pets",
                    "attributes": {
                        "name": element.name,
                        "specie": element.specie.value,
                        "age": element.age,
                    },
                    "relationships": {
                        "owner": {"id": element.user_id, "type": "users"}
                    },
                }
            )

        return jsonify({"data": message}), response.status_code

    # error codes
    return jsonify(
        {"error": {"status": response.status_code, "title": response.body["error"]}}
    )
