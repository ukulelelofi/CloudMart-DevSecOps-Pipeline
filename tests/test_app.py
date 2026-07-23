from src.app import app, calculate_total



def test_calculate_total():
    assert calculate_total(100, 2) == 200


def test_homepage():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Welcome to CloudMart Solutions!" in response.data


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
