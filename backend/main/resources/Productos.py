from math import prod
from flask_restful import Resource
from flask import request, jsonify
from .. import  db
from main.models import ProductoModel

class Producto(Resource):
    #busca el producto por id, si existe devuelve el json
    def get(self, id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        try:
            return producto.to_json()
        except:
            return 'Recurso no encontrado', 404
        
    # busca el producto por id, lee el json y actualiza cada atributo del modelo
    def put(self,id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(producto, key, value)
            
        try:
            db.session.add(producto)
            db.session.commit()
        except:
            return "", 404
    
    #busca el producto por id, elimina de la bd con delete
    def delete(self,id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        try:
            db.session.delete(producto)
            db.session.commit()
        except:
            return '', 404

class Productos(Resource):
    #trae todos los productos
    def get(self):
        productos = db.session.query(ProductoModel).all()
        
        return jsonify({
            'productos': [producto.to_json() for producto in productos]
        })
        
        
    #agrega un producto
    def post(self):
        producto = ProductoModel.from_json(request.get_json())
        db.session.add(producto)
        db.session.commit()
        
        return producto.to_json()
    