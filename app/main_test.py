from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/items")
    assert response.status_code == 200

def test_create_user():
    response = client.post(
        "/users/",
        headers={'Content-Type': 'application/json'},
        json={"email": "user@test.com", "password": "pass123"},
    )
    assert response.status_code == 200
    assert response.json() == {
    "email": "user@test.com",
    "id": 1,
    "is_active": True,
    "items": []
    }

