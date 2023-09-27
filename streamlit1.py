import streamlit as st
st.title('My parent new healthy diner')
st.header ('Breakfast Menu')
st.text('Blueberry Oat Meal')
st.text('🥑Avocado Toast🍞')
import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

fruit_selected=st.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Avocado','Banana'])
fruits_to_show=my_fruit_list.loc[fruit_selected]
st.dataframe(my_fruit_list)
