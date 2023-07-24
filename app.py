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


@app.route('/users')
def all_user():
        #return jsonify(users)
        documents = list(collection.find())
        return jsonify(documents)

@app.route('/users/<int:user_id>')
def get_user(user_id):
        documents = collection.find_one({'_id': user_id})
        if documents:
            return jsonify(documents)
        else:
            return jsonify({'error': 'Document not found'})
    

@app.route('/element', methods=['POST'])
def insert_element():
    element = request.get_json()
    result = collection.insert_one(element)
    if result:
        return jsonify({'message': 'Element inserted successfully'})
    else:
        return jsonify({'error': 'Failed to insert element'})

@app.route("/clear_database", methods=["GET"])
def clear_database():
    # Удаление всех документов из коллекции
    result = collection.delete_many({})
    return f"Deleted {result.deleted_count} documents from the database."

if __name__ == "__main__":
    app.run(debug=True)
