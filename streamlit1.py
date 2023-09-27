import streamlit as st
st.title('My parent new healthy diner')
st.header ('Breakfast Menu')
st.text('Blueberry Oat Meal')
st.text('🥑Avocado Toast🍞')
import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruit_selected=st.multiselect("Pick Some Fruits:",list(my_fruit_list.index))
fruits_to_show=my_fruit_list.loc[fruit_selected]
st.dataframe(fruits_to_show)
# New section to display FruityVice API response
st.header('FruityVice Fruit Advice!')
fruit_choice=st.text_input('What fruit would you like information about','Kiwi')
st.write('The user entered',fruit_choice)
import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_normalized=pd.json_normalize(fruityvice_response.json())
#Output as table
st.dataframe(fruityvice_normalized)
