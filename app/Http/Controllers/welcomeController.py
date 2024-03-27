from flask import render_template, jsonify, request

from laraflask.Helpers.config import Config

class WelcomeController:

    # The default page
    # /resources/views/welcome.html
    def welcome(self):
        data = {
            'title': Config().get('app.app_name'),
        }

        return render_template('welcome.html', data=data)
    
    