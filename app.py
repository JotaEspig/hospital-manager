from config.config import *
from modelos.admin import Admin
from modelos.doenca import Doenca
from modelos.exame import Exame
from modelos.hospital import Hospital
from modelos.paciente import Paciente
from modelos.remedio import Remedio

@app.route("/")
def inicio():
    return 'backend operante'

@app.route("/create_tables")
def create_tables():
    db.create_all()
    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
