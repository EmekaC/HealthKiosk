from flask import Blueprint, jsonify, request
from be.controllers.temperature_controller import *


#register blueprint
temp_view = Blueprint('temp_views', __name__)

#routes

#Get all stored sensor data
@temp_view.route("/api/temp",methods=["GET"])
def getCurrentResults():
    results = getData()
    return  jsonify({'results': results})

#start sensor reading
@temp_view.route("/api/temp/start",methods=["GET"])
def starting():
    state = startTempreture()
    return jsonify({'results': state})

#delete sensor data
@temp_view.route("/api/temp/del",methods=["DELETE"])
def deleting():
    state = deleteData()
    return jsonify({'Status': state})



