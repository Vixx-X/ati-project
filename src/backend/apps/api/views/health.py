from flask_restful import Resource
from backend.apps.api.utils import make_response as res

class Health(Resource):
    def get(self):
        return res(message='Server started', status=200)