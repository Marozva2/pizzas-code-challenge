from models import db, Restaurant, Pizza, RestaurantPizza
from app import app


restaurants = [{
    "id": 1,
    "name": "Yance",
    "address": "938 Mosinee Point"
}, {
    "id": 2,
    "name": "Egor",
    "address": "56 Marcy Place"
}, {
    "id": 3,
    "name": "Rock",
    "address": "75 Montana Point"
}, {
    "id": 4,
    "name": "Charlena",
    "address": "69 Westridge Avenue"
}, {
    "id": 5,
    "name": "Isac",
    "address": "29701 Old Shore Terrace"
}, {
    "id": 6,
    "name": "Torrie",
    "address": "23 John Wall Court"
}, {
    "id": 7,
    "name": "Lind",
    "address": "501 Jenifer Crossing"
}, {
    "id": 8,
    "name": "Luigi",
    "address": "12 Alpine Court"
}, {
    "id": 9,
    "name": "Neale",
    "address": "715 Starling Junction"
}, {
    "id": 10,
    "name": "May",
    "address": "374 Hooker Court"
}]


pizzas = [{
    "id": 1,
    "name": "Cheese",
    "ingredients": "Pepsi - Diet, 355 Ml"
}, {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Wine - Ruffino Chianti"
}, {
    "id": 3,
    "name": "Meat",
    "ingredients": "Tea - Lemon Scented"
}, {
    "id": 4,
    "name": "Margherita",
    "ingredients": "Vaccum Bag 10x13"
}, {
    "id": 5,
    "name": "Greek",
    "ingredients": "Brocolinni - Gaylan, Chinese"
}, {
    "id": 6,
    "name": "Supreme",
    "ingredients": "Basil - Primerba, Paste"
}, {
    "id": 7,
    "name": "Hawaiian",
    "ingredients": "Marjoram - Fresh"
}, {
    "id": 8,
    "name": "Veggie",
    "ingredients": "Salt - Seasoned"
}, {
    "id": 9,
    "name": "BBQ",
    "ingredients": "Soup - Cream Of Broccoli, Dry"
}, {
    "id": 10,
    "name": "Buffallo",
    "ingredients": "Radish"
}]


restaurantpizzas = [{
    "id": 1,
    "restaurant_id": 2,
    "pizza_id": 1
}, {
    "id": 2,
    "restaurant_id": 1,
    "pizza_id": 4
}, {
    "id": 3,
    "restaurant_id": 5,
    "pizza_id": 2
}, {
    "id": 4,
    "restaurant_id": 3,
    "pizza_id": 3
}, {
    "id": 5,
    "restaurant_id": 4,
    "pizza_id": 7
}]


with app.app_context():
    db.session.query(Restaurant).delete()
    db.session.query(Pizza).delete()
    db.session.query(RestaurantPizza).delete()

    for restaurant in restaurants:
        new_restaurant = Restaurant(
            id=restaurant['id'], name=restaurant['name'], address=restaurant['address'])
        db.session.add(new_restaurant)

    for pizza in pizzas:
        new_pizza = Pizza(id=pizza['id'], name=pizza['name'],
                          ingredients=pizza['ingredients'])
        db.session.add(new_pizza)

    for restaurantpizza in restaurantpizzas:
        new_restaurantpizza = RestaurantPizza(
            id=restaurantpizza['id'], restaurant_id=restaurantpizza['restaurant_id'], pizza_id=restaurantpizza['pizza_id'])
        db.session.add(new_restaurantpizza)

    db.session.commit()
