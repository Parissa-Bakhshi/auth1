#User = [
#    {
#        "username": "test_user1"
#    },
#     {
#         "username": "test_user2"
#     }
# ]

from shared import uuidgen
from auth1 import db

class User(db.Model): #User class inherits from db.Model
     id = db.Column(db.String(64), primary_key=True, default=uuidgen)
     username = db.Column(db.String(128), unique=True, index=True, nullable=False)
     password = db.Column(db.String(128), nullable=False)


