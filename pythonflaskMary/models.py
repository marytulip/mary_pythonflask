from database import db

class Alunos(db.Model):
    __tablename__ = "Alunos"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    matricula = db.Column(db.String(50))
    idade = db.Column(db.Integer)

    def __init__(self, nome, matricula, idade):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade

    def __repr__(self):
        return "<Alunos {}>".format(self.nome)