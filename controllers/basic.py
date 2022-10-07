from typing import Tuple

from config.config import db, app
from models.admin import Admin
from models.doenca import Doenca
from models.exame import Exame
from models.hospital import Hospital
from models.paciente import Paciente
from models.medico import Medico


@app.route("/")
def inicio() -> Tuple[str, int]:
    return 'backend operante', 200


@app.route("/create_tables")
def create_tables() -> Tuple[str, int]:
    db.create_all()
    return "", 200
