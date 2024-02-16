from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Hero, HeroPower, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

# Define request parser for POST requests
hero_power_parser = reqparse.RequestParser()
hero_power_parser.add_argument('hero_id', type=int, required=True, help="Hero ID is required")
hero_power_parser.add_argument('power_id', type=int, required=True, help="Power ID is required")
hero_power_parser.add_argument('strength', type=str, required=True, choices=('Strong', 'Weak', 'Average'), help="Strength must be one of 'Strong', 'Weak', 'Average'")

class HeroListResource(Resource):
    def get(self):
        heroes = Hero.query.all()
        hero_list = [{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes]
        return jsonify(hero_list)

class HeroResource(Resource):
    def get(self, hero_id):
        hero = Hero.query.get(hero_id)
        if hero:
            powers = [{"id": power.id, "name": power.name, "description": power.description} for power in hero.powers]
            return jsonify({"id": hero.id, "name": hero.name, "powers": powers})
        else:
            return jsonify({"error": f"Hero with id {hero_id} not found"})

class HeroPowerResource(Resource):
    def post(self):
        args = hero_power_parser.parse_args()
        hero_id = args['hero_id']
        power_id = args['power_id']
        strength = args['strength']

        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)

        if not hero or not power:
            return jsonify({"error": "Hero or Power not found"}), 404

        hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
        db.session.add(hero_power)

        try:
            db.session.commit()
            powers = [{"id": p.id, "name": p.name, "description": p.description} for p in hero.powers]
            return jsonify({
                "message": "HeroPower created successfully",
                "hero": {"id": hero.id, "name": hero.name, "powers": powers}
            }), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Failed to create HeroPower. {str(e)}"}), 500

class PowerResource(Resource):
    def get(self, power_id):
        power = Power.query.get(power_id)
        if power:
            return jsonify({"id": power.id, "name": power.name, "description": power.description})
        else:
            return jsonify({"error": f"Power with id {power_id} not found"}), 404

class PowersResource(Resource):
    def get(self):
        powers = Power.query.all()
        powers_data = [{"id": power.id, "name": power.name, "description": power.description} for power in powers]
        return jsonify({"powers": powers_data})


api.add_resource(HeroListResource, '/heroes')
api.add_resource(HeroResource, '/heroes/<int:hero_id>')
api.add_resource(HeroPowerResource, '/hero_powers')
api.add_resource(PowerResource, '/powers/<int:power_id>')
api.add_resource(PowersResource, '/powers')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
