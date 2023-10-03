import streamlit as st
import pyodbc
import pandas as pd
st.title('SMFG Reporting App')
username = None
username = st.text_input('Username', key='username')
    if not username:
        st.error('Username cannot be empty. Please enter your username.')
    
