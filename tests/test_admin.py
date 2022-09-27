import unittest

from config.config import db, bcrypt
from models.admin import Admin


class TestAdmin(unittest.TestCase):
    def test_admin(self):
        hash_de_teste = bcrypt.generate_password_hash("senha") \
                        .decode('utf-8', 'ignore')
        a1 = Admin(username="TesteDeAdmin", pwhash=hash_de_teste)
        db.session.add(a1)
        db.session.commit()

        a1 = Admin.query.filter_by(username="TesteDeAdmin").first()
        assert a1.username == "TesteDeAdmin"
        assert bcrypt.check_password_hash(a1.pwhash, "senha")

        db.session.delete(a1)
        db.session.commit()
