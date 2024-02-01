# models.py
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

#create tabels

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    super_name = db.Column(db.String(255), nullable=False)

    #relationship
    powers = db.relationship('Power', secondary='hero_powers', back_populates='heroes')

    

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(255), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)

#relationships
    power = db.relationship('Power', back_populates='hero_powers')
    hero = db.relationship('Hero', back_populates='hero_powers')

    @validates('strength')
    def validate_strength(self, key, strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be one of 'Strong', 'Weak', 'Average'")
        return strength

    
class Power(db.Model):
    __tablename__ = 'powers'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

#relationship
    heroes = db.relationship('Hero', secondary='hero_powers', back_populates='powers')

#validation
    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return description



    