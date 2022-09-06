
from flask import Response, request
# from flask_jwt_extended.exceptions import NoAuthorizationError
from flask_restful import Resource
# from mongoengine import FieldDoesNotExist, NotUniqueError, DoesNotExist, InvalidQueryError
from errors import InternalServerError
from core.models.predictionsModel import Perdictions


class Perdictions2Api(Resource):
    def get(self):
        try:
            args = request.args
            print(args)
            perdiction = Perdictions.objects.exclude('id').to_json()
            return Response(perdiction, mimetype='application/json', status=200)
        except Exception:
            raise InternalServerError
