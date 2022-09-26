from config.config import *
from modelos.remedio import Remedio


def testRemedio():
    r = Remedio(nome="TesteDeRemedio", descricao="N sei")
    db.session.add(r)
    db.session.commit()

    r = db.session.query(Remedio).filter_by(nome="TesteDeRemedio").first()
    if r.nome != "TesteDeRemedio":
        print("erro")

