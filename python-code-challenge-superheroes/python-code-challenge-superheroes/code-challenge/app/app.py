#app.py
from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api
from models import db, Hero, HeroPower, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)



@app.route('/')
def home():
    return '<h1>This is landing pasge</h1>'

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')
    strength = data.get('strength')

    if not all([hero_id, power_id, strength]):
        return jsonify({"error": "Missing required fields"})

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({"error": "Hero or Power not found"})

    if strength not in ['Strong', 'Weak', 'Average']:
        return jsonify({"error": "Invalid strength value. Must be one of 'Strong', 'Weak', 'Average'"})

    hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
    db.session.add(hero_power)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to create HeroPower. {str(e)}"})

    powers = [{"id": p.id, "name": p.name, "description": p.description} for p in hero.powers]
    return jsonify({
        "message": "HeroPower created successfully",
        "hero": {"id": hero.id, "name": hero.name, "powers": powers}
    })


@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_power(power_id):
    power = Power.query.get(power_id)

    if not power:
        return jsonify({"error": f"Power with id {power_id} not found"}), 404

    data = request.json
    new_description = data.get('description')

    if new_description:
        power.description = new_description

        try:
            db.session.commit()
            return jsonify({"message": "Power description updated successfully", "power": {"id": power.id, "description": power.description}})
        except ValueError as e:
            return jsonify({"error": str(e)})
    else:
        return jsonify({"error": "Invalid request data"})


@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get(power_id)
    if power:
        return jsonify({"id": power.id, "name": power.name, "description": power.description})
    else:
        return jsonify({"error": f"Power with id {power_id} not found"})



@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_data = [{"id": power.id, "name": power.name, "description": power.description} for power in powers]
    return jsonify({"powers": powers_data})


@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get(hero_id)
    if hero:
        powers = [{"id": power.id, "name": power.name, "description": power.description} for power in hero.powers]
        return jsonify({"id": hero.id, "name": hero.name, "powers": powers})
    else:
        return jsonify({"error": f"Hero with id {hero_id} not found"})
    

if __name__ == '__main__':
    app.run(port=5555)



