import mysql.connector
db=mysql.connector.connect(host="localhost",user="user",passwd="pass123",database="password_manager")
cursor=db.cursor()
def insert_cred(self,web,user,pwd): 
    cursor.execute("SELECT WEBSITE FROM DETAILS")
    cols=cursor.fetchall()
    if(web,) in cols: 
        print("Credentials already exist! Kindly delete the existing ones to change the credentials.")
    else:
        insert_cmd="INSERT INTO DETAILS (WEBSITE,USERNAME,PASSWORD) VALUES (%s,%s,%s)"
        vals=(web,user,pwd)
        cursor.execute(insert_cmd,vals)
        db.commit()
        print("Credentials added successfully!")
def display_all(self):
    print("Your credentials: \n")
    cursor.execute("SELECT * FROM DETAILS")
    table=cursor.fetchall()
    print("(Website,Username,Password)")
    print("")
    for row in table:
        print(row)
    print("")
def display_creds(self,web): 
    sel_stat="SELECT * FROM DETAILS WHERE WEBSITE=%s"
    val=(web,)
    cursor.execute(sel_stat,val)
    cred=cursor.fetchone()
    print("")
    print("Credentials for "+web+":\nUsername: ",cred[1],"\nPassword: ",cred[2])
    print("")
    return cred
def delete_cred(self,web): 
    cursor.execute("SELECT WEBSITE FROM DETAILS")
    cols=cursor.fetchall()
    if(web,) in cols: 
        del_stat="DELETE FROM DETAILS WHERE WEBSITE=%s"
        val=(web,)
        cursor.execute(del_stat,val)
        db.commit()
        print("Credentials deleted successfully!")
    else:
        print("No such details found! Please check your input.")
    print("")
