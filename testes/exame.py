from config.config import *
from modelos.exame import Exame


def testExame():
    r = Exame(nome="TesteDeExame", descricao="N sei", resultado=True)
    db.session.add(r)
    db.session.commit()

    r = db.session.query(Exame).filter_by(nome="TesteDeExame").first()
    if r.nome != "TesteDeExame":
        print("erro")

