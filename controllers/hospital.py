from http.client import OK, BAD_REQUEST, NOT_FOUND

from flask import request, jsonify

from config.config import app
from models.hospital import Hospital
from controllers.utils import is_logged


@is_logged
@app.route("/hospital/get_all")
def get_all_hospital():
    hospitals = Hospital.query.all()
    return jsonify([hospital.json() for hospital in hospitals]), OK


@is_logged
@app.route("/hospital/get")
def get_hospital():
    hospital_id = request.args.get("id")
    if hospital_id is None or hospital_id == "":
        return jsonify(None), BAD_REQUEST

    hospital = Hospital.query.filter_by(id=hospital_id).first()
    return (jsonify(hospital.json()), OK) if hospital is not None else ("", NOT_FOUND)
