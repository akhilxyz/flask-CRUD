# Import from application modules
from core.usecases.loginCase import LoginApi
from core.usecases.userCase import User2Api, UserApi
from core.usecases.predictionsCase import Perdictions2Api
from core.usecases.resolvePredictionsCase import ResolvePerdictions2Api


# Function to initialize route to API Flask
def initialize_routes(api):
    api.add_resource(LoginApi, '/api/v1/login')
    api.add_resource(User2Api, '/api/v1/user')
    api.add_resource(UserApi, '/api/v1/user/<id>')
    # Collective Vault event api
    api.add_resource(Perdictions2Api, '/api/perdictions')
    api.add_resource(ResolvePerdictions2Api, '/api/resolveperdictions')
