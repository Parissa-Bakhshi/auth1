from time import time # to get the system time
from jwt import encode, decode
from flask import request,abort # we need to read request from user
from jwt.exceptions import ExpiredSignatureError # jwt token expiration exception


from auth1.config import Config # to set JWT_TOKEN_LIFETIME
from auth1.model import User
from auth1.schema.apiv1 import UserSchema # to get data from user



class AuthController:

    def create_token():

        if not request.is_json:
            abort (415) # unsupported media type. if the user does send json format: Content-Type: application/json in curl
        user_schema = UserSchema() # read schema
        data = user_schema.load(request.get_json()) 
        if "username" in data and "password" in data:
            user = User.query.filter_by(username=data["username"]).first() # check if username exists. This the the data that the user has entered
            if user is None:
                abort(404)
            if user.password == data["password"]:
                current_time=time()
                #print ("###########-1")
                jwt_token = encode(
                    {
                        "user_id": user.id,
                        "username": user.username,
                        "iss": "auth1", #issuer
                        "iat": current_time, #when issued
                        "nbf": current_time, # not before
                        "exp": current_time + Config.JWT_TOKEN_LIFETIME #expiration

                    },
                    Config.SECRET, 
                    algorithm=Config.JWT_ALGO 
                )#.decode("utf8")  # data is binary, so it should be changed to utf-8
                #print ("###########-2")
                return { "user": user_schema.dump(user) }, 201, { "X-Subject-Token": jwt_token } # 201=created . this is body + header


            else: #wrong pass

                abort(401)# unauthorized


            
        else:
            abort(400)

    def verify_token():
        if not request.is_json: #If it is not json >>> no problem
            abort (415)
        if "X-Subject-Token" not in request.headers:
            abort (400)
        #we should read the header and verify it
        jwt_token = request.headers.get("X-Subject-Token")
        try:
            jwt_token_data = decode(
                jwt_token,
                Config.SECRET,
                algorithms=[Config.JWT_ALGO] # if we should not specify this >>> a security breach ("none algorithm")
                #now we should exception on github page of pyjwt
                #https://github.com/jpadilla/pyjwt/blob/master/jwt/exceptions.py
                #https://pyjwt.readthedocs.io/en/stable/api.html
            )
        
        except ExpiredSignatureError:
            abort (401) #unauthorized
        except: # all other exceptions
            abort (400)
        user = User.query.get(jwt_token_data["user_id"])# find the user for verification
        if user is None:
            abort(404) # no user found
        # we can check other user options like: is_enabled, expiration time
        user_schema = UserSchema()
        return { "user": user_schema.dump(user) }, 200, { "X-Subject-Token": jwt_token } # 200: ok


        