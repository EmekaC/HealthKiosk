import datetime
from flask import current_app
from be import db, ma


#Next of kin table model
class Nextofken(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    relationship = db.Column(db.Enum('Mother','Father','Parent','Brother','Sister','Son','Daughter','Child','Friend','Spouse','Partner','Family member','Carer','Social worker','Guardian','Other'),nullable=False)
    patient_id = db.Column(db.String(8), db.ForeignKey('patients.id'),nullable=False, unique=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    mobile = db.Column(db.Integer, nullable=False, unique=True)
    gender = db.Column(db.Enum('Male','Female','Other'),nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(45), nullable=False) 
    contact_hrs = db.Column(db.String(), nullable=True)
    
    
    def __init__(self,relationship,name,surname,mobile,gender,address,city,patient_id,contact_hrs= ""):
        self.relationship = relationship
        self.name = name
        self.surname = surname
        self.mobile = mobile
        self.gender = gender
        self.address = address
        self.city = city
        self.contact_hrs = contact_hrs
        self.patient_id = patient_id
        
        
    
#Next of Kin schema in order to serialize record
class NOKSchema(ma.Schema):
    class Meta:
        fields = ( 'relationship', 'name', 'surname', 'mobile', 'gender', 'address','city','contact_hrs')
        ordered = True
        
        
# Methods used to serialise/deserialise db rows
nok_share_schema = NOKSchema()
noks_share_schema = NOKSchema(many=True)

       
        