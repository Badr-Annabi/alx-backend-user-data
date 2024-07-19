#!/usr/bin/env python3
"""Basic Flask app"""
from auth import Auth
from flask import Flask, abort, request, jsonify, make_response, redirect

AUTH = Auth()
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    POST /sessions
    Returns:
        session id
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response(
            jsonify({"email": email, "message": "logged in"}))
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """this function is used to logout user"""
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)
    # user = AUTH.get_user_from_session_id(session_id)
    # if user is None:
    #     abort(403)
    AUTH.destroy_session(session_id)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
