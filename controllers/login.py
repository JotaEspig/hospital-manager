from flask import abort, request
from flask_login import current_user, login_user, logout_user

from config.config import app
from models.admin import Admin


@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    if "username" not in dados or "password" not in dados:
        abort(400) # BadRequest
    
    a = Admin.query.filter_by(username=dados["username"]).first()
    if a is None:
        abort(404)

    isValid = a.validate_password(dados["password"])
    if not isValid:
        abort(403)

    if current_user.is_authenticated:
        logout_user(a)
    login_user(a)

    return "", 200
