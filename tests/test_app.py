import pytest

from app.main import app, add


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"CI/CD Pipeline" in response.data


def test_health(client):
    response = client.get("/health")
    assert response.get_json() == {"status": "ok"}


def test_add_route(client):
    response = client.get("/add/4/6")
    assert response.get_json() == {"result": 10}
