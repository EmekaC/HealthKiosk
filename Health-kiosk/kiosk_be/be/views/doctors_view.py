from flask import Blueprint, jsonify, request
from be.controllers.doctors_controller import *
from be.views.login_view import token_required

#register blueprint
doctor_view = Blueprint('doctor_view', __name__)


#Get all next of kins
@doctor_view.route("/api/docs",methods=["GET"])
def getAllDocs():
    docs = getAllDoctors()
    return  jsonify({'doctors': docs})
