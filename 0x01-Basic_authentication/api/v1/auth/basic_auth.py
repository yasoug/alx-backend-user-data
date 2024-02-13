#!/usr/bin/env python3
"""module for the class BasicAuth"""

from api.v1.auth.auth import Auth
import base64


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
