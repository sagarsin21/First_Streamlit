import pyodbc 
server ='SAGAR(SQL Server 14.0.1000.169 -sa)' 
database='mydb'
username='SA'
password='1234'

# Create connection string
connection_string=f'DRIVER=SQL Server;SERVER={SAGAR(SQL Server 14.0.1000.169 -sa)};DATABASE={mydb};UID={SA};PWD={1234}'
# Connect to the database
conn=pyodbc.connect(connection_string)
