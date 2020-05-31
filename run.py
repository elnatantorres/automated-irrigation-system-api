from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from controller.irrigation_execution_controller import IrrigationExecutionController
from controller_arduino.while_true_sensor import irrigation

app = Flask(__name__)
api = Api(app)

api.add_resource(IrrigationExecutionController, '/irrigation-execution') 

if __name__ == '__main__':
    app.run()
    # irrigation