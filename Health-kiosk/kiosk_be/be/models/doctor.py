import datetime
from flask import current_app
from be import db, ma


#Doctor table model
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    mobile = db.Column(db.Integer, nullable=False, unique=True)
    patients = db.relationship('Patients', backref='patients')
    
    
    def __init__(self,name,surname,email,mobile):
        self.name = name
        self.surname = surname
        self.email = email
        self.mobile = mobile
        
        

#Doctor schema in order to serialize record
class DoctorSchema(ma.Schema):
    class Meta:
        fields = ( 'id','name', 'surname', 'email', 'mobile')
        ordered = True
        
        
# Methods used to serialise/deserialise db rows
doctor_share_schema = DoctorSchema()
doctors_share_schema = DoctorSchema(many=True)

       
        