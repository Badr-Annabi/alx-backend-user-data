#!/bin/usr/env python3
"""Module for authentication service"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """takes a password and returns a hashed password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
