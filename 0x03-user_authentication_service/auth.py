#!/usr/bin/env python3
"""Module for authentication service"""
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
import bcrypt


def _hash_password(password: str) -> bytes:
    """takes a password and returns a hashed password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """this method registers a new user"""
        hashed_pwd = _hash_password(password)
        try:
            usr = self._db.find_user_by(email=email)
            if usr is not None:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            user = self._db.add_user(email=email, hashed_password=hashed_pwd)
        return user
