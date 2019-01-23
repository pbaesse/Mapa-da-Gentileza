from flask import jsonify
import datetime
import json


def default_parser(obj):
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    elif type(obj) == datetime:
        return obj.isoformat()
    else:
        return str(obj)


def make_response_message(message):
    response = {}
    response['message'] = message
    return json.dumps(response)

"""
def to_dict(obj):
    if hasattr(obj, '__dict__'):
        obj = obj.__dict__

    if isinstance(obj, dict):
        return { k:to_dict(v) for k, v in obj.items() }
    elif isinstance(obj, list) or isinstance(obj, tuple):
        return [to_dict(e) for e in obj]
    else:
        return obj
"""

def convert_object_to_json(obj):
    return json.dumps(obj, default=default_parser)
