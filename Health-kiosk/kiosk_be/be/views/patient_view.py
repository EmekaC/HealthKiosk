from flask import Blueprint, jsonify, request, redirect, url_for
from be.controllers.patients_controller import *
from be.views.login_view import token_required
from be.views.nok_view import createNok

#register blueprint
patients_view = Blueprint('patients_view', __name__)

#routes

#Get all patients
@patients_view.route("/api/patients",methods=["GET"])
@token_required
def getAllPatients(current_user):
    
    patients = getPatients()
    return  jsonify({'patients': patients})

#Get all active patients
@patients_view.route("/api/patients/active",methods=["GET"])
@token_required
def getAllActivePatients(current_user):
    
    patients = getActivePatients()
    return  jsonify({'patients': patients})


#Get patient by id
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
    try:
        id = data['id']
        name = data['name']
        surname = data['surname']
        mobile = data['mobile']
        gender = data['gender']
        dob = data['dob']
        address = data['address']
        city = data['city']
        marital_status = data['marital_status']
        siblings = data['siblings']
        email = data['email']
        password =data['password']
        doctor_id = data['doctor']
        
        status = createPatient(id,name,surname,mobile,gender,dob,address,city,marital_status,siblings,email,password,doctor_id)
    except Exception as error:
        return jsonify({'result': error }),400
    
    if status == True:
      return jsonify({'result': 'success'}),201
      #return redirect(url_for('next_of_ken_view.createNok'),code=307)
    else:
        return jsonify({'result': status}),422


# Delete patient account (set patient to deactive)
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
        try:
            field = row['key']
            value = row['value']
            status = updatePatient(id,field,value)
        except Exception as error:
            return jsonify({'result': error }),400
        
    if status == True:
        return jsonify({'result': 'success'}),201
    else:
        return jsonify({'result': status})
