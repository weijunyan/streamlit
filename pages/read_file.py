import streamlit as st
import pandas as pd
from io import StringIO

df = pd.read_csv("pages/files/products.csv")
gas_list = pd.read_csv("pages/files/gases.csv")
platform_list = pd.read_csv("pages/files/platform.csv")
options_df = pd.read_csv("pages/files/options.csv")
function_df = pd.read_csv("pages/files/function.csv")
st.subheader("Main Product")

measured_gas = st.selectbox('Choose your measured gas',gas_list,index=None)
platform = st.selectbox('Choose your platform',platform_list,index=None)

df_g = df[df["Gas"]==measured_gas]
df_p=df_g[df_g["Platform"]==platform]
options_p= options_df[options_df["Platform"]==platform]
df_m = df_p[df_p.columns[2:7]]
# sdf_g = st.dataframe(df_m, hide_index=True, column_order=("P/N","Description","Information"))
# selected_monitor = st.selectbox("Choose your monitors",df_m)

selected_monitor_row = st.radio("Choose your monitors",df_m,index=None)
selected_monitor = st.empty()
main_monitor = st.empty()
with selected_monitor.container():
    if selected_monitor_row:
        selected_monitor = df_m[df_m["Analyzer"] == selected_monitor_row]
        main_monitor = selected_monitor.iloc[0,1]
        main_price = selected_monitor.iloc[0,4]
        st.subheader("Options")
        function_list =function_df[function_df["Platform"]==platform]
        options = function_list["Function"].tolist()
        options_selected = pd.DataFrame([])
        for item in options:
            is_choosed = st.checkbox(item)
            if is_choosed:
                option_item_df_pre = options_p[options_p["Function"]==item]
                option_item_df =option_item_df_pre[["Analyzer","ListPrice"]]
                selected_option_row = st.radio("Please Choose",option_item_df,index = None)
                if selected_option_row:
                    selected_option_item= option_item_df[option_item_df["Analyzer"] == selected_option_row]
                    options_selected = pd.concat([options_selected,selected_option_item])
        if options_selected.empty:
            options_price = 0
        else:
            options_price = options_selected["ListPrice"].sum(axis=0)
        total_monitor_price = main_price+options_price
        selected_monitor.iloc[0, 4] = total_monitor_price
        selected_monitor = st.dataframe(selected_monitor,column_order=("Analyzer","ListPrice"),hide_index=True)
        expander = st.expander("***Options***")
        with expander.container():
            options_selected =st.dataframe(options_selected,hide_index=True)





