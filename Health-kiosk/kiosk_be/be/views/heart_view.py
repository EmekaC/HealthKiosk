from flask import Blueprint, jsonify, request
from be.controllers.heart_sensor_controller import *


#register blueprint
heart_view = Blueprint('heart_views', __name__)

#routes

#Get all stored sensor data
@heart_view.route("/api/heart",methods=["GET"])
def getCurrentResults():
    results = getData()
    return  jsonify({'results': results})

# start sensor reading
@heart_view.route("/api/heart/start",methods=["GET"])
def starting():
    state = startReadingHeartBeat()
    return jsonify({'results': state})

#delete sensor data 
@heart_view.route("/api/heart/del",methods=["DELETE"])
def deleting():
    state = deleteData()
    return jsonify({'Status': state})



