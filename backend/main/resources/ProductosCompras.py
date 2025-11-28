from flask_restful import Resource
from flask import request, jsonify
from .. import  db
from main.models import ProductoCompraModel

class ProductosCompras(Resource):
    def get(self):
    #busca TODAS las productoscompras devuelve una lista de json de cada una
        page = request.args.get("page",1,type=int)
        per_page = request.args.get("per_page",5,type=int)
    
        # Query
        productoscompras = ProductoCompraModel.query.paginate(
        page=page,
        per_page=per_page
        )

        return jsonify({
        "productoscompras": [p.to_json() for p in productoscompras.items],
        "total": productoscompras.total,
        "pages": productoscompras.pages,
        "page": productoscompras.page
        })

    def post(self):
        productocompra = ProductoCompraModel.from_json(request.get_json())
        db.session.add(productocompra)
        db.session.commit()
        return productocompra.to_json(), 201

class ProductoCompra(Resource):
    def get(self, id):
        productocompra = db.session.query(ProductoCompraModel).get_or_404(id)
        try:
            return productocompra.to_json()
        except:
            return '', 404

    def delete(self, id):
        productocompra = db.session.query(ProductoCompraModel).get_or_404(id)
        try:
            db.session.delete(productocompra)
            db.session.commit()
            return '', 204
        except:
            return '', 404
    
    def put(self, id):
        productocompra = db.session.query(ProductoCompraModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(productocompra, key, value)
        try:
            db.session.add(productocompra)
            db.session.commit()
            return productocompra.to_json(), 201
        except:
            return '', 404