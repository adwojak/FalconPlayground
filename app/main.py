from simplexml import dumps as simplexml_dumps
from flask import Flask, make_response
from flask_restful import Api, Resource


class SomeResource(Resource):
    def post(self):
        # from flask import request
        # request.content_type
        # request.data
        return {"hello": "world"}


def output_xml(data, code, headers=None):
    # Representations
    """Makes a Flask response with a XML encoded body"""
    resp = make_response(simplexml_dumps({"response": data}), code)
    resp.headers.extend(headers or {})
    return resp


def create_app():
    app = Flask(__name__)
    api = Api(app, default_mediatype="application/xml")
    api.representations = {"application/xml": output_xml}

    api.add_resource(SomeResource, "/")

    return app
