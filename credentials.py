import streamlit as st
connection_string = 'DRIVER={SQL Server};SERVER=DESKTOP-J1I1PPA;DATABASE=mydb;UID=SA;PWD=1234'
st.header('Hello')
import pyodbc
conn = pyodbc.connect(connection_string)
#import pandas as pd
#query = 'SELECT * FROM myTable'
#df = pd.read_sql(query, conn)
