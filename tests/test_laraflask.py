import pytest
import laraflask

# Test if the laraflask package is installed correctly
def test_laraflask_library_install():
    """Test if laraflask package is installed correctly."""
    assert laraflask.__version__ is not None

# Test if the author name is correct
def test_laraflask_author_email():
    """Test if the author email is correct."""
    assert laraflask.__email__ == "teguhrijanandi02@gmail.com"