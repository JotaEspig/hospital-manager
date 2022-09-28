import unittest

from config.config import db
from models.admin import Admin


class TestAdmin(unittest.TestCase):
    def test_admin(self):
        a1 = Admin(username="TesteDeAdmin", pwhash="senha")
        db.session.add(a1)
        db.session.commit()

        a1 = Admin.query.filter_by(username="TesteDeAdmin").first()
        self.assertEqual(a1.username, "TesteDeAdmin")
        self.assertEqual(a1.validate_password("senha"), True)
        self.assertEqual(a1.validate_password("senha1"), False)

        db.session.delete(a1)
        db.session.commit()
