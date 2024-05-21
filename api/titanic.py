import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
import pandas as pd

from model.titanic import *

model_api = Blueprint('model_api', __name__,
                   url_prefix='/api/titanic')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(model_api) # start up the API
class TitanicAPI:
    class _Titanic(Resource):
        def post(self):
            # get all the json-format data and enter into variables
            body = request.get_json()
            name = body.get('name')
            pclass = body.get('pclass')
            sex = body.get('sex')
            age = body.get('age')
            fmem = body.get('fmem')
            fare = body.get('fare')
            embark = body.get('embark')
            # build new passenger from data given from frontend
            passenger = pd.DataFrame({
                'name': [name],
                'pclass': [pclass],
                'sex': [sex],
                'age': [age],
                'sibsp': [fmem], 
                'parch': [fmem], 
                'fare': [fare], 
                'embarked': [embark], 
                'alone': [True if fmem == 0 else False]
            })
            initTitanic()
            # initialize model and return the survival prediction
            return predictSurvival(passenger)
    api.add_resource(_Titanic, '/')

