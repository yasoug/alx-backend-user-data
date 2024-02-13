#!/usr/bin/env python3
"""module for the class BasicAuth"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """class for basic authentication"""
    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """Returns the Base64 part of the request header"""
        if not (authorization_header and isinstance(authorization_header, str)
                and authorization_header.startswith('Basic ')):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """Returns the decoded value of a Base64 string"""
        if not (base64_authorization_header and
                isinstance(base64_authorization_header, str)):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        """Returns user email and password from the Base64 decoded value"""
        if not (decoded_base64_authorization_header and
                isinstance(decoded_base64_authorization_header, str) and
                ':' in decoded_base64_authorization_header):
            return None, None
        email, password = decoded_base64_authorization_header.split(':')
        return email, password

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """Returns the User instance based on his email and password"""
        if not (user_email and isinstance(user_email, str) and
                user_pwd and isinstance(user_pwd, str)):
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None
        if not user or not user[0].is_valid_password(user_pwd):
            return None
        return user[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns current user or none"""
        auth_header = self.authorization_header(request)
        extracted = self.extract_base64_authorization_header(auth_header)
        decoded = self.decode_base64_authorization_header(extracted)
        email, password = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(email, password)
