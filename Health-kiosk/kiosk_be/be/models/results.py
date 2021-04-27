import datetime
from flask import current_app
from flask_marshmallow.fields import fields
from be import db, ma

#Results table model
class Results(db.Model):
    resultNo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    temperature = db.Column(db.Numeric(4,2), nullable=False)
    weight = db.Column(db.Numeric(4,2), nullable=False)
    bloodOx = db.Column(db.Integer, nullable=False)
    heartRate = db.Column(db.Integer, nullable=False)
    taken_on = db.Column(db.DateTime, nullable=False)
    patientId = db.Column(db.String(8), db.ForeignKey('patients.id'),nullable=False)
    remarks = db.Column(db.String(),nullable=True)
    
    #Create new Results object
    def __init__(self,temperature,weight,bloodOx,heartRate,patientId):
        self.temperature = temperature
        self.weight = weight
        self.bloodOx = bloodOx
        self.heartRate = heartRate
        self.taken_on = datetime.datetime.now()
        self.patientId = patientId
        

    
#Results schema in order to serialize record
class ResultsSchema(ma.Schema):
    temperature = fields.Float()
    weight = fields.Float()
    class Meta:
        fields = ('resultNo', 'temperature', 'weight', 'bloodOx', 'heartRate', 'taken_on', 'remarks')
        ordered = True
        
        
# Methods used to serialise/deserialise db rows
result_share_schema = ResultsSchema()
results_share_schema = ResultsSchema(many=True)
