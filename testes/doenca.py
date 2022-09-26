from config.config import *
from modelos.doenca import Doenca


def testDoenca():
    r = Doenca(nome="TesteDeDoenca", sintomas="N sei")
    db.session.add(r)
    db.session.commit()

    r = db.session.query(Doenca).filter_by(nome="TesteDeDoenca").first()
    if r.nome != "TesteDeDoenca":
        print("erro")

