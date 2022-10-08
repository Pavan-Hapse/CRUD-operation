import mysql.connector
mysqldb=mysql.connector.connect(host="localhost", user="root", password="pavan123", database="d")
mysqlcursor=mysqldb.cursor()

#To create the table

#mysqlcursor.execute("Create table studentrecord(rollno int(10), name varchar(30), marks int(10))")

#To insert the data into the table

try:
    mysqlcursor.execute("insert into studentrecord(rollno, name, marks) values(1, 'Pavan', 99), (3, 'Vishal', 33), (4, 'Neha', 101)")
    mysqldb.commit()
    print("The record inserted into the table")
except:
    mysqldb.rollback()

mysqldb.close()



#display record

"""try:
    mysqlcursor.execute("Select * from studentrecord")
    'or mysqlcursor.execute("Select * from studentrecord where rollno=1")'
    result=mysqlcursor.fetchall()
    for i in result:
        roll= i[0]
        name= i[1]
        marks= i[2]
        print(roll, name, marks)

except:
    print("Some issue in the code")
mysqlcursor.close()"""


#update the record

"""try:
    mysqlcursor.execute("update studentrecord set name='Virat' where rollno=2")
    mysqldb.commit()
    print("The record has been updated successfully")
except:
    mysqldb.rollback()"""



# To delete the record

"""try:
    mysqlcursor.execute("delete from studentrecord where rollno=1")
    mysqldb.commit()
    print("The record has been deleted successfully")
except:
    mysqldb.rollback()
"""