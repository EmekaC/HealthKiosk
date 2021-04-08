from kiosk_be import db
from kiosk_be.models.results import Results , result_share_schema , results_share_schema 
from kiosk_be.utils.validation import *


# get all results from db
def getAllResults():
    print("Get all results")
    results = Results.query.all()
    print(results)
    return results_share_schema.dump(results)


# get all the results of a patient
def getPatientResults(patientId):
    print("Get results of a specific patient")
    if validateId(patientId):
        results = Results.query.filter_by(patientId=patientId).order_by(Results.taken_on).all()
        return results_share_schema.dump(results)
    else:
        return False

# add a new result record   
def addResult(temperature, weight, bloodOx, heartRate, patientId):
    print("Adding a new result")
    
    validation = ( 
                   validateId(patientId) and validateTemperature(temperature)
                   and validateWeight(weight) and validateBloodOx(bloodOx)
                   and validateHeartPulse(heartRate)
                 )
    print(validation)
    if validation:
        newResult = Results(temperature,weight,bloodOx,heartRate,patientId)
        try: 
            db.session.add(newResult)
            db.session.commit()
            return True
        except Exception as error:
            db.session.flush()
            db.session.rollback()
            return str(error)
    else:
        if not validateId(patientId):
            return "Invalid id card"
        elif not validateWeight(weight):
            return "Invalid weight value"
        elif not validateTemperature(temperature):
            return "Invalid temperature value"
        elif not validateBloodOx(bloodOx):
            return "Invalid blood oxygen value"
        else:
            return "Invalid pulse rate"

