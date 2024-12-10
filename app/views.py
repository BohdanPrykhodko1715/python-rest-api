from flask import request, jsonify
from app import app

#Base endpoint
@app.route('/', methods=['GET'])
def base_endpoint():
    return jsonify({"message": "Welcome to Expense Tracking REST API"}), 200

# User Endpoints
@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    user['id'] = len(users) + 1
    users.append(user)
    return jsonify({"message": "User created", "user": user}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users})
