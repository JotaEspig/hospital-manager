from typing import Tuple
from http.client import OK, BAD_REQUEST, NOT_FOUND

from flask import Response, request, jsonify

from config.config import app, db
from models.paciente import Paciente
from controllers.utils import is_logged
from models.utils import is_data_valid


@is_logged
@app.route("/paciente/add", methods=["POST"])
def add_paciente() -> Tuple[Response, int]:
    data = dict(request.form)
    if not is_data_valid(Paciente, data):
        return "", BAD_REQUEST

    h = Paciente(**data)
    db.session.add(h)
    db.session.commit()
    return jsonify(h.json()), OK


@is_logged
@app.route("/paciente/get_all")
def get_all_paciente() -> Tuple[Response, int]:
    pacientes = Paciente.query.all()
    return jsonify([paciente.json() for paciente in pacientes]), OK


@is_logged
@app.route("/paciente/get")
def get_paciente() -> Tuple[Response, int]:
    paciente_id = request.args.get("id")
    if paciente_id is None or paciente_id == "":
        return jsonify(None), BAD_REQUEST

    paciente = Paciente.query.filter_by(id=paciente_id).first()
    return (jsonify(paciente.json()), OK) if paciente is not None else ("", NOT_FOUND)
