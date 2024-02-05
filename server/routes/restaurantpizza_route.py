# restaurantpizza_route.py

from flask import Blueprint, make_response, jsonify
from flask_restful import Api, Resource, abort, reqparse
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import RestaurantPizza, db


restpizza_bp = Blueprint('restpizza_bp', __name__)
ma = Marshmallow(restpizza_bp)
api = Api(restpizza_bp)

post_args = reqparse.RequestParser()
post_args.add_argument('restaurant_id', type=int,
                       required=True, help='Restaurant_id is required')
post_args.add_argument('pizza_id', type=str, required=True,
                       help='Pizza_id is required')


patch_args = reqparse.RequestParser()
patch_args.add_argument('restaurant_id', type=int)
patch_args.add_argument('pizza_id', type=int)


class RestaurantPizzaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RestaurantPizza

    id = ma.auto_field()
    restaurant_id = ma.auto_field()
    pizza_id = ma.auto_field()


restaurantpizzas_schema = RestaurantPizzaSchema()


class RestaurantPizzaResource(Resource):
    def get(self):
        rest_pizzas = RestaurantPizza.query.all()
        response = restaurantpizzas_schema.dump(rest_pizzas, many=True)

        return response

    def post(self):
        pass


class RestaurantByIdPizzaResource(Resource):
    def get(self, id):
        rest_pizza = RestaurantPizza.query.filter_by(id=id).first()

        if not rest_pizza:
            abort(404, detail=f'Restaurant not found')

        else:
            result = restaurantpizzas_schema.dump(rest_pizza)
            response = make_response(jsonify(result), 200)
            return response

    def patch(self, id):
        pass

    def delete(self, id):
        pass


api.add_resource(RestaurantPizzaResource, '/restaurant_pizza')
api.add_resource(RestaurantByIdPizzaResource, '/restaurant_pizza/<int:id>')
