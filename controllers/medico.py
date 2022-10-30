from http.client import OK, BAD_REQUEST, NOT_FOUND

from flask import request, jsonify

from config.config import app
from models.medico import Medico
from controllers.utils import is_logged


@is_logged
@app.route("/medico/get_all")
def get_all_medico():
    medicos = Medico.query.all()
    return jsonify([medico.json() for medico in medicos]), OK


@is_logged
@app.route("/medico/get")
def get_medico():
    medico_id = request.args.get("id")
    if medico_id is None or medico_id == "":
        return jsonify(None), BAD_REQUEST

    medico = Medico.query.filter_by(id=medico_id).first()
    return (jsonify(medico.json()), OK) if medico is not None else ("", NOT_FOUND)
