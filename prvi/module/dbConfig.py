import mysql.connector

def dbConnector():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "aaa"
    )