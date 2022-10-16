from http.client import OK, BAD_REQUEST, UNAUTHORIZED, NOT_FOUND

from flask import abort, request
from flask_login import current_user, login_user, logout_user

from config.config import app
from models.admin import Admin


@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    if "username" not in dados or "password" not in dados:
        abort(BAD_REQUEST)
    
    a = Admin.query.filter_by(username=dados["username"]).first()
    if a is None:
        abort(NOT_FOUND)

    is_valid = a.validate_password(dados["password"])
    if not is_valid:
        abort(UNAUTHORIZED)

    if current_user.is_authenticated:
        logout_user(a)
    login_user(a)

    return "", OK
