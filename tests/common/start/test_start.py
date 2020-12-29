from auth1 import db

def test_env(app): # it automatically injects the app defined in the conftest
   assert app.config["ENV"] == "testing"  # if we are in prod env, it asserts

def test_database(app):
    with app.app_context():
       result = db.engine.execute("SELECT database();").first() # find the db name, so we can make sure we are not working on prod DB
       assert result[0] == "testing" # this forces us to use database named "testing"

