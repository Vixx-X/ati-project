from datetime import datetime
from flask import json
import pytest
from .test_init import client, user
from backend.apps.posts.models import Post

# POST TESTS
@pytest.fixture
def post_info():
    post = {
        "title": "titulo1",
        "description": "descrip",
        "public": "True",
        "tags": ["1", "2"],
    }
    
    yield post

class Post_test():
    def test_post_post(client, post_info):
        # get token
        rv = client.get('https://localhost:8000/api/health')
        response = json.loads(rv.data)
        csrftoken = response["data"]

        resp = client.post('/api/posts', headers={'csrfmiddlewaretoken': str(csrftoken)},
                        data=post_info)
        assert resp.status_code == 200

    def test_post_get(client):
        rv = client.get('/api/posts')
        assert rv.status_code == 200


# COMENT TEST
@pytest.fixture
def comment(user):
    comment = {
        "author": user,
        "content": "This is a comment",
        "time_created": datetime.utcnow(),
    }

    yield comment

@pytest.fixture(scope="class")
def postID():
    postID = Post(post_info).save()["id"]
    yield postID

class Comment_Test("postID"):
    def test_post(self, client, comment):
        # get token
        rv = client.get('https://localhost:8000/api/health')
        response = json.loads(rv.data)
        csrftoken = response["data"]

        resp = client.post(f'/api/posts/{self.postID}/comments', headers={'csrfmiddlewaretoken': str(csrftoken)},
                        data=comment)
        assert resp.status_code == 200

    def test_get(self, client, comment, post_info):
        resp = client.post(f'/api/posts/{self.postID}/comments')
        assert resp.status_code == 200

