import streamlit as st
st.title('My parent new healthy diner')
st.header ('Breakfast Menu')
st.text('Blueberry Oat Meal')
st.text('🥑Avocado Toast🍞')
import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
