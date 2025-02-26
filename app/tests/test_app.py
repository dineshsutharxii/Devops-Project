import requests

BASE_URL = "http://localhost:5000"

def test_health_check():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_counter():
    response1 = requests.get(f"{BASE_URL}/counter")
    response2 = requests.get(f"{BASE_URL}/counter")

    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response2.json()["counter"] + 1 == response1.json()["counter"] + 2
