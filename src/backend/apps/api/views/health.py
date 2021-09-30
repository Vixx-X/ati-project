from flask_restful import Resource
from backend.apps.api.utils import make_response as res
from flask_wtf.csrf import generate_csrf


class Health(Resource):
    def get(self):
        csrf = generate_csrf()
        return res(data=str(csrf), message="Server started", status=200)
