#!/usr/bin/env python3
"""Basic auth Class"""


from .auth import Auth
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """Class that inheits from Auth"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """Returns the Base64 part of the Authorization"""
        keyword = 'Basic '
        keyword_len = len(keyword)
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if 'Basic' not in authorization_header:
            return None
        position = authorization_header.find(keyword)
        if position != -1:
            return authorization_header[position + keyword_len:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """
        Returns the decoded value of a Base64
        string base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(
                base64_authorization_header,
                validate=True)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """
        Returns the user email and password
        from the Base64 decode value
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        usr_psw = decoded_base64_authorization_header.split(':', 1)
        if len(usr_psw) != 2:
            return (None, None)
        return (usr_psw[0], usr_psw[1])

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance
        based on his email and password.
        """
        if user_email is None or user_pwd:
            return None
        
