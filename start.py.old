# # if you write this script with bash , you will have a better performance
from sys import exit
from time import sleep
from flask import current_app
from os import system

from auth1 import create_app
from auth1.command.app.test import test_database
# 
# 
app = create_app()
print ("Running tests....")


for _ in range(5):
    with app.app_context(): # load and bind to the application, enters to the context of the program
    # applictaion context . request context
    # binds the configs of the instance
        result = test_database()
    if result is True:
        break
    sleep(5)


if result is False:
    print ("Tests failed!")
    exit(1)


system("flask db upgrade")

app.run()










