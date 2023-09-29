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
st.write(date,time)
with st.echo():
 st.write('Code will be executed and printed')
