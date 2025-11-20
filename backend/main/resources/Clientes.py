from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import UsuarioModel

clientes = [
    {
        "id": 1,
        "nombre": "Valentin",
        "apellido": "Corallo"
    },
    {
        "id": 2,
        "nombre": "Mia",
        "apellido": "Mendoza"
    }
]

class Clientes(Resource):
    
    def get(self):
        clientes = db.session.query(UsuarioModel).filter(UsuarioModel.role == 'cliente').all()
        return jsonify({
            'clientes': [clientes.to_json() for cliente in clientes]
        })
        
    def post(self):
        cliente = UsuarioModel.from_json(request.get_json())
        cliente.role = 'cliente'
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_json(), 201
        
        
class Cliente(Resource):
    def get(self, id):
        cliente = db.session.query(UsuarioModel).get_or_404(id)
        if cliente.role == 'cliente':
            return cliente.to_json()
        else:
            return '', 404
        
    def delete(self, id):
        cliente = db.session.query(UsuarioModel).get_or_404(id)
        try:
            db.session.delete(cliente)
            db.session.commit()
            return '',204
        except:
            return '',404
        
    def put(self, id):
        cliente = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(cliente, key, value)
        try:
            db.session.add(cliente)
            db.session.commit()
            return cliente.to_json(),201
        except:
            return '', 404