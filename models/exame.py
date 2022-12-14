from typing import Dict
from hashlib import md5

from config.config import db
from models.hospital import Hospital
from models.medico import Medico
from models.doenca import Doenca
from models.paciente import Paciente


class Exame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    resultado = db.Column(db.Boolean)
    hash = db.Column(db.Text)

    hospital_id = db.Column(db.Integer, db.ForeignKey(Hospital.id), nullable=False)
    hospital = db.relationship("Hospital")

    doenca_id = db.Column(db.Integer, db.ForeignKey(Doenca.id))
    doenca = db.relationship("Doenca")

    medico_id = db.Column(db.Integer, db.ForeignKey(Medico.crm), nullable=False)
    medico = db.relationship("Medico")

    paciente_id = db.Column(db.Integer, db.ForeignKey(Paciente.id), nullable=False)
    paciente = db.relationship("Paciente")

    photo_filename = db.Column(db.Text)

    def generate_hash(self) -> None:
        id_str = str(self.id).encode()
        self.hash = md5(id_str).hexdigest()
    
    # expressao da classe no formato json
    def json(self) -> Dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "resultado": self.resultado,
            "hash": self.hash,
            "hospital": self.hospital.json(),
            "hospital_id": self.hospital_id,
            "doenca": self.doenca.json() if self.doenca is not None else None,
            "doenca_id": self.doenca_id,
            "medico": self.medico.json(),
            "medico_id": self.medico_id,
            "paciente": self.paciente.json(),
            "paciente": self.paciente_id,
            "photo_filename": self.photo_filename
        }
