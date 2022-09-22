from config.config import *

class Doenca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    sintomas = db.Column(db.String(254))

    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "sintomas": self.sintomas
        }