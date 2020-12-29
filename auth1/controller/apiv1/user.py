from flask import abort, request

from auth1 import db
from auth1.model import User
from auth1.schema.apiv1 import UserSchema
from auth1.decorator.apiv1 import auth_required
class UserController:
    
    @auth_required # this is our decorator for authentication befor running the following funcs
    def get_users():
        users = User.query.all()
        users_schema = UserSchema(many=True)
        #return { "users_schema".dump(users) }
  
        return users_schema.dump(users) 
     
    def get_user(user_id):
        user = User.query.get(user_id)
        user_schema = UserSchema()
        if user is None:
            abort(404)
        return  user_schema.dump(user) 

    def create_user():
        user_schema = UserSchema()
        #data = request.get_json()
        # print ("##########-1")
        try:
            data = user_schema.load(request.get_json())# filter data
        except:
            abort (400)
        if not data["username"] or not data["password"]:
            abort(400)
        if "username" in data and "password" in data: # if the user has entered username and password items
            user = User.query.filter_by(username=data["username"]).first() # find the fisrt entered value for the username
            if user is None:
                user = User(username=data["username"], password=data["password"])
                db.session.add(user) # add session for the user instance you created
                try:
                    db.session.commit() 
                except: # is a db error occures:
                    db.session.rollback()
                    abort (500) # internal server error
                return  user_schema.dump(user), 201 

                
            else:
                abort (409) # data conflict
        else: 
            abort(400)