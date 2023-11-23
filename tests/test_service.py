import pytest
import requests
import unittest.mock as mock
import source.service as service

# Define function that will be mocked
@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    # Define return value from the mocking function
    mock_get_user_from_db.return_value = ("Mocked Alice")
    # Calling the original function
    # Under the hood pytest will call mock_get_user_from_db
    user_name = service.get_user_from_db(1)
    
    # Check
    assert user_name == "Mocked Alice"
    

@mock.patch("requests.get")
def test_get_user(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Mockinvich"}
    mock_get.return_value = mock_response
    
    data = service.get_users()
    
    assert data == {"id": 1, "name": "John Mockinvich"}

@mock.patch("requests.get")
def test_get_user_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    
    with pytest.raises(requests.HTTPError):
        service.get_users()