import unittest

from server.api import app


class RootUnitTest(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app
        self.client = app.test_client()

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
