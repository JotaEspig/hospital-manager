from typing import Dict

from config.config import db

class Hospital(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    localizacao = db.Column(db.String(254), nullable=False)
    
    # expressao da classe no formato json
    def json(self) -> Dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "localizacao": self.localizacao
        }
