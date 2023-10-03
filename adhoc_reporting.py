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
with st.container():
    col1, col2 = st.columns(2)  # Create two columns

    from_date = col1.date_input('From Date', key='from_date')
    to_date = col2.date_input('To Date', key='to_date')
    
    customer_id = col1.text_input('Customer ID (comma-separated)', key='customer_id')
    batch_id = col2.text_input('Batch ID (comma-separated)', key='batch_id')

    app_ref_no = col1.text_input('App Ref No (comma-separated)', key='app_ref_no')
    lead_id = col2.text_input('Lead ID (comma-separated)', key='lead_id')

    gl_codes = col1.text_input('GL Code (comma-separated)', key='gl_codes')
    lan = col2.text_input('LAN (comma-separated)', key='lan')

df = pd.DataFrame(from_date,to_date,customer_id,batch_id,app_ref_no,lead_id,gl_codes,lan)
# Report selection dropdown
reports = st.selectbox('Select a report', ['Report 1', 'Report 2', 'Report 3'])

# Submit button
if st.button('Submit'):
    df.to_excel("user_data.xlsx", index=True)
    st.success("Data submitted successfully!")
    #username = st.session_state.username  # Set username (you should set this value as needed)
    if not username:
        st.error('Username cannot be empty. Please enter your username.')
    else:
        # Process the form submission
        st.write(f"Hello, {username}! Your {reports} will be placed in the shared folder in a few hours. Kindly wait. Thank you!")
