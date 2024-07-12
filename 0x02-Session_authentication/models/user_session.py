#!/usr/bin/env python3
"""Create a UserSession class"""


from .base import Base


class UserSession(Base):
    """This class represents a user session"""
    def __init__(self, *args: list, **kwargs: dict) -> None:
        """Initialize the UserSession instance"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
