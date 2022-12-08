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
        exit(0)

    a = models.admin.Admin(username="admin", pwhash="admin")
    db.session.add(a)
    db.session.commit()
    if models.doenca.Doenca.query.filter_by(nome="covid").first() != None:
        exit(0)
    d = models.doenca.Doenca(nome="covid", sintomas="dor")
    db.session.add(d)
    db.session.commit()
    return "", OK
