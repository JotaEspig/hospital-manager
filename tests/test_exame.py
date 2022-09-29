import unittest

from config.config import *
from models.doenca import Doenca
from models.exame import Exame
from models.hospital import Hospital
from models.paciente import Paciente
from models.remedio import Remedio


class TestExame(unittest.TestCase):
    def test_exame(self):
        d1 = Doenca(nome="TesteDeDoenca", sintomas="N sei")
        db.session.add(d1)
        h1 = Hospital(nome="TesteDeHospital", localizacao="N sei")
        db.session.add(h1)
        p1 = Paciente(nome="TesteDePaciente", cpf="000.000.000-00",
            email="a@g.com", telefone="KKKK")
        db.session.add(p1)
        r1 = Remedio(nome="TesteDeRemedio", descricao="N sei")
        db.session.add(r1)
        db.session.commit()
        e1 = Exame(nome="TesteDeExame", descricao="N sei", resultado=True,
            doenca=d1, hospital=h1, paciente=p1, remedio=r1, 
            photo_filename="a.jpg")
        db.session.add(e1)
        db.session.commit()

        e1 = Exame.query.filter_by(nome="TesteDeExame").first()
        self.assertEqual(e1.nome, "TesteDeExame")
        self.assertEqual(e1.doenca.nome, "TesteDeDoenca")
        self.assertEqual(e1.hospital.nome, "TesteDeHospital")
        self.assertEqual(e1.paciente.nome, "TesteDePaciente")
        self.assertEqual(e1.remedio.nome, "TesteDeRemedio")

        db.session.delete(e1)
        db.session.delete(d1)
        db.session.delete(h1)
        db.session.delete(p1)
        db.session.delete(r1)
        db.session.commit()
    