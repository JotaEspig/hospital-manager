from typing import Dict

from config.config import db
from modelos.hospital import Hospital
from modelos.remedio import Remedio
from modelos.doenca import Doenca
from modelos.paciente import Paciente


class Exame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    resultado = db.Column(db.Boolean)
    hash = db.Column(db.Text, nullable=True)

    hospital_id = db.Column(db.Integer, db.ForeignKey(Hospital.id))
    hospital = db.relationship("Hospital")

    doenca_id = db.Column(db.Integer, db.ForeignKey(Doenca.id))
    doenca = db.relationship("Doenca")

    remedio_id = db.Column(db.Integer, db.ForeignKey(Remedio.id))
    remedio = db.relationship("Remedio")

    paciente_id = db.Column(db.Integer, db.ForeignKey(Paciente.id))
    paciente = db.relationship("Paciente")
    #imagem = 
    
    # expressao da classe no formato json
    def json(self) -> Dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "resultado": self.resultado,
            "hash": self.hash,
            "hospital": self.hospital,
            "doenca": self.doenca,
            "remedio": self.remedio,
            "paciente": self.paciente
        }
