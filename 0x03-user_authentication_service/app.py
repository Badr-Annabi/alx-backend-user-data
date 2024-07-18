#!/usr/bin/env python3
"""Basic Flask app"""
from auth import Auth
from flask import Flask, render_template, request, jsonify

Auth = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    GET /
    Return: payload containing a welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """this function is used to register a new user"""
    email, password = request.form.get("email"), request.form.get("password")
    try:
        Auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")