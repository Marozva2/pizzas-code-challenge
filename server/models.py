from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String)
    address = db.Column(db.String)

    pizzas = db.relationship('RestaurantPizza', backref='restaurant')


class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)

    restaurants = db.relationship('RestaurantPizza', backref='pizza')


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurantpizzas'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
