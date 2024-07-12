#!/usr/bin/env python3
"""Create a class to manage the Api auth"""


from flask import request
from typing import List, TypeVar


class Auth():
    """Manages the API Authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public method that requires auth
        Return:
            True if path in excluded_paths
            False if not
        """
        if path is None or excluded_paths is None:
            return True
        nomal_path = path.rstrip('/')
        for excluded_path in excluded_paths:
            if nomal_path == excluded_path.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Public method for authorization header"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None
