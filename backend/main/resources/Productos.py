from math import prod
from flask_restful import Resource
from flask import request, jsonify
from .. import  db
from main.models import ProductoModel

class Producto(Resource):
    def get(self, id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        try:
            return producto.to_json()
        except:
            return 'Recurso no encontrado', 404
        
        
    def put(self,id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(producto, key, value)
            
        try:
            db.session.add(producto)
        except:
            return "", 404
        
    def delete(self,id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        try:
            db.session.delete(producto)
        except:
            return '', 404

class Productos(Resource):
    
    def get(self):
        productos = db.session.query(ProductoModel).all()
        
        return jsonify({
            'productos': [producto.to_json() for producto in productos]
        })
    
    def post(self):
        producto = ProductoModel.from_json(request.get_json())
        db.session.add(producto)
        db.session.commit()
        
        return producto.to_json()
    