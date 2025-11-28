from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuarioModel

class Usuario(Resource):
    def get(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        return usuario.to_json()
    
    def delete(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return '', 204
    
    def put(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(usuario, key, value)
        db.session.add(usuario)
        db.session.commit()

class Usuarios(Resource):
    def get(self):
    #busca TODAS las usuarios devuelve una lista de json de cada una
        page = request.args.get("page",1,type=int)
        per_page = request.args.get("per_page",5,type=int)
    
        # Query
        usuarios = UsuarioModel.query.paginate(
        page=page,
        per_page=per_page
        )

        return jsonify({
        "usuarios": [p.to_json() for p in usuarios.items],
        "total": usuarios.total,
        "pages": usuarios.pages,
        "page": usuarios.page
        })