import pytest
from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
from api import app, Monster  # Import the app and Monster class from your api.py
from unittest.mock import patch, MagicMock

# Create a test client
@pytest.fixture
def client():
    app.config["MONGO_URI"] = "mongodb://localhost:27017/test_db"  # Use a test database
    with app.test_client() as client:
        yield client

# Mock MongoDB
@pytest.fixture
def mock_mongo():
    with patch('api.mongo') as mock:
        mock.db.monsters = MagicMock()
        yield mock

#1 Test POST for /monsters
def test_create_monster(client, mock_mongo):
    response = client.post('/monsters', json={
        "name": "Test Monster"
        "description": "Test Description"
        "type": "Test Type"
    })
    assert response.status_code == 200
    assert response.json['name'] == "Test Monster"

#2 Test POST for /monsters without a name
def test_create_monster_without_name(client, mock_mongo):
    response = client.post('/monsters', json={
        #"name": "Test Monster"
        "description": "Test Description"
        "type": "Test Type"
    })
    assert response.status_code == 400
    assert response.json['message'] == "Name and description are required!"

#3 Test POST for /monsters with missing description
def test_create_missing_description(client, mock_mongo):
    response = client.post('/monsters', json={
        "name": "Test Monster"
        #"description": "Test Description"
        "type": "Test Type"
    })
    assert response.status_code == 400
    assert response.json['message'] == "Name and description are required!"

#4 Test POST for /monsters with invalid data
def test_create_invalid_id(client, mock_mongo):
    response = client.post('/monsters', json={})
    assert response.status_code == 400
    assert response.json['message'] == "Name and description are required!"

#5 Test POST for /monsters with duplicate name
def test_create_duplicate(client, mock_mongo):
    mock_mongo.db.monsters.find_one.return_value = {"name": "Duplicate Monster"}
    response = client.post('/monsters', json={
        "name": "Duplicate Monster",
        "description": "A monster for testing",
        "type": "Test Type"
    })
    assert response.status_code == 400
    assert response.json['message'] == "Monster with this name already exists!"

#6 Test GET for /monsters
def test_get_all_monsters(client, mock_mongo):
    mock_mongo.db.monsters.find.return_value = [
        {"id": 1, "name": "Monster1", "description": "Description1", "type": "Type1"},
        {"id": 2, "name": "Monster2", "description": "Description2", "type": "Type2"}
    ]
    response = client.get('/monsters')
    assert response.status_code == 200
    assert len(response.json) == 2
    
#7 Test GET for /monsters/<id>
def test_get_monster_by_id(client, mock_mongo):

#8 Test GET for /monsters/<id> for not found
def Test_get_not_found(client, mock_mongo):

#9 Test GET for /monsters with no monsters
def test_get_empty_db(client, mock_mongo):

#10 Test GET for /monsters/<id> with non-integer id
def test_get_nonInteger(client, mock_mongo):

#11 Test GET for /monsters with specific type filter
def test_get_filter(client, mock_mongo):

#12 Test PUT for /monsters/<id>
def test_update_monster(client, mock_mongo):

#13 Test PUT for /monsters/<id> for not found
def test_update_not_found(client, mock_mongo):

#14 Test PUT for /monsters/<id> with missing fields
def test_update_missing_field(client, mock_mongo):

#15 Test PUT for /monsters/<id> with non-integer id
def test_update_nonInteger(client, mock_mongo):

#16 Test DELETE for /monsters/<id>
def test_delete_monster(client, mock_mongo):

#17 Test DELETE for /monsters/<id> for not found
def test_delete_not_found(client, mock_mongo):

#18 Test DELETE for /monsters/<id> with invalid id
def test_delete_invalid_id(client, mock_mongo):

#19 Test DELETE for /monsters/<id> with non-integer id
def test_delete_nonInteger(client, mock_mongo):

#20 Test that the app runs without errors
def test_app_runs(client, mock_mongo):