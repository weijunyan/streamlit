import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

# Using cache
a0 = time()
st.subheader('Using st.cache')

@st.cache_data
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)


# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)


st.header('Output')

st.write("st.session_state object:", st.session_state)

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  main_instrument = st.radio(
    "What's your favorite movie genre",
    [['A','Laugh out loud.'], ['B',"Get the popcorn."], ["Documentary :movie_camera:","Get the popcorn."]],
    key="gas")
with col2:
  other =  st.radio(
    "What's your favorite movie genre",
    [[':rainbow[Comedy]','Laugh out loud.'], ["***Drama***","Get the popcorn."], ["Documentary :movie_camera:","Get the popcorn."]],
    key="cable")

st.write("You selected:", main_instrument[0],other[0])
st.write("You selected:", main_instrument,other)
