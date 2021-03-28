from flask import Flask
from flask_restful import Api

from app.constants import MEDIATYPE_XML
from app.libs.representations import output_xml
from app.api.routing import routing


def create_routing(api):
    for resource, routes in routing.items():
        api.add_resource(resource, *routes)


def create_app():
    app = Flask(__name__)
    api = Api(app, default_mediatype=MEDIATYPE_XML)
    api.representations = {MEDIATYPE_XML: output_xml}
    create_routing(api)

    return app
