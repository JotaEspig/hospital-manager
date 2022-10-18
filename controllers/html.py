from http.client import OK
from typing import Tuple

from flask import send_from_directory, Response

from config.config import app


@app.route("/frontend/<string:path>")
def login_page(path: str) -> Tuple[Response, int]:
    return send_from_directory('../frontend', path), OK
