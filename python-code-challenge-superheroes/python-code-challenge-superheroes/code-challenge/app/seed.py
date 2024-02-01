from app.models import db, Hero, HeroPower, Power

# Seeding powers
powers_data = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
]

powers = [Power(**power_data) for power_data in powers_data]
db.session.add_all(powers)
db.session.commit()

# Seeding heroes
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

heroes = [Hero(**hero_data) for hero_data in heroes_data]
db.session.add_all(heroes)
db.session.commit()

# Adding powers to heroes
strengths = ["Strong", "Weak", "Average"]
for hero in heroes:
    for _ in range(2):  # Add 2 random powers to each hero
        power = Power.query.order_by(db.func.random()).first()
        hero_power = HeroPower(hero=hero, power=power, strength=strengths.pop())
        db.session.add(hero_power)

db.session.commit()

print("Seeding completed successfully!")
