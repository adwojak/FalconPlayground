from flask_restful import Resource


class ExampleResource(Resource):
    def post(self):
        # from flask import request
        # request.content_type
        # request.data
        return {"hello": "worqweld"}
