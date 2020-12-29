import pytest

from auth1 import create_app  # we can have multiple instances with multiple configs

#fixture: Basic functions that we should have to test the application

@pytest.fixture
def app():
     app = create_app()
     return app

@pytest.fixture # without running flask we can send request to endpoint and get the results
def client(app):
    return app.test_client() 

@pytest.fixture # we can use the cli we created for test
def runner(app):
    return app.test_cli_runner()
