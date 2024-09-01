import pyodbc

def get_connection():
    conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=AdventureWorks2022;Trusted_Connection=yes;')
    return conn
