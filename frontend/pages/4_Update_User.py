import streamlit as st
import requests

st.title("Update User Details:")

user_id = st.text_input("Enter the User ID to update:")

field = st.selectbox("Select the field to update:", ["phone", "emergency_contact"])

new_value = st.text_input("Enter the new value:")

if st.button("Update User"):
    if user_id:
        response = requests.put(
            f"http://localhost:8000/update_user/{user_id}",
            params={"field": field, "new_value": str(new_value)}
        )
        
        if response.status_code == 200:
            st.success("User updated successfully!")
        else:
            st.error(f"Error: {response.json().get('detail', response.text)}")
    else:
        st.warning("Please fill in all fields")
