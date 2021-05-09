from flask import Blueprint, jsonify, request
from be.controllers.heart_controller import *


#register blueprint
heart_view = Blueprint('heart_views', __name__)

#routes

#Get all patients
@heart_view.route("/api/heart",methods=["GET"])
def getCurrentResults():
    results = getData()
    return  jsonify({'results': results})


@heart_view.route("/api/heart/start",methods=["GET"])
def starting():
    state = startReading()
    return jsonify({'results': state})

@heart_view.route("/api/heart/del",methods=["DELETE"])
def deleting():
    state = deleteData()
    return jsonify({'Status': state})



