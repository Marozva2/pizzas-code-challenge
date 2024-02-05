# restaurant_route.py

from flask import Blueprint, make_response, jsonify
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_restful import Api, Resource, reqparse, abort
from flask_marshmallow import Marshmallow

from models import Restaurant, db

restaurant_bp = Blueprint('restaurant_bp', __name__)
ma = Marshmallow(restaurant_bp)
api = Api(restaurant_bp)

post_args = reqparse.RequestParser()
post_args.add_argument('id', type=int, required=True)
post_args.add_argument('name', type=str)
post_args.add_argument('address', type=str)

patch_args = reqparse.RequestParser()
patch_args.add_argument('id', type=int)
patch_args.add_argument('name', type=str)
patch_args.add_argument('address', type=int)


class RestaurantSchema(SQLAlchemyAutoSchema):

    pizzas = ma.Nested('PizzaSchema', many=True)

    class Meta:
        model = Restaurant
        include_fk = True


restaurants_schema = RestaurantSchema()


class RestaurantResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        result = restaurants_schema.dump(restaurants, many=True)
        response = make_response(jsonify(result), 200)

        return response

    def post(self):
        pass


class RestaurantByIdResource(Resource):
    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()

        if not restaurant:
            abort(404, detail=f'Restaurant with {id} does not exist')

        else:
            result = restaurants_schema.dump(restaurant)
            response = make_response(jsonify(result), 200)
            return response

    def delete(self, id):
        pass

    def patch(self, id):
        pass


api.add_resource(RestaurantResource, '/restaurants')
api.add_resource(RestaurantByIdResource, '/restaurants/<int:id>')
