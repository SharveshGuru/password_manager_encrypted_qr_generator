import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="pass123"
)
cursor=db.cursor()
cursor.execute("CREATE DATABASE PASSWORD_MANAGER")
cursor.execute("USE PASSWORD_MANAGER")
pm_table='''CREATE TABLE DETAILS(WEBSITE VARCHAR(50) NOT NULL, USERNAME VARCHAR(50) NOT NULL, PASSWORD VARCHAR(50) NOT NULL)'''
cursor.execute(pm_table)