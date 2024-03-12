# routes/web.py

from flask import Blueprint
from app.Http.Controllers.welcomeController import WelcomeController

# Create a Blueprint for web routes
web_bp = Blueprint('web', __name__)

# Define routes
@web_bp.route('/')
def index():
    return WelcomeController().welcome()

# Define routes
@web_bp.route('/post_method', methods=['POST'])
def post_method():
    return WelcomeController().post_method()

@web_bp.route('/other_post_method', methods=['POST'])
def other_post_method():
    return WelcomeController().post_method()
