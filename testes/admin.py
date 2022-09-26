from config.config import *
from modelos.admin import Admin


def testAdmin():
    hash_de_teste = bcrypt.generate_password_hash("senha") \
                    .decode('utf-8', 'ignore')
    a = Admin(username="TesteDeAdmin", pwhash=hash_de_teste)
    db.session.add(a)
    db.session.commit()

    a = db.session.query(Admin).filter_by(username="TesteDeAdmin").first()
    if a.username != "TesteDeAdmin":
        print("erro")

    if not bcrypt.check_password_hash(a.pwhash, hash_de_teste):
        print("erro")
        
