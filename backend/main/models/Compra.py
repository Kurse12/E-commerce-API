from .. import db
import datetime as dt


class Compra(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fecha_compra = db.Column(db.DateTime, default=dt.datetime.now, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    usuario = db.relationship(
        "Usuario", back_populates="compras"
    )
    productoscompras = db.relationship(
    "ProductoCompra",
    back_populates="compra",
    cascade="all, delete-orphan",
    single_parent=True
)

    def __repr__(self):
        return f"Fecha compra: {self.fecha_compra}"

    def to_json(self):
        compra_json = {
            "id": self.id,
            "fecha_compra": (
                self.fecha_compra.isoformat() if self.fecha_compra else None
            ),
            "usuario": self.usuario.to_json() if self.usuario else None,
        }
        return compra_json


@staticmethod
def from_json(compra_json):
    id = compra_json.get("id")
    fecha_compra = compra_json.get("fecha_compra")
    usuarioId = compra_json.get("usuarioId")

    if isinstance(fecha_compra, str):
        fecha_compra = dt.datetime.fromisoformat(fecha_compra)

    return Compra(id=id, fecha_compra=fecha_compra, usuarioId=usuarioId)
