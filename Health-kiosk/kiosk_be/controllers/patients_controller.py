from kiosk_be import db
from kiosk_be.models.patient import Patient, patient_share_schema, patients_share_schema
from kiosk_be.utils.validation import *

def getPatients():
    print("Get all patients")

    patients = Patient.query.all()
    return patients_share_schema.dump(patients)

def getPatientById(patientId):
    print("Get patient by id")
    if validateId(patientId):
        patient = Patient.query.with_entities(Patient.name,Patient.surname).filter_by(id=patientId).first_or_404(description='There is no data with {}'.format(patientId))
        return patient_share_schema.dump(patient)
    else:
        return False

def createPatient(patientId,name,surname,dob,email,password,address,city,mobile):
    print("Create patient")
    validation = (
                    validateId(patientId) and validateString(name) 
                    and validateString(surname) and validateDOB(dob) 
                    and validateEmail(email) and validatePassword(password) 
                    and validateString(city) and validateMobile(mobile)
                )       
    
    if validation:
            if Patient.query.filter_by(id=patientId).first():
                return "Patient already exists"
            else :
                newPatient = Patient(patientId,name,surname,dob,email,password,address,city,mobile)
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
        else: 
           return "Invalid mobile"
        
            
    
def deletePatient(patientId):
    print("Delete patient")
    if validateId(patientId):
        deletePatient = Patient.query.filter_by(id=patientId).first_or_404(description='There is no data with {}'.format(patientId))
        try: 
            db.session.delete(deletePatient)
            db.session.commit()
            return True
        except Exception as error:
            db.session.flush()
            db.session.rollback()
            return str(error)
    else:
        return "Invalid ID"


def updatePatient(patientId,key,value):
    print("Update patient")

    if validateId(patientId):
        updatePatient = Patient.query.filter_by(id=patientId).first_or_404(description='There is no data with {}'.format(patientId))
  
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
