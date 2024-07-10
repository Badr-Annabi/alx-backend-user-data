#!/usr/bin/env python3
"""
Route module for the API
"""
import os
from os import getenv
from typing import Tuple
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def req_unauth(error: Exception) -> Tuple[jsonify, int]:
    """Req Unauth handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def user_not_allowed(error: Exception) -> Tuple[jsonify, int]:
    """user auth but not allowed handler"""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)