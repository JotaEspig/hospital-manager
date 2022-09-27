import unittest

from config.config import *
from models.exame import Exame


class TestExame(unittest.TestCase):
    def test_exame(self):
        e1 = Exame(nome="TesteDeExame", descricao="N sei", resultado=True)
        db.session.add(e1)
        db.session.commit()

        e1 = Exame.query.filter_by(nome="TesteDeExame").first()
        self.assertEqual(e1.nome, "TesteDeExame")

        db.session.delete(e1)
        db.session.commit()
    