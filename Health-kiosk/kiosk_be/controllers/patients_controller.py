from kiosk_be import db
from kiosk_be.models.patient import Patient, patient_share_schema, patients_share_schema

def getPatients():
    print("Get all patients")

    patients = Patient.query.all()
    return patients_share_schema.dump(patients)

def getPatientById(patientId):
    print("Get patient by id")

    patient = Patient.query.with_entities(Patient.name,Patient.surname).filter_by(id=patientId).first_or_404(description='There is no data with {}'.format(patientId))
    return patient_share_schema.dump(patient)

def createPatient(patientId,name,surname,dob,email,password,address,city,mobile):
    print("Create patient")

    newPatient = Patient(patientId,name,surname,dob,email,password,address,city,mobile)
    try: 
        db.session.add(newPatient)
        db.session.commit()
        return True
    except Exception as error:
        db.session.flush()
        db.session.rollback()
        return error
    
def deletePatient(patientId):
    print("Delete patient")

    deletePatient = Patient.query.filter_by(id=patientId).first()
    try: 
        db.session.delete(deletePatient)
        db.session.commit()
        return True
    except Exception as error:
        db.session.flush()
        db.session.rollback()
        return error


def updatePatient(patientId,key,value):
    print("Update patient")

    updatePatient = Patient.query.filter_by(id=patientId).first()
  
    if key == 'name':
        updatePatient.name = value
    elif key == 'surname':
        updatePatient.surname = value
    elif key == 'email':
        updatePatient.email = value
    elif key == 'address':
        updatePatient.address = value
    elif key == 'city':
        updatePatient.city = value
    else:
        updatePatient.mobile = value
    
    try: 
        db.session.commit()
        return True
    except Exception as error:
        db.session.flush()
        db.session.rollback()
        return error
