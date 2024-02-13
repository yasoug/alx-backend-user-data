#!/usr/bin/env python3
"""module for the class Auth"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines required authentication"""
        if not path or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user"""
        return None
