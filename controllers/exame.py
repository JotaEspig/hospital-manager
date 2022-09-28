from flask import request, jsonify

from config.config import app
from models.exame import Exame


@app.route("/exame/get")
def get_exame():
    exame_hash = request.args.get("hash")
    if exame_hash is None or exame_hash == "":
        return jsonify(None), 400

    exame = Exame.query.filter_by(hash=exame_hash).first()
    return jsonify(exame), 200 if exame is not None else 404
