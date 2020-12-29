from flask_restx import Resource
from auth1.controller.apiv1.user import UserController

class UserResource(Resource): #inheritance from Resource
    
    def get(self, user_id=None):
        """
        GET /users >> Get user collection  
        GET /users/<user_id> >> Get single user 
        """
        if user_id == None:
            return UserController.get_users() # Get user collection
        else:
            return UserController.get_user(user_id)
        

    def post(self):
       """
       POST  /users --> Create new user
       """  
       return UserController.create_user()

    def patch(self): 
        pass

    def delete(self):
        pass

    
