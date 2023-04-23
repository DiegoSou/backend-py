from flask import Flask
from flask_cors import CORS

from src.main.routes import api_routes_blueprint

app = Flask(__name__)
CORS(app)  # middware

app.register_blueprint(api_routes_blueprint)
