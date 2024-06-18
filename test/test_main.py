from fastapi.testclient import TestClient
#from app.main import app
from fastapi import FastAPI

app = FastAPI()
client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_create_users():
    response = client.post(
        "/create_user",
        json={
            "name": "test_pytest",
            "last_name": "test_pytest",
            "login": "test_pytest",
            "password": "test_pytest",
            "email": "test_pytest@gmail.com"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
            "name": "test_pytest",
            "last_name": "test_pytest",
            "login": "test_pytest",
            "password": "test_pytest",
            "email": "test_pytest@gmail.com"
        }
