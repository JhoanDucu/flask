import enum

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Cancion(db.Model):
    __tablename__ = 'Cancion'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))

    def __rep__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.minutos, self.segundos, self.interprete)


class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3


class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(128))
    contrasena = db.Column(db.Integer)


class Album(db.Model):
    __tablename__ = 'Album'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    ano = db.Column(db.Integer)
    descripcion = db.Column(db.Integer)
    medio = Medio(Medio.DISCO) # ES UN EJEMPLO PARA QUE TENGA PARAMETROS


