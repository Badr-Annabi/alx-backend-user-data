#!/usr/bin/env python3
""" auth script defines _hash_password method for now """
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """method to hash a password"""
    bytes = password.encode("utf-8")

    salt = gensalt()

    hash = hashpw(bytes, salt)
    return(hash)


def _generate_uuid() -> str:
    """ returns a string representation of a new UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """method that registers a new user"""
        hashed_pwd = _hash_password(password)
        try:
            usr = self._db.find_user_by(email=email)
            if usr is not None:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            user = self._db.add_user(email=email, hashed_password=hashed_pwd)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """method that checks if a user is logged in"""
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                checkpw(password.encode('utf-8'), user.hashed_password)
                return True
        except NoResultFound:
            return False
        return False

    def create_session(self, email: str) -> str:
        """method that creates a new session"""
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
            return None
        except NoResultFound:
            return None
