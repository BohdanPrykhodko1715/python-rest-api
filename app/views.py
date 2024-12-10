from flask import request, jsonify
from app import app
from app.models import users, categories, records

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

# Record Endpoints
@app.route('/records', methods=['POST'])
def create_record():
    record = request.json
    record['id'] = len(records) + 1
    records.append(record)
    return jsonify({"message": "Record created", "record": record}), 201

@app.route('/records/user/<int:user_id>', methods=['GET'])
def get_user_records(user_id):
    user_records = [record for record in records if record['user_id'] == user_id]
    return jsonify({"records": user_records})

@app.route('/records/category/<int:category_id>/user/<int:user_id>', methods=['GET'])
def get_category_records(user_id, category_id):
    category_records = [record for record in records if record['category_id'] == category_id and record['user_id'] == user_id]
    return jsonify({"records": category_records})
