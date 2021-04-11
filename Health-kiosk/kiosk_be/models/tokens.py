import datetime
from flask import current_app
from kiosk_be import db, ma

#Tokens table model
class Tokens(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), nullable=False, unique=True)
    exp = db.Column(db.DateTime, nullable=False)
    revoked_on = db.Column(db.DateTime, nullable=False)
    
    #Create new Token object
    def __init__(self,token,exp):
        self.token = token
        self.exp = exp
        self.revoked_on = datetime.datetime.now()
    
#Tokens schema in order to serialize record    
class TokensSchema(ma.Schema):
    class Meta:
        fields = ('id', 'token','exp','revoked_on')
        ordered = True

# Methods used to serialise/deserialise db rows        
token_share_schema = TokensSchema()
tokens_share_schema = TokensSchema(many=True)