from flask import Blueprint, jsonify, request
from be.controllers.selections_controller import *

#register blueprint
selections_view = Blueprint('selection_view', __name__)


#Get genders
@selections_view .route("/api/genders",methods=["GET"])
def getAllGenders():

    genders = getGenders()
    return  jsonify({'genders': genders})


#Get relationships
@selections_view .route("/api/relationships",methods=["GET"])
def getAllRelationshios():

    relations = getRelations()
    return  jsonify({'relationships': relations})

#Get statuses
@selections_view .route("/api/status",methods=["GET"])
def getAllStatuses():

    status = getStatuses()
    return  jsonify({'status': status})

#Get communications
@selections_view .route("/api/communication",methods=["GET"])
def getAllCommonications():

    communication = getCommunications()
    return  jsonify({'communications': communication})



