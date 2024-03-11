import streamlit as st
import pandas as pd
if 'product_cart' not in st.session_state:
    st.session_state.product_cart = pd.DataFrame([])

st.title('Cart')
st.dataframe(st.session_state.product_cart,use_container_width=True,hide_index=True)

