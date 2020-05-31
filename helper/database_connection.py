import pyodbc

class DatabaseConnection():
    def connectToDatabase(self):
        connection = pyodbc.connect(
            Driver='{ODBC Driver 17 for SQL Server}',
            Server='DESKTOP-P2FHOP0\SQLEXPRESS',
            Database='AutomatedIrrigationSystem',
            ApplicationIntent='ReadWrite',
            UseFMTOnly='yes',
            Trusted_Connection='yes')

        return connection