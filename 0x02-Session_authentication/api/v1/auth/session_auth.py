#!/usr/bin/env python3
"""Session authentication Class"""


from uuid import uuid4
from models.user import User
from .auth import Auth


class SessionAuth(Auth):
    """Session auth class that inherits from Auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """This method creates a session ID for user_id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """This module returns a User ID based on a Session ID"""
        if isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        """This method returns a User instance based on a cookie value"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """This module deletes the user session
        (log out the user)"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if (request is None or session_id is None) or user_id is None:
            return False
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]
        return True
