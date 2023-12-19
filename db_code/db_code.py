import sqlite3
import pandas as pd

#creating and connecting the database
conn=sqlite3.connect('STAFF.db')

#creating the table and attributes details
table_name='INSTRUCTOR'
attribute_list= ['ID','FNAME','LNAME','CITY','CCODE']

#reading the CSV file
file_path='/home/project/INSTRUCTOR.csv'
df=pd.read_csv(file_path,names=attribute_list)

#loading the data to the table
df.to_sql(table_name,conn,if_exists='replace', index=False)
print('Table is ready!')

#viewing all the data in the table
query_statement=f"SELECT * FROM {table_name}"
query_output =pd.read_sql(query_statement,conn)
print(query_statement)
print(query_output)

#viewing only FNAME column of data
query_statement= f"SELECT FNAME FROM {table_name}"
query_output =pd.read_sql(query_statement,conn)
print(query_statement)
print(query_output)

#viewing the total number of entries in the table
query_statement=f"SELECT COUNT(*) FROM {table_name}"
query_output =pd.read_sql(query_statement,conn)
print(query_statement)
print(query_output)

#create dataframe of the new data
data_dict={'ID':[100],
'FNAME':['John'],
'CITY':['Paris'],
'CCODE':['FR']}
data_append=pd.DataFrame(data_dict)

#append data to the table
data_append.to_sql(table_name,conn,if_exists='append',index=False)
print('data appended succesfully')

#repeating the count query to observe the data increase
query_statement=f"SELECT COUNT(*) FROM {table_name}"
query_output =pd.read_sql(query_statement,conn)
print(query_statement)
print(query_output)

#close the connection to the database
conn.close()