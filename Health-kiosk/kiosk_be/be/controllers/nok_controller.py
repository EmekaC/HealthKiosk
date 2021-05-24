from be import db
from be.models.nok import Nextofken , nok_share_schema, noks_share_schema
from be.utils.validation import *


# get all contacts from db
def getAllNOKs():
    print("Get all next of kins")
    noks = Nextofken.query.all()
    return noks_share_schema.dump(noks)

# get the next of kin a patient
def getPatientNok(patientId):
    print("Get next of kin of a  patient")
    if validateId(patientId):
        nok = Nextofken.query.filter_by(patient_id=patientId).first_or_404(description='There is no record of pattient with id {}'.format(patientId))
        return nok_share_schema.dump(nok)
    else:
        return False
    
     
# adding a next of kin record  
def addNextOfKen(relationship,name,surname,mobile,gender,address,city,contact_hrs,patientId):
    print("Adding a new next of ken")
        
    validation = ( 
                   validateRelationship(relationship) and validateString(name) 
                    and validateString(surname) and validateMobile(mobile) 
                    and  validateGender(gender) and validateAddress(address)
                    and validateCity(city) and  validateId(patientId) 
                 )
    
    if validation:
        nok = Nextofken(relationship,name,surname,mobile,gender,address,city,patientId,contact_hrs)
        try: 
            db.session.add(nok)
            db.session.commit()
            return True
        except Exception as error:
            db.session.flush()
            db.session.rollback()
            return str(error)
    else:
        if not validateId(patientId):
            return "Invalid id card"
        elif not validateRelationship(relationship):
            return "Invalid relationship "
        elif not validateString(name):
            return "Invalid name"
        elif not validateString(surname):
            return "Invalid surname"
        elif not validateMobile(mobile):
            return "Invalid mobile"
        elif not validateGender(gender):
            return "Invalid gender"
        elif not validateAddress(address):
            return "Invalid address"
        else:
            return "Invalid city"
        
               
           