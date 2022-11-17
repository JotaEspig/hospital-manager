from typing import Dict

from config.config import db


class Doenca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    sintomas = db.Column(db.String(254))

    # expressao da classe no formato json
    def json(self) -> Dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "sintomas": self.sintomas
        }
