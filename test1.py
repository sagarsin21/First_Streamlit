import streamlit as st
import pandas as pd

st.title('Excel Data Entry')
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:")
email = st.text_input("Enter your email:")
st.dataframe(name,age,email)
