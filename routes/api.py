# routes/api.py

from flask import Blueprint, jsonify

# Create a Blueprint for web routes
api_bp = Blueprint('api', __name__)

# Define routes
@api_bp.route('/')
def index():
    # Return json
    return jsonify({'message': 'Welcome to the LaraFlask API!'})