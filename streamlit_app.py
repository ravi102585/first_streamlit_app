import streamlit
import snowflake.connector
import pandas
import requests
from urllib.error import URLError

streamlit.title('My MoM\'s New Healthy Diner')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.header(' Breakfast Favototes')
streamlit.text('🍳 omega 3 & Blueberry Oatmeal')
streamlit.text('🌽kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌 🍍Build Your Own Fruit Smoothie🥝🍇')


fruits_selected = streamlit.multiselect('Pick some fruits : ', list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")

def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    # streamlit.text(fruityvice_response.json())
    # write your own comment -what does the next line do?
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

try:
     fruit_choice = streamlit.text_input('What fruit would you like information about?')
     if not fruit_choice:
         streamlit.error("please select a fruit to get information")
     else:
         #import requests

         # write your own comment - what does this do?
         back_from_fundtion=get_fruitvice_data(fruit_choice)
         streamlit.dataframe(back_from_fundtion)
         #streamlit.write('The user entered ', fruit_choice)
except URLError as e:
    streamlit.error()





streamlit.header("View our fruit list - Add your favorities!")
#snowflake related fuction
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from pc_rivery_db.public.fruit_load_list;")
        return  my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_row =get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_row)

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('"+new_fruit+"');")
        return 'Thanks adding Fruit '+new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like load?')
if streamlit.button('Add Fruit to the list '):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_fundtion = insert_row_snowflake(add_my_fruit)
    my_cnx.close()
    streamlit.text(back_from_fundtion)