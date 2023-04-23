from flask import Blueprint, jsonify, request
from src.main.composer import register_user_composer
from src.main.adapter import flask_adapter

# from src.main.composer import register_user_composer

api_routes_blueprint = Blueprint("api_routes", __name__)


@api_routes_blueprint.route("/api/users", methods=["POST"])
def register_user():
    """register user route"""

    message = {}
    response = flask_adapter(request=request, api_route=register_user_composer())

    # success codes
    if response.status_code < 300:
        message = {
            "attributes": {"name": response.body.name},
            "id": response.body.id,
            "type": "users",
        }

        return jsonify({"data": message}), response.status_code

    # error codes
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )
