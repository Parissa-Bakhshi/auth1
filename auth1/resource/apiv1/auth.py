from flask_restx import Resource 

from auth1.controller.apiv1 import AuthController

class AuthResource(Resource):
    def get(self):
        """
        GET /auth/tokens ---> verify JWT token
        """
        return AuthController.verify_token()
    def post(self):
        """
        POST /auth/tokens ---> Create new JWT token
        """
        return AuthController.create_token()
         

  
    
