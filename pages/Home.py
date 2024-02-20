import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(
    page_title="WJY App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


if st.button("Home"):
    st.switch_page("Home.py")
if st.button("Radio"):
    st.switch_page("pages/radio.py")
if st.button("Layout Container"):
    st.switch_page("pages/layout_container.py")

with st.echo():
    st.write('This code is wrong!')

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')



class Dog:
  '''A typical dog.'''

  def __init__(self, breed, color):
    self.breed = breed
    self.color = color

  def bark(self):
    return 'Woof!'


fido = Dog('poodle', 'white')

st.help(fido)

df1 = pd.DataFrame(np.random.randn(10, 10), columns=("col %d" % i for i in range(10)))

my_table = st.table(df1)

df2 = pd.DataFrame(np.random.randn(5, 10), columns=("col %d" % i for i in range(10)))

my_table.add_rows(df2)

if 'key' not in st.session_state:
    st.session_state['key'] = 'table'

st.session_state['key'] = 'value2'  # Dictionary like API

st.write(st.session_state.key)
st.session_state

st.text_input("Your name", key="name")
st.session_state.name

def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'



if 'name' not in st.session_state:
    st.session_state['name'] = 'John Doe'

st.header(st.session_state['name'])

if st.button('Jane'):
    st.session_state['name'] = 'Jane Doe'
    st.rerun()

if st.button('John'):
    st.session_state['name'] = 'John Doe'
    st.rerun()

st.header(st.session_state['name'])

