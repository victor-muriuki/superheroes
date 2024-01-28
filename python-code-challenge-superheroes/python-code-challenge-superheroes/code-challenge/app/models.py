# models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Nullable

db = SQLAlchemy()

#create tabels

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    

class HeroPower(db.Model):
    __tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)
    strength = db.Column(db.String(20), nullable=False)

     #define relationships
    hero = db.relationship('Hero', backref='hero_powers')
    power_relation = db.relationship('Power', backref='hero_powers_related') 

    
class Power(db.Model):
    __tablename__ = 'power'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(150), nullable = False)
    
    #relationship
    hero_powers_relation = db.relationship('HeroPower', backref='power')


    

# add any models you may need. 