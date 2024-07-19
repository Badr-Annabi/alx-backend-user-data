#!/usr/bin/env python3
"""Basic Flask app"""
from auth import Auth
from flask import Flask, abort, request, jsonify, make_response

Auth = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """
    GET /
    Return: payload containing a welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """this function is used to register a new user"""
    email, password = request.form.get("email"), request.form.get("password")
    try:
        Auth.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """
    this function is used to login a user
    Return: payload containing a login info
    """
    email, password = request.form.get("email"), request.form.get("password")
    if not Auth.valid_login(email, password):
        abort(401)
    session_id = Auth.create_session(email)
    res = make_response(
        jsonify({"email": email, "message": "logged in"}))
    res.set_cookie("session_id", session_id)
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
