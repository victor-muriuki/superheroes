#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate


from models import db, Hero, HeroPower, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>This is landing pasge</h1>'

@app.route('/add_hero', methods = ['POST'])
def add_hero():
    data = request.json

    new_hero = Hero(name = data['name'])
    db.session.add(new_hero)
    db.session.commit()


    return jsonify({"message": "Hero added successfully"}),


    if __name__ == '__main__':
        app.run(port=5555)
