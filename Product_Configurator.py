import streamlit as st
import pandas as pd


# 初始化购物车
if 'product_cart' not in st.session_state:
    st.session_state.product_cart = pd.DataFrame([])
if 'spare_cart' not in st.session_state:
    st.session_state.spare_cart = pd.DataFrame([])


def main():
    st.title('Product Configuration')

    df = pd.read_csv("pages/files/products.csv")
    gas_list = pd.read_csv("pages/files/gases.csv")
    platform_list = pd.read_csv("pages/files/platform.csv")
    options_df = pd.read_csv("pages/files/options.csv")
    function_df = pd.read_csv("pages/files/function.csv")
    platform_sp = pd.read_csv("pages/files/platform_sp.csv")
    spare_part = pd.read_csv("pages/files/spare.csv")
    type = st.sidebar.radio("Type", ["Select Product", "Select Spare Part"],key="type")

    if type == "Select Product":
        with st.sidebar:
            measured_gas = st.selectbox('Choose your measured gas', gas_list, index=None)
            platform_list_gas = platform_list[platform_list["Gas"] == measured_gas][["Platform"]]
            platform = st.selectbox('Choose your platform', platform_list_gas, index=None)

        df_g = df[df["Gas"] == measured_gas]
        df_p = df_g[df_g["Platform"] == platform]
        options_p = options_df[options_df["Platform"] == platform]
        df_m = df_p[["Analyzer", "ListPrice"]]
        st.subheader(f"Main Product: {platform},{measured_gas}")
        selected_monitor_row = st.radio("Choose your monitors", df_m, index=None,key="analyzer")

        if selected_monitor_row:
            selected_monitor = df_m[df_m["Analyzer"] == selected_monitor_row]
            monitor_description = selected_monitor.iloc[0, 0]
            main_price = selected_monitor.iloc[0, 1]
            st.subheader("Options")
            function_list = function_df[function_df["Platform"] == platform]
            options = function_list["Function"].tolist()
            options_selected = pd.DataFrame([])
            for item in options:
                with st.expander(f"{item}"):
                    option_item_df_pre = options_p[options_p["Function"] == item]
                    option_item_df = option_item_df_pre[["Analyzer", "ListPrice"]]
                    selected_option_row = st.radio("Please Choose", option_item_df, index=None,key=item)
                    if selected_option_row:
                        selected_option_item = option_item_df[option_item_df["Analyzer"] == selected_option_row]
                        options_selected = pd.concat([options_selected, selected_option_item])
                        monitor_description = monitor_description + "  \n" + selected_option_item.iloc[0, 0]
            if options_selected.empty:
                options_price = 0
            else:
                options_price = options_selected["ListPrice"].sum(axis=0)
            total_monitor_price = main_price + options_price
            if 'row' not in st.session_state:
                st.session_state['row'] = 0
            output = pd.DataFrame({
                "Analyzer": [monitor_description],
                "ListPrice": [total_monitor_price],
                "Discount": [0],
                "Quantity": [1],
                "Unit Price": [total_monitor_price],
                "Total Price": [total_monitor_price],
            }, index=[st.session_state['row']])
            with st.sidebar:
                st.subheader("Your Selected Product")
                st.dataframe(output, column_order=("Analyzer","ListPrice"), hide_index=True)
                if not options_selected.empty:
                    with st.expander("Option"):
                        st.dataframe(options_selected, hide_index=True)
                if st.button('Add to cart'):
                    st.session_state.product_cart=pd.concat([st.session_state.product_cart,output])
                    st.session_state['row'] += 1
                    st.success('Added to cart!')
                    st.rerun()
    elif type == "Select Spare Part":
        platform_sparepart = st.selectbox('Choose your platform', platform_sp, index=None)
        spare_part_list = spare_part[spare_part["Platform"] == platform_sparepart][["Analyzer","Platform", "ListPrice","Discount","Quantity","Unit Price","Total Price"]]
        options_selected=st.multiselect('Choose your options',spare_part_list)
        options = spare_part_list[spare_part_list["Analyzer"].isin(options_selected)]
        options
        if st.button('Add to cart'):
            st.session_state.spare_cart = pd.concat([st.session_state.spare_cart,options]).reset_index(drop = True)
            st.success('Added to cart!')
            st.rerun()



if __name__ == "__main__":
    main()
