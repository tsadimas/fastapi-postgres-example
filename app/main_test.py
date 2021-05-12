from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data.database import Base
from main import app, get_db
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


client = TestClient(app)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


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

