import datetime
from flask import current_app
from be import db, ma
from be.models.results import Results

#Patient table model
class Patients(db.Model):
    id = db.Column(db.String(8),primary_key=True, unique=True, nullable=False)
    active = db.Column(db.Boolean, default='1', nullable=False)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    mobile = db.Column(db.Integer, nullable=False, unique=True)
    gender = db.Column(db.Enum('Male','Female','Other'),nullable=False)
    dob = db.Column(db.Date(), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    marital_status = db.Column(db.Enum('Single','Married','Domestic Partnership','Divorced'),nullable=False)
    siblings = db.Column(db.Boolean, default='0', nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(14), nullable=False)
    deceased = db.Column(db.Boolean, default='0', nullable=False)
    deceased_date = db.Column(db.DateTime, nullable=True)
    photo = db.Column(db.LargeBinary(length=(2**32)-1), nullable=True)
    general_practitioner = db.Column(db.Integer, nullable=True)
    managed_organization = db.Column(db.String(45), nullable=True)
    communitcation = db.Column(db.Enum('English','Maltese','Italian','French'),nullable=False, default='English')
    
    
    
    #results = db.relationship('Results', backref='patient')

    #Create new Patient object
    def __init__ (self,id,name ,surname ,mobile ,gender ,dob ,address ,city ,marital_status ,siblings ,email, password): 
        self.id = id
        self.active = 1
        self.name = name
        self.surname = surname
        self.mobile = mobile
        self.gender = gender
        self.dob = dob
        self.address = address
        self.city = city
        self.marital_status = marital_status
        self.siblings = siblings
        self.email = email
        self.password = password
        self.deceased = 0
        self.communitcation = 'English'
        
        
        
        

    
#Patient schema in order to serialize record
class PatientsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'surname', 'mobile', 'gender', 'dob', 'address', 'city','marital_status','siblings','email','general_practitioner','communitcation')
        ordered = True

# Methods used to serialise/deserialise db rows
patient_share_schema = PatientsSchema()
patients_share_schema = PatientsSchema(many=True)