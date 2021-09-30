from flask import json
import pytest
from .test_init import client


@pytest.fixture
def post():
    post = {
        "title": "titulo1",
        "description": "descrip",
        "public": "True",
        "tags": ["1", "2"],
    }
    yield post


def test_post(client, post):
    resp = client.post("/api/posts")
    assert resp.status_code == 200


# def test_get(client):
# # get token
# rv = client.get('https://localhost:8000/api/health')
# response = json.loads(rv.data)
# csrftoken = response["data"]

# client.set_cookie('localhost', 'csrfmiddlewaretoken', str(csrftoken))
# resp = client.get('/api/posts')
# assert resp.status_code == 200


def test_server_status(client):
    rv = client.get("/api/health")
    assert rv.status_code == 200


def test_get(client):
    rv = client.get("/api/posts")
    assert rv.status_code == 200
