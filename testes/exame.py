from config.config import *
from modelos.exame import Exame


def test_exame():
    e1 = Exame(nome="TesteDeExame", descricao="N sei", resultado=True)
    db.session.add(e1)
    db.session.commit()

    e1 = Exame.query.filter_by(nome="TesteDeExame").first()
    assert e1.nome == "TesteDeExame"
