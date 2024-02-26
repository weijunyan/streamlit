import streamlit as st
import pandas as pd

st.subheader("气体折扣表")
st.info("以下折扣表需满足100%预付!")
discount_table = pd.DataFrame({
    "气体":["O2","NH3","CO","CO2","HCl","H2S","H2O","HF","CH4","粉尘","其他"],
    "折扣":[45,55,45,42,42,42,42,42,42,42,35],
})
discount_table

st.subheader("备件折扣表")
st.info("吹扫法兰折扣为50%，其他未标注'No Discount'的，均为35%的折扣！")
