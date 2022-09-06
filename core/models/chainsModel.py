# Import from application modules
from core.db.database import db

# Object Document Model (ODM) for Multichain Objects


class chainDetails(db.Document):
    chainId = db.IntField(required=True)
    perBlockNo = db.IntField(required=True)
    resolvePerBlockNo = db.IntField(required=True)
