import unittest

from config.config import *
from models.paciente import Paciente


class TestPaciente(unittest.TestCase):
    def test_paciente(self):
        p1 = Paciente(nome="TesteDePaciente", cpf="000.000.000-00",
            email="a@g.com", telefone="KKKK")
        db.session.add(p1)
        db.session.commit()

        p1 = Paciente.query.filter_by(nome="TesteDePaciente").first()
        self.assertEqual(p1.nome, "TesteDePaciente")
        self.assertEqual(p1.cpf, "000.000.000-00")

        db.session.delete(p1)
        db.session.commit()
    