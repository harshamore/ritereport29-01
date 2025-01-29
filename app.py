import streamlit as st

# Title or header for the app
st.title("Chart of Account Input Form")

# Text input for "Chart of Account Name"
chart_of_account_name = st.text_input("Enter Chart of Account Name:")

# Selectbox for "Debit or Credit"
context = st.selectbox("Debit or Credit:", ["Debit", "Credit"])

# Display the user input
st.write("**Chart of Account Name:**", chart_of_account_name)
st.write("**Context:**", context)
