# pizza_route.py

from flask import Blueprint, make_response, jsonify
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_restful import Resource, Api, abort, reqparse
from flask_marshmallow import Marshmallow

from models import Pizza, db

pizza_bp = Blueprint('pizza_bp', __name__)
ma = Marshmallow(pizza_bp)
api = Api(pizza_bp)


post_args = reqparse.RequestParser()
post_args.add_argument('id', type=int, required=True)
post_args.add_argument('name', type=str)
post_args.add_argument('ingredients', type=str)

patch_args = reqparse.RequestParser()
patch_args.add_argument('id', type=int)
patch_args.add_argument('name', type=str)
patch_args.add_argument('ingredients', type=int)


class PizzaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Pizza


pizzas_schema = PizzaSchema()


class PizzaResource(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        response = pizzas_schema.dump(pizzas, many=True)
        return response


class PizzaByIdResource(Resource):
    def get(self, id):
        pizza = Pizza.query.filter_by(id=id).first()

        if not pizza:
            abort(404, detail=f'pizza with {id} does not exist')

        else:
            result = pizzas_schema.dump(pizza)
            response = make_response(jsonify(result), 200)
            return response

    def patch(self, id):
        pass

    def delete(self, id):
        pass


api.add_resource(PizzaResource, '/pizzas')
api.add_resource(PizzaByIdResource, '/pizza/<int:id>')
