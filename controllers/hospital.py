from typing import Tuple
from http.client import OK, BAD_REQUEST, NOT_FOUND

from flask import Response, request, jsonify

from config.config import app, db
from models.hospital import Hospital
from models.utils import is_data_valid
from controllers.utils import is_logged


@is_logged
@app.route("/hospital/add", methods=["POST"])
def add_hospital() -> Tuple[Response, int]:
    data = dict(request.form)
    if not is_data_valid(Hospital, data):
        return "", BAD_REQUEST

    h = Hospital(**data)
    db.session.add(h)
    db.session.commit()
    return jsonify(h.json()), OK


@is_logged
@app.route("/hospital/get_all")
def get_all_hospital() -> Tuple[Response, int]:
    hospitals = Hospital.query.all()
    return jsonify([hospital.json() for hospital in hospitals]), OK


@is_logged
@app.route("/hospital/get")
def get_hospital() -> Tuple[Response, int]:
    hospital_id = request.args.get("id")
    if hospital_id is None or hospital_id == "":
        return jsonify(None), BAD_REQUEST

    hospital = Hospital.query.filter_by(id=hospital_id).first()
    return (jsonify(hospital.json()), OK) if hospital is not None else ("", NOT_FOUND)
