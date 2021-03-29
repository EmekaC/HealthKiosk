from flask import render_template,Blueprint, jsonify, request
from kiosk_be.controllers.patients_controller import *

#register blueprint
patients_view = Blueprint('patients_view', __name__)

#routes
@patients_view.route("/",methods=["GET"])
def getPats():
    patients = getPatients()
    return  jsonify(patients)

@patients_view.route("/<id>",methods=["GET"])
def getPatById(id):
    patient = getPatientById(id)
    return  jsonify(patient)

@patients_view.route("/create",methods=["POST"])
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
        return jsonify({'result': status})


@patients_view.route("/delete/<id>",methods=["DELETE"])
def deletePat(id):
    status = deletePatient(id)

    if status == True:
        return jsonify({'result': 'success'}),201
    else:
        return jsonify({'result': status})


@patients_view.route("/update/<id>",methods=["PUT"])
def updatePat(id):
    data = request.get_json()
 
    for row in data:
        field = row['key']
        value = row['value']
        status = updatePatient(id,field,value)
        
    if status == True:
        return jsonify({'result': 'success'}),201
    else:
        return jsonify({'result': status})

    
    