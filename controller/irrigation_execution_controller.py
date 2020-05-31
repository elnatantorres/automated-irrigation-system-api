from flask import Flask, request, jsonify
from flask.views import MethodView
import pyodbc
from datetime import datetime
from service.authentication_service import AuthenticationService
from helper.database_connection import DatabaseConnection
from controller_arduino.controller_sensor import excution_irrigation

class IrrigationExecutionController(MethodView):
    def post(self):
        irrigation_system_id = request.json['irrigationSystemId']
        username = request.headers['Username']
        password = request.headers['Password']

        try:
            user_authentication = AuthenticationService.authenticate(self, username, password)

            if(user_authentication.isUserAuthenticated == False):
                return jsonify('User not authenticated')

            database_connection = DatabaseConnection()
            connection = database_connection.connectToDatabase() 

            initial_execution_datetime = datetime.now()

            cursor =  connection.cursor()
            cursor.execute("""INSERT INTO dbo.IrrigationExecution OUTPUT INSERTED.Id
                           VALUES (?, ?, ?, ?)""", irrigation_system_id, initial_execution_datetime, None, user_authentication.userId)

            irrigation_execution_id = cursor.fetchone()[0]

            cursor.commit()

            ## THE CALL TO ARDUINO GOES HERE
            try:
                excution_irrigation()
            except Exception as e:
                print(e)
            final_execution_datetime = datetime.now()

            cursor = connection.cursor()
            cursor.execute("""UPDATE dbo.IrrigationExecution 
                              SET FinalExecutionDateTime = ?
                              WHERE Id = ? """, final_execution_datetime, irrigation_execution_id)

            cursor.commit()
        except Exception as ex:
            print(ex)

    def get(self):
        username = request.headers['Username']
        password = request.headers['Password']

        try:
            user_authentication = AuthenticationService.authenticate(self, username, password)

            if(user_authentication.isUserAuthenticated == False):
                return jsonify('User not authenticated')

            database_connection = DatabaseConnection()
            connection = database_connection.connectToDatabase() 

            cursor =  connection.cursor()

            cursor.execute("SELECT * FROM dbo.IrrigationExecution")

            query_result = []
            rows = cursor.fetchall()
            for row in rows:
                query_result.append((row.Id, row.IrrigationSystemId, str(row.InitialExecutionDateTime), 
                str(row.FinalExecutionDateTime), row.UserId))

            print(query_result)

            return {'results':
                [dict(zip([column[0] for column in cursor.description], row))
                for row in query_result]}

        except Exception as ex:
            print(ex)