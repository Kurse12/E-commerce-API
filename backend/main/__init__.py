import os
from flask import Flask
from dotenv import load_dotenv

#Modulo para api-rest
from flask_restful import Api

api = Api()

def create_app():
    app = Flask(__name__)
    
    load_dotenv()
    
    import main.resources as resources
    api.add_resource(resources.ClientesResource, '/clientes')
    api.add_resource(resources.ClienteResource, '/cliente/<id>')
    
    api.init_app(app)
    
    return app

