import unittest

from config.config import db
from models.medico import Medico


class TestMedico(unittest.TestCase):
    def test_medico(self):
        m1 = Medico(nome="TesteDeMedico")
        db.session.add(m1)
        db.session.commit()

        m1 = Medico.query.filter_by(nome="TesteDeMedico").first()
        self.assertEqual(m1.nome, "TesteDeMedico")

        db.session.delete(m1)
        db.session.commit()
    