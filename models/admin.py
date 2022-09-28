from typing import Dict

from sqlalchemy.ext.hybrid import hybrid_property

from config.config import db, bcrypt


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(254), nullable=False)
    _pwhash = db.Column(db.Text, nullable=False)

    @hybrid_property
    def pwhash(self) -> str:
        return self._pwhash

    @pwhash.setter
    def pwhash(self, value: str) -> None:
        self._pwhash = bcrypt.generate_password_hash(value) \
            .decode('utf-8', 'ignore')

    def validate_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self._pwhash, password)

    # expressao da classe no formato json
    def json(self) -> Dict:
        return {
            "id": self.id,
            "username": self.username
        }
