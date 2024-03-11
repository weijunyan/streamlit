import streamlit as st
import pandas as pd


# 初始化购物车
if 'product_cart' not in st.session_state:
    st.session_state.product_cart = pd.DataFrame([])

def main():
    st.title('Factory Product Configuration')

    df = pd.read_csv("pages/files/products.csv")
    gas_list = pd.read_csv("pages/files/gases.csv")
    platform_list = pd.read_csv("pages/files/platform.csv")
    options_df = pd.read_csv("pages/files/options.csv")
    function_df = pd.read_csv("pages/files/function.csv")

    Tag_no =st.text_area("Input the tag number(s)")

    measured_gas = st.selectbox('Choose your measured gas', gas_list, index=None)
    platform_list_gas = platform_list[platform_list["Gas"] == measured_gas][["Platform"]]
    platform = st.selectbox('Choose your platform', platform_list_gas, index=None)

    df_g = df[df["Gas"] == measured_gas]
    df_p = df_g[df_g["Platform"] == platform]
    options_p = options_df[options_df["Platform"] == platform]
    df_m = df_p[["Analyzer", "ListPrice"]]
    selected_monitor_row = st.radio("Choose your monitors", df_m, index=None,key="analyzer")
    none_row = pd.DataFrame({
        "Analyzer":[None],
    })

    if selected_monitor_row:
        selected_monitor = df_m[df_m["Analyzer"] == selected_monitor_row]
        monitor_description = selected_monitor.iloc[0, 0]
        function_list = function_df[function_df["Platform"] == platform]
        options = function_list["Function"].tolist()
        options_selected = pd.DataFrame([])
        for item in options:
            with st.expander(f"{item}"):
                option_item_df_pre = options_p[options_p["Function"] == item]
                option_item_df = pd.concat([none_row,option_item_df_pre[["Analyzer", ]]])
                selected_option_row = st.radio("Please Choose",option_item_df, index=None,key=item)
                if selected_option_row:
                    selected_option_item = option_item_df[option_item_df["Analyzer"] == selected_option_row]
                    options_selected = pd.concat([options_selected, selected_option_item])
                    monitor_description = monitor_description + "  \n" + selected_option_item.iloc[0, 0]
        output = pd.DataFrame({
            "Tag No.(s)": [Tag_no],
            "Analyzer": [monitor_description],
        })
        st.subheader("Your Selected Product")
        st.dataframe(output, use_container_width=True, hide_index=True)
        if st.button('Add to cart'):
            st.session_state.product_cart=pd.concat([st.session_state.product_cart,output]).reset_index(drop = True)
            st.success('Added to cart!')
            st.rerun()



if __name__ == "__main__":
    main()
