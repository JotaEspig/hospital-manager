from config.config import *
from modelos.paciente import Paciente


def testPaciente():
    r = Paciente(nome="TesteDePaciente", ="N sei")
    db.session.add(r)
    db.session.commit()

    r = db.session.query(Paciente).filter_by(nome="TesteDePaciente").first()
    if r.nome != "TesteDePaciente":
        print("erro")

