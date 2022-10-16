from http.client import FORBIDDEN

from flask import abort
from flask_login import current_user


def is_logged(func):
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            abort(FORBIDDEN)

        return func(*args, **kwargs)
    return wrapper
