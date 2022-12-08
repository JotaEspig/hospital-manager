from typing import Tuple
from http.client import OK, BAD_REQUEST, NOT_FOUND

from flask import Response, request, jsonify

from config.config import app, db
from models.medico import Medico
from models.utils import is_data_valid
from controllers.utils import is_logged


@is_logged
@app.route("/medico/add", methods=["POST"])
def add_medico() -> Tuple[Response, int]:
    data = dict(request.form)
    if not is_data_valid(Medico, data):
        return "", BAD_REQUEST

    m = Medico(**data)
    db.session.add(m)
    db.session.commit()
    return jsonify(m.json()), OK


@is_logged
@app.route("/medico/get_all")
def get_all_medico() -> Tuple[Response, int]:
    medicos = Medico.query.all()
    return jsonify([medico.json() for medico in medicos]), OK


@is_logged
@app.route("/medico/get")
def get_medico() -> Tuple[Response, int]:
    medico_id = request.args.get("id")
    if medico_id is None or medico_id == "":
        return jsonify(None), BAD_REQUEST

    medico = Medico.query.filter_by(id=medico_id).first()
    return (jsonify(medico.json()), OK) if medico is not None else ("", NOT_FOUND)
