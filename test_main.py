from fastapi.testclient import TestClient
from main import app
import requests

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Hacker News API."}

def test_top_news_success():
    response = client.get("/top-news?count=5")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 5

def test_top_news_invalid_count():
    response = client.get("/top-news?count=-1")
    assert response.status_code == 422  # FastAPI automatically validates query parameters

def test_top_news_api_failure(monkeypatch):
    # Simulate a failure in the Hacker News API
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 503
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    
    response = client.get("/top-news?count=5")
    assert response.status_code == 503
    assert response.json() == {"detail": "Hacker News API is unavailable"}
