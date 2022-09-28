import unittest

from config.config import db
from models.remedio import Remedio


class Remedio(unittest.TestCase):
    def test_remedio(self):
        r1 = Remedio(nome="TesteDeRemedio", descricao="N sei")
        db.session.add(r1)
        db.session.commit()

        r1 = Remedio.query.filter_by(nome="TesteDeRemedio").first()
        self.assertEqual(r1.nome, "TesteDeRemedio")
        self.assertEqual(r1.descricao, "N sei")

        db.session.delete(r1)
        db.session.commit()
    