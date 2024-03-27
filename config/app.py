import os

# App configuration class
class AppConfiguration:

    def __init__(self):
        # Laraflask app name configuration
        self.app_name = os.getenv('APP_NAME', 'LaraFlask')

        # Laraflask app debug configuration
        self.app_debug = os.getenv('APP_DEBUG', True)

        # Laraflask app environment configuration
        self.app_environment = os.getenv('APP_ENV', 'production')

        # Laraflask app port configuration
        self.app_port = os.getenv('APP_PORT', 5000)

        # Laraflask app host configuration
        self.app_host = os.getenv('APP_HOST', '0.0.0.0')

        # Laraflask secret key configuration
        self.secret_key = os.getenv('APP_KEY')
        
