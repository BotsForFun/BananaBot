import mysql.connector
import os

mydb = mysql.connector.connect(
    host=os.environ.get("HOST"),
    user=os.environ.get("USERNAME"),
    password=os.environ.get("PASSWORD"),
    database=os.environ.get("DATABASE"),
    auth_plugin="mysql_native_password"
)


def checkserverprefix():
    mycursor = mydb.cursor()

