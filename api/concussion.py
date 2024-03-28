import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
import pandas as pd

from model.concussion import * # import everything from the model

concussion_api = Blueprint('concussion_api', __name__,
                   url_prefix='/api/concussion') # set up blueprint w URL

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(concussion_api) # define API
class ConcussionAPI: # define the class
    class _Concussion(Resource):
        def post(self): # post method used by frontend
            # get all the json-format data and enter into variables
            body = request.get_json()
            name = body.get('name')
            sex = body.get('sex')
            age = body.get('age')
            ht = body.get('ht')
            wt = body.get('wt')
            smoke = body.get('smoke')
            alcohol = body.get('alcohol')
            sleephrs = body.get('sleephrs')
            exercisehrs = body.get('exercisehrs')
            hitbox = body.get('hitbox')
            # build individual concussion case from variables
            case = pd.DataFrame({
                'name': [name],
                'sex': [sex],
                'age': [age],
                'ht': [ht],
                'wt': [wt],
                'smoke': [smoke],
                'alcohol': [alcohol],
                'sleephrs': [sleephrs],
                'exercisehrs': [exercisehrs],
                'hitbox': [hitbox],
            })
            # initConcussion from the model file
            initConcussion()
            # predict based on data passed in
            return jsonify(predict(case))
    # add _Concussion class to the built API
    api.add_resource(_Concussion, '/')

