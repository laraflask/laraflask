# routes/api.py
# This routes are used for unit testing. 
# You can remove this file if you don't need it.

from flask import Blueprint
from app.Http.Controllers.testController import testController

# Create a Blueprint for test routes
test_bp = Blueprint('test', __name__)

# Define routes for test hello world
@test_bp.route('/hello_world', methods=['GET'])
def hello_world():
    return testController().hello_world()

# Define routes for post method without CSRF protection
@test_bp.route('/post_method', methods=['POST'])
def post_method():
    return testController().post_method()

# Define routes for other post method with CSRF protection
@test_bp.route('/other_post_method', methods=['POST'])
def other_post_method():
    return testController().post_method()

# Define routes for health check
@test_bp.route('/health_check', methods=['GET'])
def health_check():
    return testController().health_check()
