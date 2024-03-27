import pytest
import laraflask
import os
import json
import subprocess

# Test if the laraflask package is installed correctly
def test_laraflask_library_install():
    """Test if laraflask package is installed correctly."""
    assert laraflask.__version__ is not None

# Test if the author name is correct
def test_laraflask_author_email():
    """Test if the author email is correct."""
    assert laraflask.__email__ == "teguhrijanandi02@gmail.com"

# Test if the project runs correctly
def test_run_project():
    """Test if the project runs correctly."""
    run_file = os.path.join(os.getcwd(), "run.py")

    assert run_file is not None

    # Run the project
    import subprocess
    process = subprocess.Popen(["python", run_file], stdout=subprocess.PIPE)

    # Get the output
    output, error = process.communicate()

    assert output is not None

    # Check if the project is running
    assert "Running on http://" in str(output)

    # Kill the process
    process.kill()

# Test if the hello_world route is working correctly
def test_hello_world_routes():
    """Test if the hello_world route is working correctly."""
    run_file = os.path.join(os.getcwd(), "run.py")

    # Run the project
    process = subprocess.Popen(["python", run_file], stdout=subprocess.PIPE)

    # Access to /hello_world route
    import requests
    response = requests.get("http://localhost:5000/hello_world")

    # Check if the response is correct
    # assert response.status_code == 200

    # Check if the response is correct
    # from 'message' key object in the response
    assert json.loads(response.text)["message"] == "Hello, World"

    # Kill the process
    process.kill()
    