from be import db
from be.models.doctor import Doctor , doctor_share_schema, doctors_share_schema
from be.utils.validation import *


# get all contacts from db
def getAllDoctors():
    print("Get all doctors")
    doctors = Doctor.query.all()
    return doctors_share_schema.dump(doctors)