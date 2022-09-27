from config.config import db
from models.remedio import Remedio


def test_remedio():
    r1 = Remedio(nome="TesteDeRemedio", descricao="N sei")
    db.session.add(r1)
    db.session.commit()

    r1 = Remedio.query.filter_by(nome="TesteDeRemedio").first()
    assert r1.nome == "TesteDeRemedio"

    db.session.delete(r1)
    db.session.commit()
    