from config.config import *

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(254), nullable=False)
    telefone = db.Column(db.String(254), nullable=False)
    
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
            "email": self.email,
            "telefone": self.telefone
        }