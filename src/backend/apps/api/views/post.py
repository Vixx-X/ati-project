"""
Views for the media module.
"""

from flask import request
from mongoengine.errors import ValidationError, NotUniqueError
from backend.apps.api.views.utils import APIView

from backend.apps.posts.models import Post as PostModel
from backend.apps.api.utils import makeRespone as res

from flask_babel import gettext as _ # for i18n


class PostView(APIView):
    # HTTP GET method
    def get(self):
        try:
            page = int(request.args.get('page'))
        except Exception:
            page = 1
        postsPagination = PostModel.objects(public=True).paginate(page, 10)
        currentPage = postsPagination.items
        count = len(currentPage)

        posts = list(map(lambda x: x.as_dict(), currentPage))

        return res(posts, 'Success', count, 200)

    # HTTP POST method
    def post(self):
        body = request.get_json()
        body["author"] = self.user

        try:
            post = PostModel(**body).save()
        except ValidationError:
            return res(None, 'One or more required fields are missing', 0, 400)
        except NotUniqueError:
            return res(None, 'Post already exist', 0, 409)

        return res(str(post.id), 'Success', 1, 201)

    def delete(self):
        try:
            id = str(request.args.get('id'))
        except Exception:
            return res(None, 'You should insert an id', 0, 400)

        try:
            post = PostModel.objects(id=id).first()
        except ValidationError:
            post = None

        if post is None:
            return res(None, 'Post does not exist', 0, 404)

        post.delete()
        
        return res(str(post.id), 'Post deleted', 1, 200)