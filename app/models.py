from app import db

class Gentileza(db.Model):
    __tablename__ = 'usuario'

    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String, nullable=False)
    tipo = db.Column(db.Integer, nullable=False)
    latitude = db.Column(db.String, nullable=False)
    longitude = db.Column(db.String, nullable=False)
    nome = db.Column(db.String)

    def __repr__(self):
        return '<gentileza %r>' % (self.nome)