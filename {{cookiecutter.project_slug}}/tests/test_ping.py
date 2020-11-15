from fastapi.testclient import TestClient

# import our instance of FastAPI() that was saved
#   in the 'api' variable in the app/main.py file
from app.main import api


client = TestClient(api)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json()['ping'] == 'pong'
