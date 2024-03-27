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
    
    # The hello world method
    def hello_world(self):
        return jsonify({'message': 'Hello, World!'})
    
    def post_method(self):
        # Catch all the post data from json
        post_data = request.json

        # Return the post data
        return jsonify(post_data)