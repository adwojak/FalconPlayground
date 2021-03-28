from flask import Flask, jsonify
from flask_restful import Api, Resource


class SomeResource(Resource):
    def post(self):
        # from flask import request
        # request.content_type
        # request.data
        return jsonify({"hello": "world"})


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(SomeResource, "/")

    return app
