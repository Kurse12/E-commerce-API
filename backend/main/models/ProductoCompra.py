from .. import db

class ProductoCompra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    producto = db.relationship('Producto', back_populates="productoscompras")
    
    compra_id = db.Column(db.Integer, db.ForeignKey('compra.id'), nullable=False)
    compra = db.relationship('Compra', back_populates="productoscompras", single_parent=True)
    
    def __repr__(self):
        return f'Producto-Compras: {self.producto.to_json()}'
    
    def to_json(self):
        return {
            'id': self.id,
            'producto': self.producto.to_json(),
            'compra': self.compra.to_json()
        }
    
    @staticmethod
    def from_json(productocompra_json):
        id = productocompra_json.get('id')
        productoId = productocompra_json.get('productoId')
        compraId = productocompra_json.get('compraId')
        return ProductoCompra(
            id=id,
            producto_id=productoId,
            compra_id=compraId
        )
