from app.libs.resources import XmlResource


class ExampleResource(XmlResource):
    def post(self):
        return {"hello": "worqweld"}
