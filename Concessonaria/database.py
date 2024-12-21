import pyodbc

def con():
    return pyodbc.connect(
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=localhost;'
        'Database=concessionariaDB;'
        'UID=sa;'
        'PWD=1234;'
    )
