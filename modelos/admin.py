from config.config import *


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(254), nullable=False)
    pwhash = db.Column(db.Text, nullable=False)

    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "username": self.username
        }