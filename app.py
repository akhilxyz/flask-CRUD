# Import from system libraries
# from schedule import schedule
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_apscheduler import APScheduler
# Import from Applications modules
from controller.collectiveVault import CollectiveVaultController
from core.db.database import initialize_db, db_config
from core.models.UserModel import User
from core.models.chainsModel import chainDetails
from routes.api import initialize_routes
from errors import errors
from service.web3 import W3
from config.web3Config import PredictionEventStartBlockNo, ResolvePredictionEventStartBlockNo


# Scheduler for runnign every 1 min

def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!", flush=True)
    CollectiveVaultController()
    # ContractController()


scheduler = APScheduler()
scheduler.daemonic = False
scheduler.add_job(id='Scheduled Task', func=sensor,
                  trigger="interval", seconds=5)
scheduler.start()


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

network = chainDetails.objects(chainId=4)
if not network:
    blockNoPred = PredictionEventStartBlockNo
    blockNoResPer = ResolvePredictionEventStartBlockNo
    chainId = W3.eth.chain_id
    network = chainDetails(chainId=4, perBlockNo=blockNoPred,
                           resolvePerBlockNo=blockNoResPer)
    network.save()

# Running Flask Application when main class executed
if __name__ == '__main__':
    app.run()
