import pytest
from app import app

@pytest.fixture
def client():
    # Create a test client using the Flask application for testing
    with app.test_client() as client:
        yield client

def test_sanitization_positive(client):
    # Test case where the input is sanitized
    response = client.post('/v1/sanitized/input/', json={'input': 'valid input'})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.get_json() == {'result': 'sanitized'}, "Unexpected JSON response"

def test_sanitization_negative(client):
    # Test case where the input is unsanitized that means it contains SQL injection characters
    response = client.post('/v1/sanitized/input/', json={'input': "user'; DROP TABLE users;"})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.get_json() == {'result': 'unsanitized'}, "Unexpected JSON response"

def test_sanitization_whitespace_input(client):
    # Test case with whitespace-only input
    response = client.post('/v1/sanitized/input/', json={'input': '   '})
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert response.get_json() == {'error': 'Empty input value'}, "Unexpected JSON response"

def test_invalid_payload(client):
    # Test case with an invalid JSON payload
    response = client.post('/v1/sanitized/input/', json={'invalid_key': 'some input'})
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert response.get_json() == {'error': 'Missing input key'}, "Unexpected JSON response"

def test_missing_input_key(client):
    # Test case with a missing 'input' key in the invalid JSON payload
    response = client.post('/v1/sanitized/input/', json={'invalid_key': ''})
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert response.get_json() == {'error': 'Missing input key'}, "Unexpected JSON response"

def test_missing_input_value(client):
    # Test case with an empty 'input' value in the JSON payload
    response = client.post('/v1/sanitized/input/', json={'input': ''})
    assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
    assert response.get_json() == {'error': 'Empty input value'}, "Unexpected JSON response"


if __name__ == '__main__':
    pytest.main()

