from flask import Blueprint, jsonify, request
from kiosk_be.controllers.results_controller import *
from kiosk_be.views.login_view import token_required


#register blueprint
results_view = Blueprint('results_view', __name__)

#Routes

#Get all results
@results_view.route("/api/results",methods=["GET"])
def getResult():
    results = getAllResults()
    return  jsonify(results)

# Get results by patient id
@results_view.route("/api/results/<id>",methods=["GET"])
@token_required
def getPatientsResult(current_user,id):
    results = getPatientResults(id)
    return  jsonify(results)

# Add new result
@results_view.route("/api/results/add",methods=["POST"])
@token_required
def addPatientResult(current_user):
    data = request.get_json()
    patientId = data['id']
    temperature = data['temperature']
    weight = data['weight']
    bloodOx = data['bloodOx']
    heartRate = data['heartRate']
    
    status = addResult(temperature,weight,bloodOx,heartRate,patientId)
    
    if status == True:
        return jsonify({'result': 'success'}),201
    else:
        return jsonify({'result': status}),422
