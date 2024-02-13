#!/usr/bin/env python3
"""module for the class BasicAuth"""

from api.v1.auth.auth import Auth


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
