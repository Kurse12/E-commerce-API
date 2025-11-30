from flask import request, Blueprint
from main.models import UsuarioModel
from main import db
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    usuario = UsuarioModel.query.filter_by(email=data.get('email')).first_or_404()

    if usuario.validate_pass(data.get('password')):
        access_token = create_access_token(identity=usuario)

        return {
            'id': usuario.id,
            'email': usuario.email,
            'rol': usuario.rol,
            'access_token': access_token
        }, 200

    return "Incorrect password", 401

@auth.route('/register', methods=['POST'])
def register():
    usuario = UsuarioModel.from_json(request.get_json())
    exists = db.session.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).scalar() is not None 
    if exists:
        return 'Duplicated Email', 409
    else:
        try:
            db.session.add(usuario)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return usuario.to_json(),201