from .. import jwt
from flask_jwt_extended import verify_jwt_in_request, get_jwt


def role_required(roles):
    def decorator(function):
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            #obtenemos los claims (peticiones), que estan dentro del jwt
            claims = get_jwt()
            #verifico que el rol sea el permitido
            
            if claims['sub']['rol'] in roles:
                return function(*args, **kwargs)
            else:
                return 'Rol not allowed', 403
        return wrapper
    return decorator

@jwt.user_identity_loader
def user_identity_lookup(usuario):
    return {
        'usuarioid': usuario.id,
        'rol': usuario.rol
    }
    
@jwt.additional_claims_loader
def add_claims_to_access_token(usuario):
    claims = {
        'id': usuario.id,
        'rol': usuario.rol,
        'email': usuario.email
    }