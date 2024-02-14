#!/usr/bin/env python3
"""module for the class SessionAuth"""

from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """class for session authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session for a given user"""
        if not user_id or type(user_id) != str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
