from os import environ
class Config:
    DEBUG = bool(environ.get("AUTH1_DEBUG", False))

    TESTING = bool( environ.get("AUTH1_TESTING", False))

    ENV = environ.get("AUTH1_ENV", "production")

    SECRET = environ.get("AUTH1_SECRET", "HARD-DEV-SECRET") # this is for dev env, fro prod env this value shoud change,
    # we have set this secret in the config env, because if we need to expire all tokens,
    # this can happen this way, by restarting containers after changing the secret env,
    # so there is no need to change the app


    SQLALCHEMY_DATABASE_URI = environ.get("AUTH1_DATABASE_URI", None)
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:test@10.10.10.76:3306/auth1'


    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost:3306/{DB_NAME}'

    SQLALCHEMY = DEBUG # when in debug mode, set this to "true", so error logs will be sent to the stderr

    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG # when true, modifications in objects will be shown in stderr

    JWT_ALGO = environ.get("AUTH1_JWT_ALGO", "HS512")
    
    JWT_TOKEN_LIFETIME = environ.get("AUTH1_JWT_TOKEN_LIFETIME", 100) # if not set use 100


      






    
