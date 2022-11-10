from http.client import OK, BAD_REQUEST, NOT_FOUND

from flask import request, jsonify

from config.config import app, db
from models.doenca import Doenca
from controllers.utils import is_logged


@is_logged
@app.route("/doenca/add", methods=["POST"])
def add_doenca():
    data = dict(request.form)
    if not Doenca.is_data_valid(data):
        return "", BAD_REQUEST

    d = Doenca(**data)
    db.session.add(d)
    db.session.commit()
    return str(d.id), OK

@is_logged
@app.route("/doenca/get_all")
def get_all_doenca():
    doencas = Doenca.query.all()
    return jsonify([doenca.json() for doenca in doencas]), OK


@is_logged
@app.route("/doenca/get")
def get_doenca():
    doenca_id = request.args.get("id")
    if doenca_id is None or doenca_id == "":
        return jsonify(None), BAD_REQUEST

    doenca = Doenca.query.filter_by(id=doenca_id).first()
    return (jsonify(doenca.json()), OK) if doenca is not None else ("", NOT_FOUND)
