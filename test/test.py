
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_create_users():
    response = client.post(
        "/create_user",
        json={},
    )
    assert response.status_code == 200
    assert response.json() == {}