from config.config import *
from modelos.paciente import Paciente


def test_paciente():
    p1 = Paciente(nome="TesteDePaciente", cpf="000.000.000-00", email="a@g.com", telefone="KKKK")
    db.session.add(p1)
    db.session.commit()

    p1 = Paciente.query.filter_by(nome="TesteDePaciente").first()
    assert p1.nome == "TesteDePaciente"
    assert p1.cpf == "000.000.000-00"

    db.session.delete(p1)
    db.session.commit()
    