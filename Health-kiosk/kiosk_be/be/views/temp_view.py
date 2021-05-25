from flask import Blueprint, jsonify, request
from be.controllers.temperature_controller import *
from be.controllers.test_tempreture_controller import *


#register blueprint
temp_view = Blueprint('temp_views', __name__)

#routes

#Get all stored sensor data
@temp_view.route("/api/temp",methods=["GET"])
def getCurrentResults():
    results = getTestData()
    return  jsonify({'results': results})

#start sensor reading
@temp_view.route("/api/temp/start",methods=["GET"])
def starting():
    state = startTestTempreture()
    return jsonify({'results': state})

#delete sensor data
@temp_view.route("/api/temp/del",methods=["DELETE"])
def deleting():
    state = deleteTestData()
    return jsonify({'Status': state})



