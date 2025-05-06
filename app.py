import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Redirecting...", layout="centered")

# Just an immediate redirect to login
switch_page("Login")
