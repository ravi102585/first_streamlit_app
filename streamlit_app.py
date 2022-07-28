import streamlit
#streamlit.title('My MoM\'s New Healthy Diner')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.header(' Breakfast Favototes')
streamlit.text('🍳 omega 3 & Blueberry Oatmeal')
streamlit.text('🌽kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌 🍍Build Your Own Fruit Smoothie🥝🍇')


streamlit.multiselect('Pick some fruits : ', list(my_fruit_list.index), ['Avocado','Strawberries'])

streamlit.dataframe(my_fruit_list)
