import unittest

from config.config import *
from models.exame import Exame
from models.hospital import Hospital
from models.paciente import Paciente
from models.medico import Medico


class TestExame(unittest.TestCase):
    def test_exame(self):
        h1 = Hospital(nome="TesteDeHospital", localizacao="N sei")
        db.session.add(h1)
        p1 = Paciente(nome="TesteDePaciente", cpf="000.000.000-00",
            email="a@g.com", telefone="KKKK")
        db.session.add(p1)
        r1 = Medico(nome="TesteDeMedico")
        db.session.add(r1)
        db.session.commit()
        e1 = Exame(nome="TesteDeExame", descricao="N sei", resultado=True, 
            hospital=h1, paciente=p1, medico=r1, photo_filename="test_image.jpg")
        db.session.add(e1)
        db.session.commit()

        e1 = Exame.query.filter_by(nome="TesteDeExame").first()
        e1.generate_hash()
        db.session.commit()

        self.assertEqual(e1.nome, "TesteDeExame")
        self.assertEqual(e1.hospital.nome, "TesteDeHospital")
        self.assertEqual(e1.paciente.nome, "TesteDePaciente")
        self.assertEqual(e1.medico.nome, "TesteDeMedico")

        db.session.delete(e1)
        db.session.delete(h1)
        db.session.delete(p1)
        db.session.delete(r1)
        db.session.commit()
    