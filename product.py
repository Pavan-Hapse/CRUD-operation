from sqlite3 import Cursor
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="pavan123", database="d")
"""mycursor=mydb.cursor()
sql="Insert into Crud(id, product, cost) values (%s, %s, %s)"
val=(1,"Nirma", 50)
mycursor.execute(sql,val)
mydb.commit()"""

def getData(mydb):
    print("Read")
    cursor=connector.connect()  

getData()