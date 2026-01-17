import streamlit as st

login = st.button("Login")


st.link_button("Home", url='http://localhost:8000/homepage')


contact_method = st.sidebar.selectbox('How would you like to be contacted?',
('Email', 'Mobile phone', 'Office Phone'))

if contact_method == 'Email':
    email = st.text_input("Pls enter your email ID:")
    st.write(f"We will reach out to you on your registered email shortly: {email}")
elif contact_method == 'Mobile phone':
    mp = st.text_input("Pls enter your Mobile Phone:")
    st.write(f"We will reach out to you on your registered phone number shortly: {mp}")
else:
    op = st.text_input("Pls enter your Office Phone:")
    st.write(f"We will reach out to your office phone shortly: {op}")