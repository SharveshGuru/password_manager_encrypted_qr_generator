#importing all required libraries
import mysql.connector
import qrcode
import cv2
from fuzzywuzzy import fuzz
from cryptography.fernet import Fernet
with open('fernet_key.txt', 'rb') as f:
    key = f.read()
#connecting mysql to python
db=mysql.connector.connect(host="localhost",user="user",passwd="pass123",database="password_manager")
cursor=db.cursor()
#creating a class for password manager
class Pass_Man:
    def insert_cred(self,web,user,pwd): #method to insert data
        cursor.execute("SELECT WEBSITE FROM DETAILS")
        cols=cursor.fetchall()
        if(web,) in cols: #to check if already the website exists
            print("Credentials already exist! Kindly delete the existing ones to change the credentials.")
        else:
            insert_cmd="INSERT INTO DETAILS (WEBSITE,USERNAME,PASSWORD) VALUES (%s,%s,%s)"
            vals=(web,user,pwd)
            cursor.execute(insert_cmd,vals)
            db.commit()
            print("Credentials added successfully!")
    def display_all(self): #method to display all credentials
        print("Your credentials: \n")
        cursor.execute("SELECT * FROM DETAILS")
        table=cursor.fetchall()
        print("(Website,Username,Password)")
        print("")
        for row in table:
            print(row)
        print("")
    def display_creds(self,web): #method to display credentials of a specific website
        sel_stat="SELECT * FROM DETAILS WHERE WEBSITE=%s"
        val=(web,)
        cursor.execute(sel_stat,val)
        cred=cursor.fetchone()
        print("")
        print("Credentials for "+web+":\nUsername: ",cred[1],"\nPassword: ",cred[2])
        print("")
        return cred
    def delete_cred(self,web): #method to delete credentials of a specific website
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
    def suggest_cred(self,web): #method to suggest correct website if typos are present
        cursor.execute("SELECT WEBSITE FROM DETAILS")
        webs=cursor.fetchall()
        max_prob=-1
        closest=None
        for i in webs:
            score=fuzz.ratio((web,),i)
            if score>max_prob:
                max_prob=score
                closest=i
        return closest[0]
#creating a class for encryption and decryption
class Encrypt_Decrypt:
    def encrypt_cred(self,creds):
        fernet = Fernet(key)    #creating fernet object
        bcreds=creds.encode()   #converting into bytes
        crypted_creds=fernet.encrypt(bcreds)    #encrypting
        return crypted_creds
    def decrypt_cred(self, crypto):
        fernet = Fernet(key)    #creating fernet object
        decrypted_creds=fernet.decrypt(crypto)  #decrypting
        dcreds=decrypted_creds.decode() #converting to string
        return dcreds
#creating a class for qr code generation and reading
class Qr:
    def generate_qr(self,web,user,pwd):
        enc=Encrypt_Decrypt()
        creds="Website: "+web+"\nUsername: "+user+"\nPassword: "+pwd #credentials
        data=enc.encrypt_cred(creds) #encrypting
        img=qrcode.make(data) #generating qr code
        img.save("qrcode.png")
        print("QR code generated successfully!")
    def decode_qr(self,save_loc):
        img=cv2.imread(save_loc)    #reading the qr code
        det=cv2.QRCodeDetector()
        ans,x,y=det.detectAndDecode(img)   #getting the data from the qr code
        obj_ed=Encrypt_Decrypt()
        creds=obj_ed.decrypt_cred(ans) #decrypting
        return creds
#main program
access_user="Admin"
access_pwd="PMqr#2023"
inp_user=input("Enter your username: ")
inp_pwd=input("Enter your password: ")
if access_user==inp_user and access_pwd==inp_pwd:    
    print("-------------------------------------------------------------------")
    print("WELCOME TO PASSWORD MANAGER AND ENCRYPTED QR CODE GENERATOR PROGRAM")
    print("-------------------------------------------------------------------")
    print("\n")
    while True:
        print("Select any of the following options:")
        print("")
        print("1. View all your credentials.")
        print("2. View credentials of a specific website.")
        print("3. Add credentials to your Password Manager.")
        print("4. Remove credentials from your Password Manager.")
        print("5. Export your credentials in the form of an Encrypted QR code.")
        print("6. Decrypt the credentials from an Encrypted QR code.")
        print("7. Exit.")
        try:
            option=int(input("Enter your choice: "))
        except:
            print("Invalid input! Please try again.")
        match option:
            case 1:
                obj_pm=Pass_Man()
                obj_pm.display_all()
                print("-------------------------------------------------------------------")
            case 2:
                obj_pm=Pass_Man()
                web=input("Enter the website: ")
                try:
                    obj_pm.display_creds(web)
                except:
                    sug=str(obj_pm.suggest_cred(web))
                    try:
                        print("Guess you meant "+sug+" instead of "+web)
                        obj_pm.display_creds(sug)
                    except:
                        print("Not found! Please check your input again.")
                print("-------------------------------------------------------------------")
            case 3:
                obj_pm=Pass_Man()
                web=input("Enter the website name: ")
                user=input("Enter the username: ")
                pwd=input("Enter the password: ")
                obj_pm.insert_cred(web,user,pwd)
                print("-------------------------------------------------------------------")
            case 4:
                obj_pm=Pass_Man()
                web=input("Enter the website name: ")
                obj_pm.delete_cred(web)
                print("-------------------------------------------------------------------")
            case 5:
                obj_pm=Pass_Man()
                obj_qr=Qr()
                web=input("Enter the website name: ")
                try:
                    cred=obj_pm.display_creds(web)
                    obj_qr.generate_qr(str(cred[0]),str(cred[1]),str(cred[2]))
                except:
                    sug=str(obj_pm.suggest_cred(web))
                    try:
                        print("Guess you meant "+sug+" instead of "+web)
                        cred=obj_pm.display_creds(sug)
                        obj_qr.generate_qr(str(cred[0]),str(cred[1]),str(cred[2]))
                    except:
                        print("Not found! Please check your input again.")
                print("-------------------------------------------------------------------")
            case 6:
                loc=input("Enter the address of the QR code: ")
                obj_qr=Qr()
                cred=obj_qr.decode_qr(loc)
                print(cred)
                print("-------------------------------------------------------------------")
            case 7:
                break
            case _:
                print("Invalid input! Please try again.")
                print("-------------------------------------------------------------------")
else:
    print("Invalid credentials!! Access denied.")                                         