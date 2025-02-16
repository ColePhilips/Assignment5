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