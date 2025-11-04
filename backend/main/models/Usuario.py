from .. import db
import datetime as dt


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True, index=True)
    rol = db.Column(db.String(45), nullable=False, default="cliente")
    telefono = db.Column(db.Integer, nullable=False)
    fecha_registro = db.Column(db.DateTime, default=dt.datetime.now(), nullable=False)
    
    def __repr__(self):
        return f'{self.id},{self.nombre}, {self.apellido}, {self.rol}, {self.telefono},{self.fecha_registro}'
    
    def to_json(self):
        usuario_json = {
            'id': self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email":self.email,
            "rol": self.rol,
            "telefono": self.telefono,
            "fecha_registro": str(self.fecha_registro)
        }
        return usuario_json
    
    @staticmethod
    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        email = usuario_json.get('email')
        rol =  usuario_json.get('rol')
        telefono = usuario_json.get('telefono')
        fecha_registro = usuario_json.get('fecha_registro')
        
        return Usuario(
            id = id,
            nombre = nombre,
            apellido = apellido,
            email = email,
            rol = rol,
            telefono = telefono,
            fecha_registro = fecha_registro
        )