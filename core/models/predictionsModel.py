from core.db.database import db

# Object Document Model (ODM) for Perdiction Event Objects


class Perdictions(db.Document):
    counter = db.IntField(required=True)
    predictionType = db.IntField(required=True)
    amount = db.DecimalField(required=True)
    price = db.DecimalField(required=True)
    token = db.StringField(required=True)
    totalAmount = db.DecimalField(required=True)
    endTime = db.IntField(required=True)
    status = db.BooleanField(required=True)
    chainId = db.IntField(required=True)
    transactionHash = db.StringField(required=True)
    user = db.StringField(required=True)
    blockNumber = db.IntField(required=True)
