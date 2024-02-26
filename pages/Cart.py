import streamlit as st
import pandas as pd
if 'product_cart' not in st.session_state:
    st.session_state.product_cart = pd.DataFrame([])
if 'spare_cart' not in st.session_state:
    st.session_state.spare_cart = pd.DataFrame([])
st.title('Cart')

total_analyzer = 0
if not st.session_state.product_cart.empty:
    st.subheader("Analyzer")
    All_selected = st.session_state.product_cart
    def data_on_change(All_selected):
        state = st.session_state["selected_editor"]
        for index, updates in state["edited_rows"].items():
            for key, value in updates.items():
                st.session_state.product_cart.loc[st.session_state.product_cart.index == index, key] = value
                st.session_state.product_cart.loc[st.session_state.product_cart.index == index, "Unit Price"] = st.session_state.product_cart.loc[st.session_state.product_cart.index == index, "ListPrice"]*(1-st.session_state.product_cart.loc[st.session_state.product_cart.index == index, "Discount"]/100)
                st.session_state.product_cart.loc[st.session_state.product_cart.index == index, "Total Price"] = st.session_state.product_cart.loc[st.session_state.product_cart.index == index, "Unit Price"]*st.session_state.product_cart.loc[st.session_state.product_cart.index == index, "Quantity"]

    def neo_editor():
        st.data_editor(st.session_state.product_cart, key="selected_editor",column_config={
            "Analyzer": st.column_config.Column(
                width="small",
            ),
            "Discount": st.column_config.NumberColumn(
                "Discount(%)",
                help="input the discount",
                min_value=0,
                max_value=100,
                step=0.01,
                format="%d",
            ),
            "Quantity": st.column_config.NumberColumn(
                "Quantity",
                help="input the quantity",
                min_value=0,
                step=1,
                format="%d",
            ),
        }, num_rows="dynamic",on_change=data_on_change,args=[st.session_state.product_cart],hide_index=True, disabled=["Analyzer", "ListPrice","Unit Price","Total Price"])
    neo_editor()
    if not All_selected.empty:
        total_analyzer = st.session_state.product_cart.loc[:, "Total Price"].sum()
        st.write("Total Analyzers cost:",total_analyzer)


total_spare = 0
if not st.session_state.spare_cart.empty:
    st.subheader("Spare Parts")
    spare_selected = st.session_state.spare_cart.reset_index(drop = True)
    def spare_on_change(spare_selected):
        state_spare = st.session_state["spare_editor"]
        for index, updates in state_spare["edited_rows"].items():
            for key, value in updates.items():
                st.session_state.spare_cart.loc[st.session_state.spare_cart.index == index, key] = value
                st.session_state.spare_cart.loc[st.session_state.spare_cart.index == index, "Unit Price"] =st.session_state.spare_cart.loc[st.session_state.spare_cart.index == index, "ListPrice"]*(1 - st.session_state.spare_cart.loc[st.session_state.spare_cart.index == index, "Discount"] / 100)
                st.session_state.spare_cart.loc[st.session_state.spare_cart.index == index, "Total Price"] = st.session_state.spare_cart.loc[st.session_state.spare_cart.index == index, "Unit Price"] * st.session_state.spare_cart.loc[st.session_state.spare_cart.index == index, "Quantity"]

    def neo_spare_editor():
        st.data_editor(st.session_state.spare_cart, key="spare_editor", column_config={
            "Analyzer": st.column_config.Column(
                width="small",
            ),
            "Discount": st.column_config.NumberColumn(
                "Discount(%)",
                help="input the discount",
                min_value=0,
                max_value=100,
                step=0.01,
                format="%d",
            ),
            "Quantity": st.column_config.NumberColumn(
                "Quantity",
                help="input the quantity",
                min_value=0,
                step=1,
                format="%d",
            ),
        }, num_rows="dynamic", on_change=spare_on_change, args=[st.session_state.spare_cart],hide_index=True,disabled=["Analyzer", "ListPrice","Unit Price","Total Price"],)
    neo_spare_editor()
    if not spare_selected.empty:
        total_spare = st.session_state.spare_cart.loc[:, "Total Price"].sum()
        st.write("Total Spare Part cost:", total_spare)



total_cost = total_analyzer+total_spare
st.write("Total Cost is:",total_cost)

