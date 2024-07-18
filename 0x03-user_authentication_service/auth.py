#!/bin/usr/env python3
"""creae a method for encrypting passwords"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """takes a password and returns a hashed password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
