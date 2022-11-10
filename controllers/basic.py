from typing import Tuple
from http.client import OK

from flask import request

from config.config import db, app
import models


@app.route("/")
def inicio() -> Tuple[str, int]:
    return 'JOTA: <a href="http://'+request.host+'/frontend/login_adm.html">'+ \
        request.host+'</a>: backend operante '+ \
        '<a href="https://github.com/JotaEspig/hospital-manager">repositório</a>',OK


@app.route("/create_tables")
def create_tables() -> Tuple[str, int]:
    db.create_all()

    if models.admin.Admin.query.filter_by(username="admin").first() != None:
        return "", OK

    a = models.admin.Admin(username="admin", pwhash="admin")
    db.session.add(a)
    db.session.commit()
    return "", OK
