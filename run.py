from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from controller.irrigation_execution_controller import IrrigationExecutionController

app = Flask(__name__)
api = Api(app)

api.add_resource(IrrigationExecutionController, '/irrigation-execution') 

if __name__ == '__main__':
    app.run()