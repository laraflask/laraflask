import os
import requests

# Test the '/test/hello_world' endpoint
# def test_response_hello_world():
#     container_ip = os.environ.get('CONTAINER_IP', '0.0.0.0')
#     app_port = 5000

#     # Construct the URL for the endpoint
#     url = f'http://{container_ip}:{app_port}/test/hello_world'

#     # Send a GET request to the URL
#     response = requests.get(url)

#     # Check for any HTTP errors
#     response.raise_for_status()

#     # Parse the response JSON
#     response_json = response.json()

#     # Check if the 'message' key exists in the response JSON
#     assert 'message' in response_json

#     # Check if the value of the 'message' key is 'Hello, World!'
#     assert response_json['message'] == 'Hello, World!'

def test_http_code_hello_world():
    container_ip = os.environ.get('CONTAINER_IP', '0.0.0.0')
    app_port = 5000

    # Construct the URL for the endpoint
    url = f'http://{container_ip}:{app_port}'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check for http code 200
    assert response.status_code == 200
