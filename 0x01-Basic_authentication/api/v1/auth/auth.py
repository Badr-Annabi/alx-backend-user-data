#!/usr/bin/env pyhton3
"""Create a class to manage the Api auth"""


from flask import request
from typing import List, TypeVar


class Auth():
    """Manages the API Authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method that requires auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """Public method for authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None
