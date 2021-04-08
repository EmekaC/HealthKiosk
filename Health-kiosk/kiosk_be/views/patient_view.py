from flask import Blueprint, jsonify, request
from kiosk_be.controllers.patients_controller import *
from kiosk_be.views.login_view import token_required

#register blueprint
patients_view = Blueprint('patients_view', __name__)

#routes

#Get all patients
@patients_view.route("/api/patients",methods=["GET"])
@token_required
def getAllPatients(current_user):
    print(current_user)
    patients = getPatients()
    return  jsonify(patients)

#Get patient bu id
@patients_view.route("/api/patients/<id>",methods=["GET"])
@token_required
def getPatById(current_user,id):
    patient = getPatientById(id)
    
    if patient== False:
        return  jsonify("Invalid id format"),422
    else:
        return  jsonify(patient)
    

# Create new patient account
@patients_view.route("/api/patients/create",methods=["POST"])
def createPat():
    data = request.get_json()
    id = data['id']
    name = data['name']
    surname = data['surname']
    dob = data['dob']
    email = data['email']
    password =data['password']
    address = data['address']
    city = data['city']
    mobile = data['mobile']

    status = createPatient(id,name,surname,dob,email,password,address,city,mobile)

    if status == True:
        return jsonify({'result': 'success'}),201
    else:
        return jsonify({'result': status}),422


# Delete patient account
@patients_view.route("/api/patients/delete/<id>",methods=["DELETE"])
@token_required
def deletePat(current_user,id):
    status = deletePatient(id)

    if status == True:
        return jsonify({'result': 'success'}),200
    else:
        return jsonify({'result': status})


# Update patient details 
@patients_view.route("/api/patients/update/<id>",methods=["PUT"])
@token_required
def updatePat(current_user,id):
    data = request.get_json()
    for row in data:
        field = row['key']
        value = row['value']
        status = updatePatient(id,field,value)
        
    if status == True:
        return jsonify({'result': 'success'}),201
    else:
        return jsonify({'result': status})
