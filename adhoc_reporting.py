import streamlit as st
import pyodbc
import pandas as pd

# Database connection setup
#conn = pyodbc.connect(
#    'DRIVER={ODBC Driver 17 for SQL Server};'
#    'SERVER=LocalHost;'
#    'DATABASE=LMS;'
#    'UID=service_account;'
#    'PWD=pwd;'
#)

#cursor = conn.cursor()

# Streamlit UI
st.title('SMFG Reporting App')
# Get the username from user input
username = None
username = st.text_input('Username', key='username')
# User input fields

    if not username:
        st.error('Username cannot be empty. Please enter your username.')
    else:
        # Process the form submission
        st.write(f"Hello, {username}! Your {reports} will be placed in the shared folder in a few hours. Kindly wait. Thank you!")
