from config.config import db
from models.hospital import Hospital


def test_hospital():
    h1 = Hospital(nome="TesteDeHospital", localizacao="N sei")
    db.session.add(h1)
    db.session.commit()

    h1 = Hospital.query.filter_by(nome="TesteDeHospital").first()
    assert h1.nome == "TesteDeHospital"
    assert h1.localizacao == "N sei"

    db.session.delete(h1)
    db.session.commit()
