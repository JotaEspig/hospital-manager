from http.client import OK, BAD_REQUEST, UNAUTHORIZED, NOT_FOUND, CONFLICT

from flask import abort, request
from flask_login import current_user, login_user, logout_user

from config.config import app, db
from models.admin import Admin


@app.route("/login", methods=["POST"])
def login():
    dados = dict(request.form)
    if "username" not in dados or "password" not in dados:
        abort(BAD_REQUEST)
    
    a = Admin.query.filter_by(username=dados["username"]).first()
    if a is None:
        abort(UNAUTHORIZED)

    is_valid = a.validate_password(dados["password"])
    if not is_valid:
        abort(UNAUTHORIZED)

    if current_user.is_authenticated:
        logout_user()
    login_user(a)

    return "", OK

@app.route("/signup", methods=["POST"])
def signup():
    dados = dict(request.form)
    a = Admin.query.filter_by(username=dados["username"]).first()
    if a is not None:
        return "", CONFLICT

    try:
        a = Admin(username=dados["username"], pwhash=dados["password"])
        db.session.add(a)
        db.session.commit()
        return "", OK
    except:
        return "", BAD_REQUEST
