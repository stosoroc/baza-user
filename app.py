import sqlite3
import os
from flask import Flask, render_template, request, g, flash, abort, redirect, url_for, json, jsonify
from FDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from UserLogin import UserLogin

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
    {"name": "Jim", "age": 22, "id": 1},
    {"name": "Ion", "age": 21, "id": 2},
    {"name": "Ina", "age": 23, "id": 3},
    {"name": "Ana", "age": 25, "id": 4},
    {"name": "Pol", "age": 32, "id": 5},
    # Add more users here...
]

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
