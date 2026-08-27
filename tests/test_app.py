import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"User Management Service"


def test_token(client):
    response = client.get("/token")

    assert response.status_code == 200

    data = response.get_json()

    assert "token" in data


def test_admin_calc(client):
    response = client.get("/admin/calc?expr=1%2B2")

    assert response.status_code == 200

    data = response.get_json()

    assert data["result"] == 3


def test_user_not_found(client):
    response = client.get("/user?id=999999")

    assert response.status_code == 404