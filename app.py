from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
import os
from flask import Flask, request, g, json, jsonify
from flask_cors import CORS
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)
app.config.from_object(__name__)

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


# @app.route('/summary')
# def summary():
#     #data = make_summary()
#     response = app.response_class(
#         response=json.dumps({"name":"Alina"}),
#         status=200,
#         mimetype='application/json'
#     )
#     return response

@app.route('/')
def home1():
    return jsonify({"mssg": "The API works"})


@app.route('/number/<var1>')
def number(var1):
    return jsonify({"number": f"{var1}"})


@app.route('/<name>')
def greet(name):
    return jsonify({"mssg": f"Hello {name}"})

users = [
    {"first_name": "Andrei", "last_name": "Popescu", "age": 24, "email": "andreipopescu@example.com", "city": "Bucharest", "_id": 1, "avatar": "https://i.pravatar.cc/80"},
    {"first_name": "Ana", "last_name": "Maria Dragomir", "age": 28, "email": "anamariadragomir@example.com", "city": "Cluj-Napoca", "_id": 2, "avatar": "https://i.pravatar.cc/80"},
    {"first_name": "Adrian", "last_name": "Diaconu", "age": 26, "email": "adriandiaconu@example.com", "city": "Timisoara", "_id": 3, "avatar": "https://i.pravatar.cc/80"},
    {"first_name": "Roxana", "last_name": "Preda", "age": 33, "email": "roxanapreda@example.com", "city": "Constanta", "_id": 4, "avatar": "https://i.pravatar.cc/80"},
    {"first_name": "Florin", "last_name": "Nicolae", "age": 35, "email": "florinnicolae@example.com", "city": "Brasov", "_id": 5, "avatar": "https://i.pravatar.cc/80"}
    ]


@app.route('/users')
@app.route('/users/')
def all_user():
    documents = list(collection.find())
    for d in documents:
        d['_id'] = str(d['_id'])
    try:
        json_object = jsonify(documents)
        return json_object
    except:
        return jsonify(users)


@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    documents = collection.find_one({'_id': ObjectId(user_id)})
    documents['_id'] = str(documents['_id'])
    if documents:
        return jsonify(documents)
    else:
        return jsonify({'error': 'Document not found'})


@app.route('/element')
def insert_element():
    element = request.get_json()
    result = collection.insert_one(element)
    if result:
        return jsonify({'message': 'Element inserted successfully'})
    else:
        return jsonify({'error': 'Failed to insert element'})


@app.route('/update/<string:user_id>')
def update_document(user_id):
    data = request.get_json()
    result = collection.update_one({'_id': ObjectId(user_id)}, {'$set': data})
    if result.modified_count == 1:
        return jsonify({'message': 'Document updated'})
    else:
        return jsonify({'message': 'Document not found'})


@app.route('/delete/<string:user_id>')
def delete_document(user_id):
    result = collection.delete_one({'_id': ObjectId(user_id)})
    if result.deleted_count == 1:
        return jsonify({'message': 'Document deleted'})
    else:
        return jsonify({'message': 'Document not found'})


@app.route("/clear_database", methods=["GET"])
def clear_database():
    # Удаление всех документов из коллекции
    result = collection.delete_many({})
    return f"Deleted {result.deleted_count} documents from the database."


if __name__ == "__main__":
    app.run(debug=True)

