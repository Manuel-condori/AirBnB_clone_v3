#!/usr/bin/python3
"""This module starts a flask app"""
from os import getenv
from models import storage
from flask import Flask, jsonify
from api.v1.views import app_views
from werkzeug.exceptions import HTTPException
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
swagger = Swagger(app)


@app.teardown_appcontext
def teardown(exception):
    """Handle teardown"""
    storage.close()


@app.route('/')
def hello_world():
    """Returns a text when / route is requested"""
    return 'Hello HBNB!'


@app.errorhandler(404)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port)
