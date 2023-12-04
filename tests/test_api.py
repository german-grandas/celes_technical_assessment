import pytest
from unittest.mock import patch

from server.api import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
