import unittest
import json
from unittest.mock import patch, MagicMock
from server.api import app


class AuthUnitTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app
        self.client = app.test_client()

    def mock_verify_id_token(self, token):
        # Mock the verify_id_token function to return a predefined user ID
        if token == "VALID_TOKEN":
            return {"uid": "test_user_id", "admin": True}
        else:
            raise ValueError("Invalid token")

    def mock_get_user_by_email(self):
        # Mock the get_user_by_email function to return a predefined user
        user = MagicMock()
        user.uid = "test_user_id"
        return user

    @patch("server.api.auth.get_user_by_email")
    @patch("server.api.auth.create_custom_token")
    def test_login(self, mock_user_by_email, mock_create_custom_token):
        # Test the login endpoint
        mock_user_by_email.return_value = "odi8as98da0".encode()
        mock_create_custom_token.return_value = self.mock_get_user_by_email()

        payload = {"email": "test@example.com", "password": "test_password"}
        response = self.client.post("/login", json=payload)
        self.assertEqual(response.status_code, 200)

    def test_secure_endpoint_authorized(self):
        # Test a endpoint with a token
        headers = {"Authorization": "Bearer VALID_TOKEN"}
        response = self.client.get("/getSalesByEmployee", headers=headers)
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertIn("response", data)

    def test_secure_endpoint_unauthorized(self):
        # Test a endpoint without a token
        headers = {"Authorization": "Bearer"}
        response = self.client.get("/getSalesByEmployee", headers=headers)
        print(response.get_json())
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 403)
        self.assertIn("error", data)
        self.assertEqual(data["error"], "Unauthorized")
