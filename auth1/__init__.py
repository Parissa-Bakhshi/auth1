from flask import Flask, Blueprint
from flask.cli import AppGroup # to create cli
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


from auth1.config import Config  # Import application config

db = SQLAlchemy() 
mg = Migrate()
ma = Marshmallow()


apiv1_bp = Blueprint("apiv1", __name__, url_prefix="/api/v1") # Create /api/v1 endpoint
apiv1 = Api(apiv1_bp)#Create API for /api/v1 endpoint

app_cli = AppGroup("app", help="Application related commands.")

from auth1 import command
from auth1 import resource

def create_app():
    app = Flask(__name__) # Create application instance
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:test@10.10.10.76:3306/auth1'
    app.config.from_object(Config) # Set application configuration test!!!!!!
    db.init_app(app)
    mg.init_app(app, db)#inputs:reads config from app and connets to db
    ma.init_app(app)
    app.register_blueprint(apiv1_bp) #register /api/v1 to application
    app.cli.add_command(app_cli)
    return app # Return application instance to caller
     