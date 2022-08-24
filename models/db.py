# Import from system libraries
from flask_mongoengine import MongoEngine

# Configuration for mongoose dataBase

db_config = [
    {
        "db": "project1",
        "host": "10.1.5.156",
        "port": 27017,
        "alias": "default",
    }
]

# MongoEngine load to db variable

db = MongoEngine()

# Function to initialize db to app


def initialize_db(app):
    db.init_app(app)
