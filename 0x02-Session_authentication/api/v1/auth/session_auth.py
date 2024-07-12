#!/usr/bin/env python3
"""Session authentication Class"""


from uuid import uuid4
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