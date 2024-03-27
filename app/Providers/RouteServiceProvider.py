# Import routes files
from routes.web import web_bp
from routes.api import api_bp
from laraflask.Routes.assets import assets_bp

# Import testing route
# You can remove this file if you don't need it.
from routes.test import test_bp

class RouteServiceProvider:

    # Initialize the RouteServiceProvider class
    def __init__(self, app):
        self.app = app

    # Register routes
    def boot(self):
        # Register web routes
        self.app.register_blueprint(web_bp)

        # Register api routes with a /api/ prefix
        self.app.register_blueprint(api_bp, url_prefix='/api')

        # Register assets route
        self.app.register_blueprint(assets_bp, url_prefix='/assets')

        # Register testing route
        # You can remove this file if you don't need it.
        self.app.register_blueprint(test_bp, url_prefix='/test')

        # Register yourself route here
        # self.app.register_blueprint(yourself_bp)

        return self.app