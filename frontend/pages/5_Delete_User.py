import streamlit as st
import requests

st.title("Delete User Details:")

user_id = st.text_input("Enter the User ID to delete:")

if user_id:
    if st.button("Delete"):
        response = requests.delete(f"http://localhost:8000/delete_user/{user_id}")

        if response.status_code == 200:
            st.success("User deleted successfully...")
        else:
            st.error(f"Error: {response.json().get('detail', response.text)}")