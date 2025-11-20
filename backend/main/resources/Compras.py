from flask_restful import Resource
from flask import request, jsonify
from .. import  db
from main.models import CompraModel

class Compra(Resource):
    #buusca una compra por id, si no existe devuelve un 404, si existe intenta devolverla como json
    def get(self,id):
        compra = db.session.query(CompraModel).get_or_404(id)
        try:
            return compra.to_json()
        except:
            return '', 404
    
    #busca la compra por id, agarra el json recibido y acxtualiza cada atributo del modelo con setattr
    #devuelve el objeto actualizado y estatus 201
    def put(self,id):
        compra = db.session.query(CompraModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(compra,key,value)
        try:
            db.session.add(compra)
            db.session.commit()
            return compra.to_json(),201
        except:
            return '', 404

class Compras(Resource):
    #busca TODAS las compras devuelve una lista de json de cada una
    def get(self):
        compras = db.session.query(CompraModel).all()
        return jsonify({
            'compras': [compra.to_json() for compra in compras]
        })
        
    #crea una compra
    def post(self):
        compra = CompraModel.from_json(request.get_json())
        db.session.add(compra)
        db.session.commir()
        return compra.to_json(),201