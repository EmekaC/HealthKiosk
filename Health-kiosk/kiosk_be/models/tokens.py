import datetime
from flask import current_app
from kiosk_be import db, ma


class Tokens(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), nullable=False, unique=True)
    exp = db.Column(db.DateTime, nullable=False)
    revoked_on = db.Column(db.DateTime, nullable=False)
    
    def __init__(self,token,exp):
        self.token = token
        self.exp = exp
        self.revoked_on = datetime.datetime.now()
    
    
class TokensSchema(ma.Schema):
    class Meta:
        fields = ('id', 'token','exp','revoked_on')
        ordered = True
        
token_share_schema = TokensSchema()
tokens_share_schema = TokensSchema(many=True)