from flask import Flask, request, jsonify
from flask.views import MethodView
import pyodbc
from json import dumps
from datetime import datetime

class IrrigationExecutionController(MethodView):
    def post(self):
        irrigation_system_id = request.json['irrigationSystemId']
        user_id = request.json['userId']

        try:
            connection = pyodbc.connect(
                Driver='{ODBC Driver 17 for SQL Server}',
                Server='BRSAOWN023741',
                Database='AutomatedIrrigationSystem',
                ApplicationIntent='ReadWrite',
                UseFMTOnly='yes',
                Trusted_Connection='yes')

            initial_execution_datetime = datetime.now()

            cursor =  connection.cursor()
            cursor.execute("""INSERT INTO dbo.IrrigationExecution OUTPUT INSERTED.Id
                           VALUES (?, ?, ?, ?)""", irrigation_system_id, initial_execution_datetime, None, user_id)

            irrigation_execution_id = cursor.fetchone()[0]

            cursor.commit()

            ## THE CALL TO ARDUINO GOES HERE

            final_execution_datetime = datetime.now()

            cursor = connection.cursor()
            cursor.execute("""UPDATE dbo.IrrigationExecution 
                              SET FinalExecutionDateTime = ?
                              WHERE Id = ? """, final_execution_datetime, irrigation_execution_id)

            cursor.commit()

            print(irrigation_execution_id)
        except Exception as ex:
            print(ex)
