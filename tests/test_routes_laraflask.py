import requests
import os

# Test if the hello_world route is working
def test_http_code_hello_world():
    # Get host and port from environment variables or use defaults
    app_host = os.getenv('APP_HOST', 'localhost')
    app_port = int(os.getenv('APP_PORT', 5000))

    # Construct the URL for the endpoint
    url = f'http://{app_host}:{app_port}/test/hello_world'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check for any HTTP errors
    response.raise_for_status()

    # Check if the response status code is 200
    assert response.status_code == 200

# Test if the hello_world route is returning the correct response
def test_response_hello_world():
    # Get host and port from environment variables or use defaults
    app_host = os.getenv('APP_HOST', 'localhost')
    app_port = int(os.getenv('APP_PORT', 5000))

    # Construct the URL for the endpoint
    url = f'http://{app_host}:{app_port}/test/hello_world'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check for any HTTP errors
    response.raise_for_status()

    # Parse the response JSON
    response_json = response.json()

    # Check if the 'message' key exists in the response JSON
    assert 'message' in response_json

    # Check if the value of the 'message' key is 'Hello, World!'
    assert response_json['message'] == 'Hello, World!'
    