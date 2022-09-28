import unittest

from config.config import db
from models.hospital import Hospital


class TestHospital(unittest.TestCase):
    def test_hospital(self):
        h1 = Hospital(nome="TesteDeHospital", localizacao="N sei")
        db.session.add(h1)
        db.session.commit()

        h1 = Hospital.query.filter_by(nome="TesteDeHospital").first()
        self.assertEqual(h1.nome, "TesteDeHospital")
        self.assertEqual(h1.localizacao, "N sei")

        db.session.delete(h1)
        db.session.commit()
