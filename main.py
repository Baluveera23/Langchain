"""
import streamlit as st
import langchain_helper

st.title("Meaning & Similar Names")
Selected = st.sidebar.selectbox(
    "Select One",("Arjun","Dhruva","Krishna","Rohan","Ravi","Ram","Raju","Venkatesh","Yashwanth")
)

if Selected :
    response = langchain_helper.generate_restaurant_name_and_item(Selected)
    st.header(response['restaurant_name'].strip())
    st.write("Similar Names")
    menu_items = response['menu_items'].strip().split(',')
    for items in menu_items:
        st.write("-",items)

"""
import streamlit as st
import langchain_helper

st.set_page_config(page_title="Meaning & Similar Names", layout="centered")
st.title("Indian Name Meaning & Similar Names")

Selected = st.sidebar.selectbox(
    "Select a name", ("Arjun", "Dhruva", "Krishna", "Rohan", "Ravi", "Ram", "Raju", "Venkatesh", "Yashwanth")
)

if Selected:
    with st.spinner("Working on it...."):
        response = langchain_helper.generate_restaurant_name_and_item(Selected)

    st.subheader("Meaning of the Name:")
    st.success(response['restaurant_name'].strip())
    st.subheader("Similar Sounding Names:")
    menu_items = response['menu_items'].strip().split(',')
    for item in menu_items:
        st.write("-", item.strip())

