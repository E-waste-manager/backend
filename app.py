from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import connection
import jwt
import datetime
import ranking

load_dotenv()


token_secret = os.getenv("TOKEN_SECRET")

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    data = "Hello, World!"
    return jsonify({'data': data})

# auth/login
@app.route('/auth/login', methods=['GET'])
def login():
    # data = request.get_json()
    username = request.args.get('username')
    password = request.args.get('password')
    client = connection.connect()
    db = client.ewaste
    users = db.users
    user = users.find_one({'username': username})

    if user and user['password'] == password:
        payload = {
            'username': username,
        }
        token = jwt.encode(payload, token_secret, algorithm='HS256')
        return jsonify(token)
    else:
        return jsonify({'message': 'failure'})

# auth/register
@app.route('/auth/register', methods=['POST'])
def register():
    # data = request.get_json()
    username = request.args.get('username')
    password = request.args.getO('password')
    client = connection.connect()
    db = client.ewaste
    users = db.users
    if users.find_one({'username': username}):
        return jsonify({'message': 'user already exists'})
    users = users.insert_one({'username': username, 'password': password})
    token = jwt.encode({'username': username}, token_secret, algorithm='HS256')
    if users:
        return jsonify(token)
    else:
        return jsonify({'message': 'failure'})

@app.route('/api/waste', methods=['POST'])
def waste():
    data = request.get_json()
    origin = (data['latitude'], data['longitude'])
    providers = ranking.ranking(origin)
    return jsonify(providers)
    
if __name__ == '__main__':
    app.run(debug=True)