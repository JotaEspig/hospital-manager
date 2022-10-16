from typing import Tuple
import os
from http.client import OK, BAD_REQUEST, NOT_FOUND

from flask import Response, request, jsonify, send_file

from config.config import app, root_path
from models.exame import Exame


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
        return jsonify(None), NOT_FOUND

    if e1.photo_filename == "":
        return jsonify(None), NOT_FOUND
    
    photo_path = os.path.join(root_path, "images/"+e1.photo_filename)
    return send_file(photo_path), OK
