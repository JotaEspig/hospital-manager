from typing import Tuple
from http.client import OK

from config.config import db, app
import models


@app.route("/")
def inicio() -> Tuple[str, int]:
    return 'backend operante', OK


@app.route("/create_tables")
def create_tables() -> Tuple[str, int]:
    db.create_all()

    if models.admin.Admin.query.filter_by(username="admin").first() != None:
        return "", OK

    a = models.admin.Admin(username="admin", pwhash="admin")
    db.session.add(a)
    db.session.commit()
    return "", OK
