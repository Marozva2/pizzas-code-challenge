# app.py
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS


from models import db

from routes.restaurantpizza_route import restpizza_bp
from routes.pizza_route import pizza_bp
from routes.restaurant_route import restaurant_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False

    db.init_app(app)
    CORS(app)
    migrate = Migrate(app, db)

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(restpizza_bp)
    app.register_blueprint(pizza_bp)

    CORS(app)

    return app
