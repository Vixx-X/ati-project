"""
Views for comment module
"""

from flask import request
from mongoengine.errors import ValidationError, NotUniqueError
from backend.apps.api.views.utils import APIView
from backend.apps.comments.models import Comment as CommentModel
from backend.apps.posts.models import Post
from backend.apps.api.utils import makeRespone as res
from flask_babel import gettext as _ # for i18n

from backend.apps.user.models import User 

class CommentView(APIView):
    # HTTP GET method
    def get(self, postID):
        try:
            post = Post.objects(id=postID).first()
        except ValidationError:
            post = None

        if post is None:
            return res(None, 'Post does not exist', 0, 404)

        try:
            page = int(request.args.get('page'))
        except Exception:
            page = 1
        
        commentPagination = CommentModel.objects(post=post["id"]).paginate(page, 10)
        currentPage = commentPagination.items

        count = len(currentPage)

        comments = list(map(lambda x: x.as_dict(), currentPage))

        return res(comments, 'Success', count, 200)

    # HTTP POST method
    def post(self, postID):
        try:
            post = Post.objects(id=postID).first()
        except ValidationError:
            post = None

        if post is None:
            return res(None, 'Post does not exist', 0, 404)
        
        body = request.get_json()
        body["author"] = self.user
        body["post"] = post

        try:
            comment = CommentModel(**body).save()
        except ValidationError:
            return res(None, 'One or more required fields are missing', 0, 400)
        except NotUniqueError:
            return res(None, 'Comment already exist', 0, 409)

        return res(str(comment.id), 'Success', 1, 201)

    def delete(self, postID):
        try:
            post = Post.objects(id=postID).first()
        except ValidationError:
            post = None

        if post is None:
            return res(None, 'Post does not exist', 0, 404)

        try:
            id = str(request.args.get('id'))
        except Exception:
            return res(None, 'You should insert an id', 0, 400)

        try:
            comment = CommentModel.objects(id=id).first()
        except ValidationError:
            comment = None
        
        if comment is None:
            return res(None, 'Comnent does not exist', 0, 404)

        comment.delete()

        return res(str(comment.id), 'Success', 1, 200)
