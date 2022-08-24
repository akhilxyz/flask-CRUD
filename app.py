# Import from system libraries
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_bcrypt import Bcrypt
from models.db import initialize_db, db_config

# Import from application modules
from errors import errors
from models.User import User
from routes.api import initialize_routes

# Flask app instance with static (html, css and js) folder configuration
app = Flask(__name__)

# Flask Restful configuration with errors included
api = Api(app, errors=errors)

# App configuration Secret key
app.config["SECRET_KEY"] = "KeepThisS3cr3tJ0hn"

# App configuration For Mongoose Settings
app.config["MONGODB_SETTINGS"] = db_config

# BCrypt instances
bcrypt = Bcrypt(app)

# JWT instances
jwt = JWTManager(app)

# CORS enabled
CORS(app)

# Database Configuration Initialization
initialize_db(app)

# API (Routing) Configuration Initialization
initialize_routes(api)

# check server is listing


@app.route("/")
def checkStatus():
    return "<p>Server is active...</p>"


# Get roles for authenticated user
@jwt.additional_claims_loader
def add_claims_to_access_token(user):
    return {'roles': user.roles}


# Load user identity
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.username


# Admin account initialization for first uses
user = User.objects(username='admin@nj.net')
if not user:
    login = User(username='admin@nj.net', password='enje123', roles=['admin'])
    login.hash_password()
    login.save()

# Running Flask Application when main class executed
if __name__ == '__main__':
    app.run()
