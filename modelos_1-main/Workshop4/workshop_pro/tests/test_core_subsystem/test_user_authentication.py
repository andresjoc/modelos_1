import pytest
import json
from unittest.mock import MagicMock, patch, mock_open
from workshop_pro.core_subsystem.user_authentication import User, Authentication


# Datos de ejemplo para el archivo users.json
mock_user_data = json.dumps(
    [
        {
            "username": "test_user",
            "password": "password123",
            "grants": {"read": True, "write": False},
        }
    ]
)


class TestUser:
    def test_get_username(self):
        user = User(username="test_user", grants={"read": True, "write": False})
        assert user.get_username() == "test_user"

    def test_is_grant(self):
        user = User(username="test_user", grants={"read": True, "write": False})
        assert user.is_grant("read") is True
        assert user.is_grant("write") is False


class TestAuthentication:
    @patch("builtins.open", new_callable=mock_open, read_data=mock_user_data)
    def test_authenticate_success(self, mock_file):
        auth = Authentication(username="test_user", password="password123")
        assert auth.authenticate() is True

    @patch("builtins.open", new_callable=mock_open, read_data=mock_user_data)
    def test_authenticate_failure(self, mock_file):
        auth = Authentication(username="test_user", password="wrongpassword")
        assert auth.authenticate() is False

    @patch("builtins.open", new_callable=mock_open, read_data=mock_user_data)
    def test_userdata(self, mock_file):
        auth = Authentication(username="test_user", password="password123")
        auth.authenticate()
        user = auth.userdata()
        assert user.get_username() == "test_user"
        assert user.is_grant("read") is True
        assert user.is_grant("write") is False
