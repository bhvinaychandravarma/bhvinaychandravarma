import streamlit as st

headerSection = st.container()
mainSection = st.container()
leftNav = st.sidebar

with headerSection:
    st.title("Streamlit")
    st.markdown("This is a demo of Streamlit")
