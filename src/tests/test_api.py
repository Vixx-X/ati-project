# from datetime import datetime
# from flask import json
# import pytest
# from .test_init import client, user
# from flask_wtf.csrf import generate_csrf
# from backend.apps.posts.models import Post

# # @pytest.fixture(scope="class")
# @pytest.fixture
# def post_info():
#     post_info = {
#         "title": "titulo1",
#         "description": "descrip",
#         "public": "True",
#         "tags": ["1", "2"],
#     }
#     return post_info

# @pytest.fixture
# def comment(user):
#     comment = {
#         "author": user,
#         "content": "This is a comment",
#         "time_created": datetime.utcnow(),
#     }

#     return comment

# # POST TESTS
# # @pytest.mark.usefixtures("postID")
# def test_post(client, post_info):
#     resp = client.post('/api/posts', data=post_info)
#     assert resp.status_code == 201

# def test_get(client):
#     rv = client.get('/api/posts')
#     assert rv.status_code == 200

# def test_get_detail(client):
#     rv = client.get('/api/posts')
#     data = json.loads(rv.data)
#     postID = data["data"]["id"]

#     rv = client.get(f'/api/posts/{postID}')
#     assert rv.status_code == 200


# # COMENT TEST
# def test_post(self, client, comment):
#     rv = client.get('/api/posts')
#     data = json.loads(rv.data)
#     postID = data["data"]["id"]
#     resp = client.post(f'/api/posts/{postID}/comments', data=comment)
#     assert resp.status_code == 201

# def test_get(self, client):
#     rv = client.get('/api/posts')
#     data = json.loads(rv.data)
#     postID = data["data"]["id"]
#     resp = client.post(f'/api/posts/{postID}/comments')
#     assert resp.status_code == 200

