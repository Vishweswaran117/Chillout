#!C:\Python312\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

print("<html>")
print("<body>")

Form=cgi.FieldStorage()
fName=Form.getvalue('name')
fNumber=Form.getvalue('phone')
fEmail=Form.getvalue('Email')
fPlace=Form.getvalue('Place')
fComment=Form.getvalue('Comment')


print("<h1>Thank you for register!!!</h1>")
print(fName,fNumber,fEmail,fPlace,fComment)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="chillout"
)

mycursor = mydb.cursor()

sql = "INSERT INTO student(Name,Number,Email,Place,Comment)VALUES(%s,%s,%s,%s,%s)"
val=(fName,fNumber,fEmail,fPlace,fComment)

mycursor.execute(sql,val)
mydb.commit()

print("</body>")
print("</html>")
