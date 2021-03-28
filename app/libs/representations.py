from simplexml import dumps as simplexml_dumps
from flask import make_response


def output_xml(data, code, headers=None):
    """Makes a Flask response with a XML encoded body"""
    resp = make_response(simplexml_dumps({"response": data}), code)
    resp.headers.extend(headers or {})
    return resp
