from models import db, Power, Hero, HeroPower
from random import randint, choice
from sqlalchemy import func
from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Configure Flask application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Bind the Flask application to the SQLAlchemy database instance
db.init_app(app)

def seed_powers():
    with app.app_context():
        print("🦸‍♀️ Seeding powers...")
        powers_data = [
            {"name": "super strength", "description": "gives the wielder super-human strengths"},
            {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
            {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
            {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
        ]

        for power_data in powers_data:
            power = Power(**power_data)
            db.session.add(power)
        
        db.session.commit()
        print("🦸‍♀️ Powers seeded!")

def seed_heroes():
    with app.app_context():
        print("🦸‍♀️ Seeding heroes...")
        heroes_data = [
            {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
            {"name": "Doreen Green", "super_name": "Squirrel Girl"},
            {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
            {"name": "Janet Van Dyne", "super_name": "The Wasp"},
            {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
            {"name": "Carol Danvers", "super_name": "Captain Marvel"},
            {"name": "Jean Grey", "super_name": "Dark Phoenix"},
            {"name": "Ororo Munroe", "super_name": "Storm"},
            {"name": "Kitty Pryde", "super_name": "Shadowcat"},
            {"name": "Elektra Natchios", "super_name": "Elektra"}
        ]

        for hero_data in heroes_data:
            hero = Hero(**hero_data)
            db.session.add(hero)

        db.session.commit()
        print("🦸‍♀️ Heroes seeded!")

def add_powers_to_heroes():
    with app.app_context():
        print("🦸‍♀️ Adding powers to heroes...")
        strengths = ["Strong", "Weak", "Average"]

        for hero in Hero.query.all():
            for _ in range(randint(1, 3)):
                power = Power.query.order_by(func.random()).first()  # Get a random power
                strength = choice(strengths)
                
                hero_power = HeroPower(hero=hero, power=power, strength=strength)
                db.session.add(hero_power)

        db.session.commit()
        print("🦸‍♀️ Done seeding!")

# Ensure the script is run only when executed directly, not when imported as a module
if __name__ == "__main__":
    seed_powers()
    seed_heroes()
    add_powers_to_heroes()
