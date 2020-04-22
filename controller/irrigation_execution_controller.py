from flask import Flask, request, jsonify
from flask.views import MethodView
from sqlalchemy import create_engine
from json import dumps

class IrrigationExecutionController(MethodView):
    def post(self):
        irrigation_system_id = request.json['irrigationSystemId']
        user_id = request.json['userId']

        print(irrigation_system_id)
        print(user_id)
