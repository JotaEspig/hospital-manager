from typing import Tuple

from config.config import db, app
import models


@app.route("/")
def inicio() -> Tuple[str, int]:
    return 'backend operante', 200


@app.route("/create_tables")
def create_tables() -> Tuple[str, int]:
    db.create_all()

    if models.admin.Admin.query.filter_by(username="admin").first() != None:
        exit(0)

    a = models.admin.Admin(username="admin", pwhash="admin")
    db.session.add(a)
    db.session.commit()
    return "", 200
