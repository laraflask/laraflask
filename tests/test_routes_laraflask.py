import requests
import os

# Test if the hello_world route is working
def test_http_code_hello_world():
    app_port = os.getenv('APP_PORT', 5000)
    app_host = os.getenv('APP_HOST', 'localhost')
    url = f'http://{app_host}:{app_port}/test/hello_world'

    response = requests.get(url)

    # Check if the response is 200
    assert response.status_code == 200

# Test if the hello_world route is returning the correct response
def test_response_hello_world():
    app_port = os.getenv('APP_PORT', 5000)
    app_host = os.getenv('APP_HOST', 'localhost')
    url = f'http://{app_host}:{app_port}/test/hello_world'

    response = requests.get(url)

    # Get the response json
    # from 'message' key in the json
    response_json = response.json()

    # Check if the response is 'Hello, World!'
    assert response_json['message'] == 'Hello, World!'
    