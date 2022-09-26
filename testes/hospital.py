from config.config import *
from modelos.hospital import Hospital


def testHospital():
    r = Hospital(nome="TesteDeHospital", localizacao="N sei")
    db.session.add(r)
    db.session.commit()

    r = db.session.query(Hospital).filter_by(nome="TesteDeHospital").first()
    if r.nome != "TesteDeHospital":
        print("erro")

