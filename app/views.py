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

# Category Endpoints
@app.route('/categories', methods=['POST'])
def create_category():
    category = request.json
    category['id'] = len(categories) + 1
    categories.append(category)
    return jsonify({"message": "Category created", "category": category}), 201

@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify({"categories": categories})
