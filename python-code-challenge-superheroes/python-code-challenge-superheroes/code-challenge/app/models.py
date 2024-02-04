# models.py

from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# create tables

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)

    # relationships
    hero_powers = db.relationship('HeroPower', back_populates='power')
    heroes_associated = db.relationship('Hero', secondary='hero_powers', back_populates='powers')  # renamed backref

    # validation
    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 5:
            raise ValueError("Description must be at least 5 characters long")
        return description

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(255), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)

    # relationships
    power = db.relationship('Power', back_populates='hero_powers')
    hero = db.relationship('Hero', back_populates='hero_powers')

    @validates('strength')
    def validate_strength(self, key, strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be one of 'Strong', 'Weak', 'Average'")
        return strength

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    super_name = db.Column(db.String(255), nullable=False)

    # relationships
    powers = db.relationship('Power', secondary='hero_powers', back_populates='heroes_associated')  # renamed backref
    hero_powers = db.relationship('HeroPower', back_populates='hero')
