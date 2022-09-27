from config.config import db
from sqlalchemy.ext.hybrid import hybrid_property


class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    _email = db.Column(db.String(254), nullable=False)
    telefone = db.Column(db.String(254), nullable=False)

    @hybrid_property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if "@" not in value:
            raise Exception("precisa conter @")

        self._email = value
    
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
            "email": self.email,
            "telefone": self.telefone
        }
