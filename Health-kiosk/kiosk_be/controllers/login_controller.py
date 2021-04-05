from kiosk_be import app
from kiosk_be.controllers.patients_controller import getPatient
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime




def login(userId, userPass):
    patient = getPatient(userId)
    password = generate_password_hash(patient.password)

    if  patient and check_password_hash(password,userPass):
        print(patient.id)
        print(app.config['SECRET_KEY'])
        token = jwt.encode({'id' : patient.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'],algorithm="HS512")
        return token

    else:
        return "Invalid credentials"