from flask import request, jsonify
from app import app

#Base endpoint
@app.route('/', methods=['GET'])
def base_endpoint():
    return jsonify({"message": "Welcome to Expense Tracking REST API"}), 200

