import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.recovery import * # import everything from the model

recovery_api = Blueprint('recovery_api', __name__,
                   url_prefix='/api/recovery') # set up blueprint w URL

api = Api(recovery_api) # define API
class RecoveryAPI: # define the class
    class _Recovery(Resource):
        def post(self):
            body = request.get_json()
            # process the stuff in the body 
            patient = [] # store processed stuff in patient list
            # then pass to model file + give the suggestions 
            return jsonify(recovery(patient))