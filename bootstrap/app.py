import os

# App bootstrap class
class AppBootstrap:

    def __init__(self):
        # Laraflask app base path
        self.app_base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Laraflask app templates path
        self.app_templates_path = os.path.join(self.app_base_path, 'resources', 'views')

        # Laraflask app static path
        self.app_static_path = os.path.join(self.app_base_path, 'resources', 'static')

        # Laraflask app config path
        self.app_config_path = os.path.join(self.app_base_path, 'config')