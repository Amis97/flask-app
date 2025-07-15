import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_home():
    from app import app
    client = app.test_client()
    response = client.get('/')
    assert response.data == b'Hello from Flask via Jenkins CI/CD!'
