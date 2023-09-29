import streamlit as st
st.title('ARCHITECTURE')
if st.button('Submit'):
  st.write('Submittedd Successfully')
name =st.text_input('Name')
st.write(name)

address=st.text_area('Enter your address')
st.write(address)
date=st.date_input('Enter a Date')
time=st.time_input('Enter a Time')
if st.checkbox("You accept T&C",value=True):
  st.write('Thank You')

