"""
Views for the media module.
"""

from flask_restful import Resource
from flask.views import MethodView
from flask import request
from mongoengine.errors import ValidationError, NotUniqueError

from backend.apps.posts.models import Post as PostModel
from backend.apps.api.utils import makeRespone as res

from flask_babel import gettext as _ # for i18n

class Post(Resource):
    # HTTP POST method
    def post(self):
        body = request.get_json()

        try:
            post = PostModel(**body).save()
        except ValidationError:
            return res(None, 'One or more required fields are missing', 0, 400)
        except NotUniqueError:
            return res(None, 'Post already exist', 0, 409)

        return res(post.id, 'Success', 1, 200)

class Posts(Resource):
    # HTTP GET method
    def get(self, page):
        postsPagination = PostModel.objects(public=True).paginate(page, 10)
        currentPage = postsPagination.items
        
        count = len(currentPage)

        return res(currentPage, 'Success', count, 200)