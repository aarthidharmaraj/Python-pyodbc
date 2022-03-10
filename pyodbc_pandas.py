import pyodbc
import pandas as pd

from tkinter import YES

SERVER='localhost'
DATABASE='testpyodbc'
conn = pyodbc.connect(driver='{MySQL ODBC 8.0 Unicode Driver}', host=SERVER, database=DATABASE, user='root', password='Aspire@123',trusted_connection=YES,autocommit=True)
##connection cursor
cursor=conn.cursor()

query=pd.read_sql_query("SELECT * FROM testpyodbc.table2",conn)
df=pd.DataFrame(query)
print(df)
df.to_csv("sql_query_csv.csv",index=False)

##Excel documents
# query=pd.read_sql("SELECT * FROM testpyodbc.table2",conn)
# df1=pd.DataFrame(query)
df.to_excel("sql_query_excel.xlsx",sheet_name='Database pyodbc')