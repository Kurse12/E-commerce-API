from .. import db
import datetime as dt


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(60), nullable=False, unique=True, index=True)
    role = db.Column(db.String(45), nullable=False, default="cliente")
    telefono = db.Column(db.Integer, nullable=False)
    fecha_registro = db.Column(db.DateTime, default=dt.datetime.now(), nullable=False)
