from functools import wraps

from flask import request
from app.controllers.auth_controller import AuthController


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("X-API-KEY")
        
        data, status = AuthController.auth_token_is_valid(token=token)
        auth_token = data.get('data')

        if not auth_token:
            return data, status

        return f(*args, **kwargs)

    return decorated
