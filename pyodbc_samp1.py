from os import access
from tkinter import YES
import boto3
import pyodbc
import csv
client=boto3.client('s3')
##for going through the drivers in pyodbc
for driver in pyodbc.drivers():
    print(driver)
SERVER='localhost'
DATABASE='testpyodbc'
##Specifying the ODBC driver, server name, database, etc. directly
##connecting the database
##defining the connection string
conn = pyodbc.connect(driver='{MySQL ODBC 8.0 Unicode Driver}', host=SERVER, database=DATABASE, user='root', password='Aspire@123',trusted_connection=YES,autocommit=True)
##connection cursor
cursor=conn.cursor()
cursor.execute('SELECT * FROM table1')
rows = cursor.fetchall()
for data in rows:
    print(data)
    
print(pyodbc.dataSources())
mydataSour=pyodbc.dataSources()
access_driver=mydataSour['MS Access Database']
print(access_driver)

# ##query to select
query1='SELECT FIRST_NAME FROM table1 WHERE AGE<25'
cursor.execute(query1)
fetch=cursor.fetchall()
for data in fetch:
    print(data)

##query statement based on the date
query1='SELECT FIRST_NAME FROM table2 WHERE DATE_OF_BIRTH="2000-02-10"'
cursor.execute(query1)
fetch=cursor.fetchall()
for data in fetch:
    print(data)
##passing a single parameter
query2='SELECT FIRST_NAME,EMAIL FROM table1 WHERE GENDER=?','F'
cursor.execute('SELECT FIRST_NAME,EMAIL FROM table1 WHERE GENDER=?','M')
fetch=cursor.fetchall()
for data in fetch:
    print(data)

##convert to a csv file
with open('pyodbcquerywrite.csv','w')as f:
    for file in fetch:
        csv.writer(f).writerow(file)
        
client.create_bucket(Bucket='pyodbcpython')
response = client.put_object(
    Body=open('pyodbcquerywrite.csv','r').read(),#object data with open and read module of the uploading file
    Bucket='pyodbcpython',
    Key='pyodbcquery_fetchdata.csv',#file name to be in s3
)
print(response)

# ## passing a multiple parameter
cursor.execute('SELECT FIRST_NAME,EMAIL,DATE_OF_BIRTH FROM table2 WHERE GENDER=? AND AGE< ?',('M',25))
fetch=cursor.fetchall()
for data in fetch:
    print(data)

##Insert a single record

query2="INSERT INTO table1(id,FIRST_NAME,LAST_NAME,EMAIL,AGE,GENDER) VALUES (?,?,?,?,?,?)",(15,'six','sixfat','six@gmail.com',27,'F')

cursor.execute("INSERT INTO table2(id,FIRST_NAME,LAST_NAME,EMAIL,DATE_OF_BIRTH,AGE,GENDER) VALUES (?,?,?,?,?,?,?)",(23,'eight','sixfat','six@gmail.com','1996-02-10',27,'F'))
query3='SELECT id,FIRST_NAME,LAST_NAME,EMAIL,DATE_OF_BIRTH,AGE,GENDER FROM table2 '
cursor.execute(query3)
res=cursor.fetchall()
print(res)
cursor.close()

#printing the row count
deleted = cursor.execute("delete from table2 where id > 10").rowcount
print(deleted)

