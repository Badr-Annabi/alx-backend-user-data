#!/usr/bin/env python3
"""Basic auth Class"""


from .auth import Auth
import base64


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
