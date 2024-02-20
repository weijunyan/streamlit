import streamlit as st

with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider",0, 130, [0,25])
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "\n checkbox", checkbox_val)

st.write("Outside the form")


if "value" not in st.session_state:
    st.session_state.value = "Title"

##### Option using st.rerun #####
st.header(st.session_state.value)

if st.button("Foo"):
    st.session_state.value = "Foo"
    st.rerun()


def update_value():
   st.session_state.value = "Bar"

st.button("Bar", on_click=update_value)

container = st.container()

if st.button("Baz"):
    st.session_state.value = "Baz"

container.header(st.session_state.value)


name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')

st.rerun()