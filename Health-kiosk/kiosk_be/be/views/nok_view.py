from flask import Blueprint, jsonify, request
from be.controllers.nok_controller import *
from be.views.login_view import token_required

#register blueprint
next_of_ken_view = Blueprint('next_of_ken_view', __name__)


#Get all next of kins
@next_of_ken_view.route("/api/noks",methods=["GET"])
@token_required
def getAllNextOfKens(current_user):

    noks = getAllNOKs()
    return  jsonify({'next of kins': noks})



#Get next of kin by patient id
@next_of_ken_view.route("/api/noks/<id>",methods=["GET"])
@token_required
def getNextOfKenById(current_user,id):
    nok = getPatientNok(id)
    
    if nok== False:
        return  jsonify("Invalid id format"),422
    else:
        return  jsonify(nok)
    
    
# Create new next of kin
@next_of_ken_view.route("/api/noks/create",methods=["POST"])
def createNok():
    data = request.get_json()
    try:
        relationship = data['relationship']
        name = data['name']
        surname = data['surname']
        mobile = data['mobile']
        gender = data['gender']
        address = data['address']
        city = data['city']
        contact_hrs = data['contact_hrs']
        patientId = data['patientId']
       
        status = addNextOfKen(relationship,name,surname,mobile,gender,address,city,contact_hrs,patientId)
    except Exception as error:
        return jsonify({'result': error }),400
    
    if status == True:
        return jsonify({'result': 'success'}),201
    else:
        return jsonify({'result': status}),422
    
