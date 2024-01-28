#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate

from flask_restful import Api, Resource, reqparse


from models import db, Hero, HeroPower, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)



@app.route('/')
def home():
    return '<h1>This is landing pasge</h1>'

@app.route('/add_hero', methods = ['POST'])
def add_hero():
    data = request.json

    new_hero = Hero(name = data['name'])
    db.session.add(new_hero)
    db.session.commit()


    return jsonify({"message": "Hero added successfully"})


@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_data = [{"id": hero.id, "name": hero.name} for hero in heroes]
    return jsonify({"heroes": heroes_data})

@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get(hero_id)
    if hero:
        return jsonify({"id": hero.id, "name": hero.name})
    else:
        return jsonify({"error": f"Hero with id {hero_id} not found"}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_data = [{"id": power.id, "description": power.description} for power in powers]
    return jsonify({"powers": powers_data})

@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get(power_id)
    if power:
        return jsonify({"id": power.id, "description": power.description})
    else:
        return jsonify({"error": f"Power with id {power_id} not found"}), 404

if __name__ == '__main__':
    app.run(port=5555)



