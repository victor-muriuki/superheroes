from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    Attributes = db.Column(db.String)

class Hero_Power(db.Model):
    __tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    
class Power(db.Model):
    __tablename__ = 'power'


    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer)
    power_id = db.Column(db.Integer)
    

    

# add any models you may need. 