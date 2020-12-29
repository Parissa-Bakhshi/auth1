from functools import wraps
from flask import abort, request
from jwt import decode
from jwt.exceptions import ExpiredSignatureError

from auth1.model import User
from auth1.config import Config

function_role_mapper = { # it is usually placed in the db
    "get_users": {  #get_users function
 #       roles = ["admin", "service", "master"]  #if we have roles defined
        "users": ["admin"]
    },
    "get_user": {
        "users": ["admin", ":user_id"] # ":user_id" means the user_id of the logged in user
    }
}

def auth_required(func): # "func" is just a name, a function with another function as input
    @wraps (func)
    def wrapper(*args, **kwargs):# wrapper is just a name, *args: inputs without name, **kwarkgs : inputs with name
        if not request.is_json:
            abort(415)
        if "X-Auth_Token" not in request.headers: # best practice is to use x-auth-token when the user is going to get the final request
            abort (401) #invalid input
        jwt_token = request.headers.get("X-Auth_Token")

        #print ("##################-1")




        try:
            jwt_token_data = decode(
                jwt_token,
                Config.SECRET,
                algorithms=[Config.JWT_ALGO]
            )
        except ExpiredSignatureError:
            abort (401)
        except:
            abort(401)
    
        user = User.query.get(jwt_token_data["user_id"])
        if user is None:
            abort(404)
        func_mapper = function_role_mapper[func.__name__] # it brings the role mapper of the called function
        if user.username in func_mapper["users"]:
           return func(*args, **kwargs)
        elif ":user_id" in func_mapper["users"]:
            user_id_mapper = func.__code__.co_varnames.index("user_id") # __code__.co_varname gives the function variables,
            # the list is a returned index. 
            if args[user_id_mapper] == user.id:
                return func(*args, **kwargs)
            else:
                abort (403)
        else:
            abort (403)


    return wrapper