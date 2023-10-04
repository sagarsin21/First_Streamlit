import streamlit as st
import pyodbc
import pandas as pd
st.title('SMFG Reprorting')
username=None
username=st.text_input('username',key='username')
df=pd.dataframe([username])
