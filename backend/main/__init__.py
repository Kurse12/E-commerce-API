import os
from flask import Flask
from dotenv import load_dotenv

#Modulo para api-rest
from flask_restful import Api

#sqlalchemy
from flask_sqlalchemy import SQLAlchemy

#jwt
from flask_jwt_extended import JWTManager

api = Api()

db = SQLAlchemy()

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    load_dotenv()
    
    #config db
    PATH = os.getenv("DATABASE_PATH")
    DB_NAME = os.getenv("DATABASE_NAME")
    
    if not os.path.exists(f'{PATH}/{DB_NAME}'):
        os.chdir(f'{PATH}')
        file = os.open(f'{DB_NAME}', os.O_CREAT)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{PATH}{DB_NAME}'
    db.init_app(app)
    
    import main.resources as resources
    api.add_resource(resources.ClientesResource, '/clientes')
    api.add_resource(resources.ClienteResource, '/cliente/<id>')
    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<id>')
    api.add_resource(resources.ComprasResource, '/compras')
    api.add_resource(resources.CompraResource, '/compra/<id>')
    api.add_resource(resources.ProductosResource, '/productos')
    api.add_resource(resources.ProductoResource, '/producto/<id>')
    api.add_resource(resources.ProductosComprasResource, '/productos-compras')
    api.add_resource(resources.ProductoCompraResource, '/producto-compra/<id>')
    
    api.init_app(app)
    
    #Configuracion jwt
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES"))
    jwt.init_app(app)
    
    from main.auth import decorators 
    from main.auth import routes
    app.register_blueprint(routes.auth )
    
    return app

