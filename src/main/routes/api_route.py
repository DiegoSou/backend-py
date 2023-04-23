from flask import Blueprint, jsonify

# from src.main.composer import register_user_composer

api_routes_blueprint = Blueprint("api_routes", __name__)


@api_routes_blueprint.route("/api", methods=["GET"])
def something():
    """teste"""

    return jsonify({"greetings": "Olá Mundo"})
