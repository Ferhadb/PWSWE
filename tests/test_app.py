# tests/test_app.py
from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_index_route():
    """Tests the '/' route to ensure it returns 'Hello, World!'."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.content == b"Hello, World!"


def test_greet_route():
    """Tests the '/greet/<name>' route with a sample name."""
    response = client.get("/greet/TestUser")
    assert response.status_code == 200
    assert b"Hello, TestUser!" in response.content
