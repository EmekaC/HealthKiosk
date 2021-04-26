from be import db
from be.models.patient import Patients, patient_share_schema, patients_share_schema
from be.utils.validation import *

#get all registered patients in database
def getPatients():
    print("Get all patients")
    
    patients = Patients.query.all()
    return patients_share_schema.dump(patients)

#get all active patients
def getActivePatients():
    print("Getting all active patients")
    
    patients = Patients.query.filter(Patients.active == 1)
    return patients_share_schema.dump(patients)

#get patient by id serializable
def getPatientById(patientId):
    print("Get patient by id")
    
    if validateId(patientId):
        patient = Patients.query.filter_by(id=patientId).first_or_404(description='There is no data with {}'.format(patientId))
        return patient_share_schema.dump(patient)
    else:
        return False

#get patient by id
def getPatient(patientId):
    print("Get patient by id for login")
    if validateId(patientId):
        patient = Patients.query.filter_by(id=patientId).first()
        if patient:
            return patient
        else:
            "No record found"
    else:
        return "Invalid id"


# add new patient -> register
def createPatient(patientId,name,surname,mobile,gender,dob,address,city,marital_status,siblings,email,password):
    print("Create patient")
    validation = (
                    validateId(patientId) and validateString(name) 
                    and validateString(surname) and validateDOB(dob) 
                    and validateEmail(email) and validatePassword(password) 
                    and validateString(city) and validateMobile(mobile) 
                    and validateGender(gender) and validateMartialStatus(marital_status)
                    and validateSiblings(siblings)
                )       
    
    if validation:
            if Patients.query.filter_by(id=patientId).first():
                return "Patient already exists"
            else :
                newPatient = Patients(patientId,name,surname,mobile,gender,dob,address,city,marital_status,siblings,email,password)
                try: 
                    db.session.add(newPatient)
                    db.session.commit()
                    return True
                except Exception as error:
                    db.session.flush()
                    db.session.rollback()
                    return str(error)
    else :
        if not validateId(patientId):
            return "Invalid id"
        elif not validateString(name):
            return "Invalid name"
        elif not validateString(surname):
            return "Invalid surname"
        elif not validateDOB(dob):
            return "Invalid dob"
        elif not validateEmail(email):
            return "Invalid email"
        elif not validatePassword(password):
            return "Invalid password"
        elif not validateString(city):
            return "Invalid city"
        elif not validateGender(gender):
            return "Invalid gender"
        elif not validateSiblings(siblings):
            return "Invalid sibling option"
        elif not validateMartialStatus(marital_status):
            return "Invalid martial status"
        else: 
            return "Invalid mobile"
        
            
# delete patient -> deactivate 
def deletePatient(patientId):
    print("Delete patient")
    if validateId(patientId):
        deletePatient = Patients.query.filter_by(id=patientId).first_or_404(description='There is no data with {}'.format(patientId))
        deletePatient.active = 0
        try: 
            db.session.commit()
            return True
        except Exception as error:
            db.session.flush()
            db.session.rollback()
            return str(error)
    else:
        return "Invalid ID"


# update patient details
def updatePatient(patientId,key,value):
    print("Update patient")

    if validateId(patientId):
        updatePatient = Patients.query.filter_by(id=patientId).first_or_404(description='There is no data with {}'.format(patientId))
  
        if key == 'name':
            if validateString(value):
                updatePatient.name = value
            else:
                return "Invalid name"
        elif key == 'surname':
            if validateString(value):
                updatePatient.surname = value
            else:
                return "Invalid surname"
        elif key == 'email':
            if validateEmail(value):
                updatePatient.email = value
            else:
                return "Invalid email"
        elif key == 'address':
            updatePatient.address = value
        elif key == 'city':
            if validateString(value):
                updatePatient.city = value
            else:
                return "Invalid city"
        elif key == 'gender':
            if validateGender(value):
                updatePatient.gender = value
            else:
                return "Invalid gender"
        elif key == 'marital_status':
            if validateMartialStatus(value):
                updatePatient.marital_status = value
            else:
                return "Invalid marital status"
        else:
            if validateMobile(value):
                updatePatient.mobile = value
            else:
                return "Invalid mobile"
    
        try: 
            db.session.commit()
            return True
        except Exception as error:
            db.session.flush()
            db.session.rollback()
            return str(error)
    else:
        return "Invalid ID"
