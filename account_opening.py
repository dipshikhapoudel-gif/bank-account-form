import streamlit as st
from datetime import date

current_date = date.today()

st.title("ABC Bank")
st.header("Account Opening Form: ")
st.write("Please fill out the form below to open an account with us.")

# User Input
full_name = st.text_input("Enter your full name: ", max_chars=50)
user_email = st.text_input("Enter your email address: ", max_chars=50)
address = st.text_area("Enter your address: ", max_chars=200)
phone_number = st.text_input("Enter your phone number: ", max_chars=10)
dob = st.date_input("Enter your date of birth: ", max_value=current_date)
yearly_income = st.number_input("Enter your yearly income: ", min_value=0, step=1000)
gender = st.radio("Select your gender: ", ("Male", "Female", "Other"), horizontal=True)
account_type = st.pills("Select account type: ", ("Savings", "Current", "Fixed Deposit"))
province = st.selectbox("Select your province: ", ("Province 1", "Province 2", "Province 3", "Province 4", "Province 5", "Province 6", "Province 7"))
prefrereed_branches = st.multiselect("Select your preferred branches: ", ("Branch A", "Branch B", "Branch C", "Branch D", "Branch E"))
terms_clicked = st.checkbox("I agree to the terms and conditions.")
register_button = st.button("Register")

if register_button:
    if not terms_clicked:
        st.error("You must agree to the terms and conditions to register.")
    else:
        st.success("Account registered successfully!")
 