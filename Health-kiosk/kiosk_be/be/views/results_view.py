from flask import Blueprint, jsonify, request
from be.controllers.results_controller import *
from be.views.login_view import token_required


#register blueprint
results_view = Blueprint('results_view', __name__)

#Routes

#Get all results
@results_view.route("/api/results",methods=["GET"])
@token_required
def getResult(current_user):
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
    try:
        patientId = data['id']
        temperature = data['temperature']
        weight = float(data['weight'])
        bloodOx = data['bloodOx']
        heartRate = data['heartRate']
        status = addResult(temperature,weight,bloodOx,heartRate,patientId)
    except Exception as error:
        return jsonify({'result': 'Missing fields in array'}),400
    
    if status == True:
        return jsonify({'result': 'success'}),201
    else:
        return jsonify({'result': status}),422
    

# Add remark by patient id and date of result 
@results_view.route("/api/results/remarks/<id>",methods=["PUT"])
def addResultRemark(id):
    data = request.get_json()
    for row in data:
        try:
            date = row['date']
            remarks = row['remark']
            status = addRemark(id,date,remarks)
        except Exception as error:
            return jsonify({'result': 'Missing fields in array'}),400
        
    if status == True:
        return jsonify({'result': 'success'}),201
    else:
        return jsonify({'result': status})
