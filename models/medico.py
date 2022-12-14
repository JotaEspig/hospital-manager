from typing import Dict

from config.config import db

class Medico(db.Model):
    crm = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    
    # expressao da classe no formato json
    def json(self) -> Dict:
        return {
            "crm": self.crm,
            "nome": self.nome
        }
