import pyodbc
from helper.database_connection import DatabaseConnection

class AuthenticationService():
    def authenticate(self, username, password):
        try:
            database_connection = DatabaseConnection()
            connection = database_connection.connectToDatabase() 

            cursor =  connection.cursor()
            cursor.execute("""SELECT
                                    'UserId' = Id,
                                    'Password' = Password
                                FROM 
                                    AutomatedIrrigationSystem.auth.[User]
                                WHERE
                                    Username = ?""", username)

            user = cursor.fetchall()

            user_id = user[0].UserId
            password_from_database = user[0].Password

            is_user_authenticated = None

            if password_from_database == password:
                is_user_authenticated = True
            else:
                is_user_authenticated = False

            userAuthentication = UserAuthentication(user_id, is_user_authenticated)

            return userAuthentication
        except Exception as ex:
            print(ex)

class UserAuthentication():
    def __init__(self, user_id, is_user_authenticated):
        self.userId = user_id
        self.isUserAuthenticated = is_user_authenticated