import datetime
from flask import current_app
from kiosk_be import db, ma
from kiosk_be.models.results import Results

#Patient table model
class Patient(db.Model):
    id = db.Column(db.String(8),primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    dob = db.Column(db.Date(), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(14), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    mobile = db.Column(db.Integer, nullable=False, unique=True)
    results = db.relationship('Results', backref='patient')

    #Create new Patient object
    def __init__(self,id,name,surname,dob,email,password,address,city,mobile):
        self.id = id
        self.name = name
        self.surname = surname
        self.dob = dob
        self.email = email
        self.password = password
        self.address = address
        self.city = city
        self.mobile = mobile

    
#Patient schema in order to serialize record
class PatientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'surname', 'dob', 'email', 'address', 'city', 'mobile')
        ordered = True

# Methods used to serialise/deserialise db rows
patient_share_schema = PatientSchema()
patients_share_schema = PatientSchema(many=True)