import datetime
from flask import current_app
from be import db, ma

#Heart table model
class Heart(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    heartbeat = db.Column(db.Integer,nullable=False)
    oxygen = db.Column(db.Integer, nullable=False)
    
    def __init__(self,heartbeat,oxygen):
        self.heartbeat = heartbeat
        self.oxygen = oxygen
       
        
        
    
#Heart schema in order to serialize record
class HeartSchema(ma.Schema):
    class Meta:
        fields = ( 'id', 'heartbeat', 'oxygen')
        ordered = True
        
        
# Methods used to serialise/deserialise db rows
heart_share_schema = HeartSchema()
hearts_share_schema = HeartSchema(many=True)

       