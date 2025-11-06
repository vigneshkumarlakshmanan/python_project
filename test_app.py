import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_home_redirect(client):
    """Check redirect when user not logged in"""
    response = client.get('/')
    assert response.status_code == 302  # redirect to login page

def test_login_page_loads(client):
    """Check login page loads"""
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data
