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

    # pass error codes
    if response.status_code < 300:
        message = {
            "Type": "users",
            "id": response.body.id,
            "attributes": {"name": response.body.name},
        }

        return jsonify({"data": message}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


#
# @api_routes_blueprint.route("/api", methods=["GET"])
# def get_dict_params():
#     """teste"""
#
#     return jsonify({"query_params" : request.args.to_dict()})
#
# @api_routes_blueprint.route("/api", methods=["GET"])
# def something():
#     """teste"""
#
#     return jsonify({"greetings": "Olá Mundo"})
