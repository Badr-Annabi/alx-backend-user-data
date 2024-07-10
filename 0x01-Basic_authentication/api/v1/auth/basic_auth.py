#!/usr/bin/env python3
"""Basic auth Class"""


from .auth import Auth


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
