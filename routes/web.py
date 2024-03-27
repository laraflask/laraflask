# routes/web.py

from flask import Blueprint
from app.Http.Controllers.welcomeController import WelcomeController

# Create a Blueprint for web routes
web_bp = Blueprint('web', __name__)

# Define routes
@web_bp.route('/')
def index():
    return WelcomeController().welcome()

