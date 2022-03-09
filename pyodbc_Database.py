from time import strftime
import mysql.connector
from datetime import datetime,date
mydb=mysql.connector.connect(host="localhost",user="root",password="Aspire@123", database='testpyodbc')

my_cursor=mydb.cursor()
# for creating new database

# my_cursor.execute("CREATE DATABASE testpyodbc")

#for showing databases

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db[0])

#for creating a table

# my_cursor.execute("CREATE TABLE table2(id integer PRIMARY KEY NOT NULL AUTO_INCREMENT,FIRST_NAME VARCHAR(100),LAST_NAME VARCHAR(100),EMAIL VARCHAR(150),DATE_OF_BIRTH DATE,AGE INTEGER(10),GENDER ENUM('M','F','O')NOT NULL)")
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table[0])
# formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
#for inserting data into table

sqlInsert="INSERT INTO table2(FIRST_NAME,LAST_NAME,EMAIL,DATE_OF_BIRTH,AGE,GENDER) VALUES(%s,%s,%s,%s,%s,%s)"
record1=("Keerthi","Siva","Keerthi@gmail.com",'2000-02-10',22,"F")
my_cursor.execute(sqlInsert,record1)
record2=("Sasi","John","sasi@gmail.com",'2001-01-30',20,"M")
my_cursor.execute(sqlInsert,record2)
record3=('Joseph','Michael','Jso@gmail.com','1990-03-09',30, 'M')
my_cursor.execute(sqlInsert,record3)
mydb.commit()
