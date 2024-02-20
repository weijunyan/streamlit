import streamlit as st
from PIL import Image
import numpy as np

genre = st.radio(
    "What's your favorite movie genre",
    [[':rainbow[Comedy]','Laugh out loud.'], ["***Drama***","Get the popcorn."], ["Documentary :movie_camera:","Get the popcorn."]],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])


st.write("You selected:", genre[0],":",genre[1])

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )

st.subheader('Multiselect')
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)


img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)


color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

st.image('sunrise.jpg', caption='Sunrise by the mountains')