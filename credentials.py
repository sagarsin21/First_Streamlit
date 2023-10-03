import pyodbc 
server ='localhost' 
database='mydb'
username='SA'
password='1234'

# Create connection string
connection_string=f'DRIVER=SQL Server;SERVER={localhost};DATABASE={mydb};UID={SA};PWD={1234}'
# Connect to the database
conn=pyodbc.connect(connection_string)
