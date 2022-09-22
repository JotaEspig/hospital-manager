from config.config import *

class Exame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    resultado = db.Column(db.Boolean)
    #imagem = 
    
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "resultado": self.resultado

        }