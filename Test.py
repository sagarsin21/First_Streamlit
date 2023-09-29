import streamlit as st
st.title('ARCHITECTURE')
if st.button('Submit'):
  st.write('Submittedd Successfully')
name =st.text_input('Name')
st.write(name);

address=st.text_area('Enter your address')
st.write(address)
