
from flask import Response
from flask_restful import Resource
from errors import InternalServerError
from core.models.resolvedPredictionsModel import ResolvedPerdictions


class ResolvePerdictions2Api(Resource):
    def get(self):
        try:
            perdiction = ResolvedPerdictions.objects().exclude('id').to_json()
            return Response(perdiction, mimetype='application/json', status=200)
        except Exception:
            raise InternalServerError
