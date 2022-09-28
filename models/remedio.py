from typing import Dict

from config.config import db

class Remedio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    descricao = db.Column(db.String(254), nullable=False)
    
    # expressao da classe no formato json
    def json(self) -> Dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao
        }