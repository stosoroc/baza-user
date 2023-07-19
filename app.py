import sqlite3
import os
from flask import Flask, render_template, request, g, flash, abort, redirect, url_for, json, jsonify
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path,'flsite.db')))


@app.route('/summary')
def summary():
    #data = make_summary()
    response = app.response_class(
        response=json.dumps({"name":"Alina"}),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/')
def home1():
        return jsonify({"mssg":"The API works"})

@app.route('/number/<var1>')
def number(var1):
        return jsonify({"number":f"{var1}"})
    
@app.route('/<name>')
def greet(name):
        return jsonify({"mssg":f"Hello {name}"})

users = [
    {"name": "Andrei Popescu","age": 24,"email": "andreipopescu@example.com","city": "Bucharest", "id": 1},
{"name": "Ana Maria Dragomir","age":  28,"email": "anamariadragomir@example.com","city": "Cluj-Napoca", "id": 2},
{"name": "Adrian Diaconu","age":  26,"email": "adriandiaconu@example.com","city": "Timisoara", "id": 3},
{"name": "Roxana Preda","age": 33,"email": "roxanapreda@example.com","city": "Constanta", "id": 4},
{"name": "Florin Nicolae","age": 35,"email": "florinnicolae@example.com","city": "Brasov", "id": 5},
{"name": "Cristina Tudor","age": 23,"email": "cristinatudor@example.com","city": "Iasi", "id": 6},
{"name": "Mihai Dumitru","age": 31,"email": "mihaidumitru@example.com","city": "Cluj-Napoca", "id": 7},
{"name": "Maria Popa","age": 21,"email": "mariapopa@example.com","city": "Sibiu", "id": 8},
{"name": "Alexandru Rusu","age": 34,"email": "alexandrurusu@example.com","city": "Craiova", "id": 9},
{"name": "Ioana Gheorghe","age": 22,"email": "ioanagheorghe@example.com","city": "Bucharest", "id": 10},
{"name": "Victor Marinescu","age": 29,"email": "victormarinescu@example.com","city": "Timisoara", "id": 11},
{"name": "Andreea Costache","age": 30,"email": "andreeacostache@example.com","city": "Constanta", "id": 12},
{"name": "Cristian Pop","age": 25,"email": "cristianpop@example.com","city": "Brasov", "id": 13},
{"name": "Teodora Munteanu","age": 27,"email": "teodoramunteanu@example.com","city": "Cluj-Napoca", "id": 14},
{"name": "Gabriel Stanescu","age": 32,"email": "gabrielstanescu@example.com","city": "Iasi", "id": 15},
{"name": "Alina Vasile","age": 23,"email": "alinavasile@example.com","city": "Sibiu", "id": 16},
{"name": "Marius Enache","age": 33,"email": "mariusenache@example.com","city": "Brasov", "id": 17},
{"name": "Ana-Maria Popescu","age": 24,"email": "anamariapopescu@example.com","city": "Bucharest", "id": 18},
{"name": "Octavian Ionescu","age": 26,"email": "octavianionescu@example.com","city": "Craiova", "id": 19},
{"name": "Diana Gavril","age": 31,"email": "dianagavril@example.com","city": "Cluj-Napoca", "id": 20},
{"name": "Lucian Stoica","age": 35,"email": "lucianstoica@example.com","city": "Timisoara", "id": 21},
{"name": "Corina Nedelcu","age": 28,"email": "corinanedelcu@example.com","city": "Constanta", "id": 22},
{"name": "Bogdan Marin","age": 29,"email": "bogdanmarin@example.com","city": "Brasov", "id": 23},
{"name": "Ana Predoiu","age": 23,"email": "anapredoiu@example.com","city": "Iasi", "id": 24},
{"name": "Andrei Petrescu","age": 22,"email": "andreipetrescu@example.com","city": "Sibiu", "id": 25},
{"name": "Elena Barbu","age": 23,"email": "elenabarbu@example.com","city": "Craiova", "id": 26},
{"name": "Ionut Mihai","age": 30,"email": "ionutmihai@example.com","city": "Cluj-Napoca", "id": 27},
{"name": "Alexandra Negru","age": 24,"email": "alexandranegru@example.com","city": "Timisoara", "id": 28},
{"name": "Stefan Ion","age": 31,"email": "stefanion@example.com","city": "Constanta", "id": 29},
{"name": "Anca Stan","age": 27,"email": "ancastan@example.com","city": "Brasov", "id": 30},
]

@app.route('/users')
def all_user():
        return jsonify(users)

@app.route('/users/<int:user_id>')
def get_user(user_id):
    # Search for the user with the specified id
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)

    # If user with specified id is not found, return an error message
    return jsonify({'error': 'User not found'})

if __name__ == "__main__":
    app.run(debug=True)
