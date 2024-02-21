#!/usr/bin/env python3
"""auth module"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """returns a salted, hashed password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
