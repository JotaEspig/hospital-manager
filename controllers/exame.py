from typing import Tuple
import os
from http.client import OK, BAD_REQUEST, NOT_FOUND, INTERNAL_SERVER_ERROR

from flask import Response, request, jsonify, send_file

from config.config import app, db, root_path
from models.exame import Exame
from models.utils import is_data_valid
from controllers.utils import is_logged


@is_logged
@app.route("/exame/add", methods=["POST"])
def add_exame() -> Tuple[Response, int]:
    data = dict(request.form)
    if not is_data_valid(Exame, data):
        return "", BAD_REQUEST

    e = Exame(**data)
    db.session.add(e)
    e.generate_hash()
    db.session.commit()
    return e.hash, OK

@is_logged
@app.route("/exame/save_image", methods=["PUT"])
def save_image() -> Tuple[Response, int]:
    try:
        file_val = request.files["foto"]
        filename = file_val.filename
        filepath = os.path.join(root_path, 'images/'+filename)
        file_val.save(filepath)
        return "", OK
    except:
        return "", INTERNAL_SERVER_ERROR

@is_logged
@app.route("/exame/associate_image", methods=["PUT"])
def associate_image() -> Tuple[Response, int]:
    data = dict(request.form)
    e = Exame.query.filter_by(hash=data["hash"]).first()
    if e is None:
        return "", NOT_FOUND

    e.photo_filename = data["filename"]
    db.session.commit()
    return "", OK

@app.route("/exame/get")
def get_exame() -> Tuple[Response, int]:
    exame_hash = request.args.get("hash")
    if exame_hash is None or exame_hash == "":
        return jsonify(None), BAD_REQUEST

    exame = Exame.query.filter_by(hash=exame_hash).first()
    return (jsonify(exame.json()), OK) if exame is not None else ("", NOT_FOUND)


@app.route("/exame/get_image")
def get_exame_image() -> Tuple[Response, int]:
    exame_hash = request.args.get("hash")
    e1 = Exame.query.filter_by(hash=exame_hash). \
        with_entities(Exame.id, Exame.photo_filename).first()
    if e1 is None:
        return "", NOT_FOUND

    if e1.photo_filename == "":
        return "", NOT_FOUND

    photo_path = os.path.join(root_path, "images/"+e1.photo_filename)
    return send_file(photo_path), OK
