from typing import Tuple

from config.config import db, app
from modelos.admin import Admin
from modelos.doenca import Doenca
from modelos.exame import Exame
from modelos.hospital import Hospital
from modelos.paciente import Paciente
from modelos.remedio import Remedio


@app.route("/")
def inicio() -> Tuple[str, int]:
    return 'backend operante', 200


@app.route("/create_tables")
def create_tables() -> Tuple[str, int]:
    db.create_all()
    return "", 200
