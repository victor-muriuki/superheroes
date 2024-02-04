# seed.py

from models import db, Hero, Power, HeroPower

def seed_data():
    # Create Powers
    power1 = Power(name='Flight', description='Can fly in the sky')
    power2 = Power(name='Super Strength', description='Has incredible strength')
    power3 = Power(name='Web-slinging', description='Can swing between buildings using webs')

    # Add Powers to the database
    db.session.add_all([power1, power2, power3])
    db.session.commit()

    # Create Heroes
    hero1 = Hero(name='Superman', super_name='Clark Kent')
    hero2 = Hero(name='Spiderman', super_name='Peter Parker')

    # Add Heroes to the database
    db.session.add_all([hero1, hero2])
    db.session.commit()

    # Create HeroPower relationships
    hero_power1 = HeroPower(hero_id=hero1.id, power_id=power1.id, strength='Strong')
    hero_power2 = HeroPower(hero_id=hero1.id, power_id=power2.id, strength='Average')
    hero_power3 = HeroPower(hero_id=hero2.id, power_id=power3.id, strength='Strong')

    # Add HeroPower relationships to the database
    db.session.add_all([hero_power1, hero_power2, hero_power3])
    db.session.commit()

if __name__ == '__main__':
    # Make sure to initialize your Flask app and database before running the seed file
    from app import app, db
    with app.app_context():
        # Uncomment the line below to create the database tables if they don't exist
        db.create_all()
        seed_data()
