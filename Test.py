import streamlit as st
import pyodbc
@st.cache_resource
def init_connection():
  return pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};SERVER="
    + st.secrets["server"]
    +";DATABASE="
    +st.secrets["database"]
    +";UID="
    +st.secrets["username"]
    +";PWD="
    +st.secrets
  )
conn=init_connection()
@st.cache_data(ttl=600)
def run_query(query):
  with conn.cursor() as cur:
    cur.execute(query)
    return cur.fetchall()
rows=run_query("Select * from mytable;")
#print results
for row in rows:
  st.write(f"{row[0]} has a :{row[1]}:")
  


