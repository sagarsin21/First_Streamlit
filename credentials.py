import pyodbc 
server ='DESKTOP-J1I1PPA' 
database='mydb'
username='SA'
password='1234'

# Create connection string
connection_string=f'DRIVER=SQL Server;SERVER={'DESKTOP-J1I1PPA'};DATABASE={'mydb'};UID={'SA'};PWD={'1234'}'
# Connect to the database
conn=pyodbc.connect(connection_string)
