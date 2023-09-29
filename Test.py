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
if st.checkbox("You accept T&C",value=False):
  st.write('Thank You')

st.radio('Colours',['r','g','b'],index=0)
st.selectbox('Colours',['r','g','b'],index=1)
st.number_input('Numbers',min_value=18,max_value=100,value=25)
img=st.file_uploader('Upload a file')
st.image(img)
