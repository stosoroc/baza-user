import sqlite3
import os
from flask import Flask, render_template, request, g, flash, abort, redirect, url_for, json, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(__name__)

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://newtemp1:456123.qaz@cluster0.txedt1k.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["user-data"]
collection = db["users"]
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


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
    {"first_name": "Andrei", "last_name": "Popescu", "age": 24, "email": "andreipopescu@example.com", "city": "Bucharest", "_id": 1, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Ana", "last_name": "Maria Dragomir", "age": 28, "email": "anamariadragomir@example.com", "city": "Cluj-Napoca", "_id": 2, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Adrian", "last_name": "Diaconu", "age": 26, "email": "adriandiaconu@example.com", "city": "Timisoara", "_id": 3, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Roxana", "last_name": "Preda", "age": 33, "email": "roxanapreda@example.com", "city": "Constanta", "_id": 4, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Florin", "last_name": "Nicolae", "age": 35, "email": "florinnicolae@example.com", "city": "Brasov", "_id": 5, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Cristina", "last_name": "Tudor", "age": 23, "email": "cristinatudor@example.com", "city": "Iasi", "_id": 6, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Mihai", "last_name": "Dumitru", "age": 31, "email": "mihaidumitru@example.com", "city": "Cluj-Napoca", "_id": 7, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Maria", "last_name": "Popa", "age": 21, "email": "mariapopa@example.com", "city": "Sibiu", "_id": 8, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Alexandru", "last_name": "Rusu", "age": 34, "email": "alexandrurusu@example.com", "city": "Craiova", "_id": 9, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Ioana", "last_name": "Gheorghe", "age": 22, "email": "ioanagheorghe@example.com", "city": "Bucharest", "_id": 10, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Victor", "last_name": "Marinescu", "age": 29, "email": "victormarinescu@example.com", "city": "Timisoara", "_id": 11, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Andreea", "last_name": "Costache", "age": 30, "email": "andreeacostache@example.com", "city": "Constanta", "_id": 12, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Cristian", "last_name": "Pop", "age": 25, "email": "cristianpop@example.com", "city": "Brasov", "_id": 13, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Teodora", "last_name": "Munteanu", "age": 27, "email": "teodoramunteanu@example.com", "city": "Cluj-Napoca", "_id": 14, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Gabriel", "last_name": "Stanescu", "age": 32, "email": "gabrielstanescu@example.com", "city": "Iasi", "_id": 15, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Alina", "last_name": "Vasile", "age": 23, "email": "alinavasile@example.com", "city": "Sibiu", "_id": 16, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Marius", "last_name": "Enache", "age": 33, "email": "mariusenache@example.com", "city": "Brasov", "_id": 17, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Ana-Maria", "last_name": "Popescu", "age": 24, "email": "anamariapopescu@example.com", "city": "Bucharest", "_id": 18, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Octavian", "last_name": "Ionescu", "age": 26, "email": "octavianionescu@example.com", "city": "Craiova", "_id": 19, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Diana", "last_name": "Gavril", "age": 31, "email": "dianagavril@example.com", "city": "Cluj-Napoca", "_id": 20, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Lucian", "last_name": "Stoica", "age": 35, "email": "lucianstoica@example.com", "city": "Timisoara", "_id": 21, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Corina", "last_name": "Nedelcu", "age": 28, "email": "corinanedelcu@example.com", "city": "Constanta", "_id": 22, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Bogdan", "last_name": "Marin", "age": 29, "email": "bogdanmarin@example.com", "city": "Brasov", "_id": 23, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Ana", "last_name": "Munteanu", "age": 27, "email": "anamunteanu@example.com", "city": "Iasi", "_id": 24, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Catalin", "last_name": "Dumitrescu", "age": 22, "email": "catalindumitrescu@example.com", "city": "Sibiu", "_id": 25, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Andrei", "last_name": "Popa", "age": 34, "email": "andreipopa@example.com", "city": "Craiova", "_id": 26, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Elena", "last_name": "Gheorghe", "age": 23, "email": "elenagheorghe@example.com", "city": "Bucharest", "_id": 27, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Mihai", "last_name": "Marin", "age": 29, "email": "mihaimarin@example.com", "city": "Timisoara", "_id": 28, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Andreea", "last_name": "Popescu", "age": 30, "email": "andreeapopescu@example.com", "city": "Constanta", "_id": 29, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Cristian", "last_name": "Ionescu", "age": 25, "email": "cristianionescu@example.com", "city": "Brasov", "_id": 30, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Teodora", "last_name": "Gavril", "age": 27, "email": "teodoragavril@example.com", "city": "Cluj-Napoca", "_id": 31, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Gabriel", "last_name": "Stoica", "age": 32, "email": "gabrielstoica@example.com", "city": "Iasi", "_id": 32, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Alina", "last_name": "Vasile", "age": 23, "email": "alinavasile@example.com", "city": "Sibiu", "_id": 33, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Marius", "last_name": "Enache", "age": 33, "email": "mariusenache@example.com", "city": "Brasov", "_id": 34, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Ana-Maria", "last_name": "Popescu", "age": 24, "email": "anamariapopescu@example.com", "city": "Bucharest", "_id": 35, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Octavian", "last_name": "Ionescu", "age": 26, "email": "octavianionescu@example.com", "city": "Craiova", "_id": 36, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Diana", "last_name": "Gavril", "age": 31, "email": "dianagavril@example.com", "city": "Cluj-Napoca", "_id": 37, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Lucian", "last_name": "Stoica", "age": 35, "email": "lucianstoica@example.com", "city": "Timisoara", "_id": 38, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Corina", "last_name": "Nedelcu", "age": 28, "email": "corinanedelcu@example.com", "city": "Constanta", "_id": 39, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Bogdan", "last_name": "Marin", "age": 29, "email": "bogdanmarin@example.com", "city": "Brasov", "_id": 40, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Ana", "last_name": "Munteanu", "age": 27, "email": "anamunteanu@example.com", "city": "Iasi", "_id": 41, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Catalin", "last_name": "Dumitrescu", "age": 22, "email": "catalindumitrescu@example.com", "city": "Sibiu", "_id": 42, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Andrei", "last_name": "Popa", "age": 34, "email": "andreipopa@example.com", "city": "Craiova", "_id": 43, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Elena", "last_name": "Gheorghe", "age": 23, "email": "elenagheorghe@example.com", "city": "Bucharest", "_id": 44, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Mihai", "last_name": "Marin", "age": 29, "email": "mihaimarin@example.com", "city": "Timisoara", "_id": 45, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Andreea", "last_name": "Popescu", "age": 30, "email": "andreeapopescu@example.com", "city": "Constanta", "_id": 46, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Cristian", "last_name": "Ionescu", "age": 25, "email": "cristianionescu@example.com", "city": "Brasov", "_id": 47, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Teodora", "last_name": "Gavril", "age": 27, "email": "teodoragavril@example.com", "city": "Cluj-Napoca", "_id": 48, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Gabriel", "last_name": "Stoica", "age": 32, "email": "gabrielstoica@example.com", "city": "Iasi", "_id": 49, "avatar":"https://i.pravatar.cc/80"},
    {"first_name": "Alina", "last_name": "Vasile", "age": 23, "email": "alinavasile@example.com", "city": "Sibiu", "_id": 50, "avatar":"https://i.pravatar.cc/80"}
]
@app.route('/users')
def all_user():
        #return jsonify(users)
         return f"{collection.find({})}"

@app.route('/users/<int:user_id>')
def get_user(user_id):
    # Search for the user with the specified id
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)

    # If user with specified id is not found, return an error message
    return jsonify({'error': 'User not found'})

@app.route("/clear_database", methods=["GET"])
def clear_database():
    # Удаление всех документов из коллекции
    result = collection.delete_many({})
    return f"Deleted {result.deleted_count} documents from the database."

if __name__ == "__main__":
    app.run(debug=True)
