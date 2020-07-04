import mysql.connector
import os

mydb = mysql.connector.connect(
    host=os.environ.get("HOST"),
    user=os.environ.get("USERNAME"),
    password=os.environ.get("PASSWORD"),
    database=os.environ.get("DATABASE"),
    auth_plugin="mysql_native_password"
)


def checkserverprefix(server_id):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM %s"
    val = (f"{server_id}",)
    mycursor.execute(sql, val)
    results = mycursor.fetchall()
    for row in results:
        prefix = row[1]
    return prefix


