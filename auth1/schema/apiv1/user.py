from auth1 import ma

from auth1.model import User

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User 
    
    id = ma.auto_field(dump_only=True)
    username = ma.auto_field()
    password = ma.auto_field()
     
 