import datetime
from flask import current_app
from flask_marshmallow.fields import fields
from be import db, ma

#Temp table model
class Temp(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    temperature = db.Column(db.Numeric(4,2), nullable=False)
   
    
    def __init__(self,temperature):
        self.temperature = temperature
       
        
#Temperature schema in order to serialize record
class TempSchema(ma.Schema):
    temperature = fields.Float()
    class Meta:
        fields = ( 'id', 'temperature')
        ordered = True
        
        
# Methods used to serialise/deserialise db rows
temp_share_schema = TempSchema()
tempss_share_schema = TempSchema(many=True)

       