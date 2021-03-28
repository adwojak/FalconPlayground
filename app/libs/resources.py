from flask import request
from flask_restful import Resource
from simplexml import loads


class BaseResource(Resource):
    def __init__(self):
        self.request = request


class XmlResource(BaseResource):
    def __init__(self):
        super().__init__()
        self.request_data = loads(request.data)
