#!/usr/bin/env python3
"""module for the class Auth"""

from typing import List, TypeVar
from flask import request
from fnmatch import fnmatch
from os import getenv


class Auth:
    """Class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determines required authentication"""
        if not path or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        return not [n for n in excluded_paths if fnmatch(path, n)]

    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header"""
        if not request:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user"""
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""
        if not request:
            return None
        return request.cookies.get(getenv('SESSION_NAME'))
