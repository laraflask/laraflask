from flask import jsonify, request

# This controller are used for unit testing. 
# You can remove this file if you don't need it.
class testController:

    # The hello world method
    def hello_world(self):
        return jsonify({'message': 'Hello, World!'})
    
    # The post method
    def post_method(self):
        # Catch all the post data from json
        post_data = request.json

        # Return the post data
        return jsonify(post_data)
    
    # The health check method
    def health_check(self):
        return "OK"