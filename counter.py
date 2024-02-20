import streamlit as st
import pandas as pd


# 初始化购物车
if 'shopping_cart' not in st.session_state:
    st.session_state.shopping_cart = []


def main():
    st.title('Product Configuration')
    page = st.sidebar.radio("Page", ["Select Product", "Shopping Cart"])

    if page == "Select Product":

        df = pd.read_csv("pages/files/products.csv")
        gas_list = pd.read_csv("pages/files/gases.csv")
        platform_list = pd.read_csv("pages/files/platform.csv")
        options_df = pd.read_csv("pages/files/options.csv")
        function_df = pd.read_csv("pages/files/function.csv")
        st.subheader("Main Product")

        measured_gas = st.selectbox('Choose your measured gas', gas_list, index=None)
        platform = st.selectbox('Choose your platform', platform_list, index=None)

        df_g = df[df["Gas"] == measured_gas]
        df_p = df_g[df_g["Platform"] == platform]
        options_p = options_df[options_df["Platform"] == platform]
        df_m = df_p[["Analyzer", "ListPrice"]]
        # sdf_g = st.dataframe(df_m, hide_index=True, column_order=("P/N","Description","Information"))
        # selected_monitor = st.selectbox("Choose your monitors",df_m)

        selected_monitor_row = st.radio("Choose your monitors", df_m, index=None)
        selected_monitor = st.empty()
        with selected_monitor.container():
            if selected_monitor_row:
                selected_monitor = df_m[df_m["Analyzer"] == selected_monitor_row]
                main_price = selected_monitor.iloc[0, 1]
                st.subheader("Options")
                function_list = function_df[function_df["Platform"] == platform]
                options = function_list["Function"].tolist()
                options_selected = pd.DataFrame([])
                for item in options:
                    is_choosed = st.checkbox(item)
                    if is_choosed:
                        option_item_df_pre = options_p[options_p["Function"] == item]
                        option_item_df = option_item_df_pre[["Analyzer", "ListPrice"]]
                        selected_option_row = st.radio("Please Choose", option_item_df, index=None)
                        if selected_option_row:
                            selected_option_item = option_item_df[option_item_df["Analyzer"] == selected_option_row]
                            options_selected = pd.concat([options_selected, selected_option_item])
                if options_selected.empty:
                    options_price = 0
                else:
                    options_price = options_selected["ListPrice"].sum(axis=0)
                total_monitor_price = main_price + options_price
                selected_monitor.iloc[0, 1] = total_monitor_price
                output = pd.concat([selected_monitor, options_selected])
                selected_monitor = st.dataframe(selected_monitor, hide_index=True)
                expander = st.expander("***Options***")
                with expander.container():
                    options_selected = st.dataframe(options_selected, hide_index=True)


        if st.button('Add to cart'):
            st.session_state.shopping_cart.append(output)
            st.success('Added to cart!')
            st.rerun()  # 刷新页面，更新商品信息

    elif page == "Shopping Cart":
        st.title('Shopping Cart')
        total_cost = 0
        for item in st.session_state.shopping_cart:
            item_monitor = item.head(1)
            item_option = []
            if len(item)>1:
                item_option=item.iloc[(1-len(item)): , :]
            item_monitor.insert(item_monitor.shape[1],'Discount',0)
            item_monitor.insert(item_monitor.shape[1], 'Quantity', 1)
            product = st.data_editor(item_monitor,column_config={
                "ListPrice": st.column_config.NumberColumn(
                    "Price (in USD)",
                    help="The ListPrice of the product in USD",
                    min_value=0,
                    step=1,
                    format="$%d",
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
                    min_value=1,
                    step=1,
                    format="%d",
                ),
            }, key=item, hide_index=True, column_order=("Analyzer","ListPrice","Discount","Quantity"))
            expander = st.expander("***Options***")
            with expander.container():
                 st.dataframe(item_option, hide_index=True)

            unit_price = product.iloc[0,1]*(1-product.iloc[0,2]/100)
            st.write("Price after discount",unit_price)
            total_price = unit_price*product.iloc[0,3]
            st.write("Price with quantity", total_price)
            total_cost= total_cost+total_price

        st.write(f"Total Cost: ${total_cost}")




if __name__ == "__main__":
    main()
