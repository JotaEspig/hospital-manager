from config.config import db
from modelos.doenca import Doenca


def test_doenca():
    d1 = Doenca(nome="TesteDeDoenca", sintomas="N sei")
    db.session.add(d1)
    db.session.commit()

    d1 = Doenca.query.filter_by(nome="TesteDeDoenca").first()
    assert d1.nome == "TesteDeDoenca"
    assert d1.sintomas == "N sei" # :)

    db.session.delete(d1)
    db.session.commit()
