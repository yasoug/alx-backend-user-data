#!/usr/bin/env python3
"""module for the class Auth"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines required authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user"""
        return None
