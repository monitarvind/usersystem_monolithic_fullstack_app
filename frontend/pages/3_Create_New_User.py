import streamlit as st
import requests
import json

st.title("Enter User Details:")

user_id = st.text_input("User ID (e.g., 001):")
name = st.text_input("Name:")
email = st.text_input("Email ID:")
married = st.checkbox("Married")
weight = st.number_input("Weight (kg):", min_value=01.00, max_value=100.00, value=50.0, step=1.0)
allergy = st.multiselect("Allergies:", ["Nuts", "Dairy", "Gluten", "Shellfish", "None"])
phone = st.text_input("Phone (10 digits, no country code):")
dob = st.date_input("Date of Birth:")
linkedin_url = st.text_input("LinkedIn Profile URL (optional):")
emergency_contact = st.text_input("Emergency Contact (optional):")

if st.button("Create User"):
    # Build payload matching User_system model
    payload = {
        "id": user_id,
        "name": name,
        "email": email,
        "married": married,
        "weight": weight,
        "allergy": allergy if allergy and "None" not in allergy else None,
        "phone": phone,
        "dob": str(dob),
        "linkedin_url": linkedin_url if linkedin_url else None,
        "emergency_contact": int(emergency_contact) if emergency_contact else None
    }
    
    response = requests.post("http://localhost:8000/create_user", json=payload)
    
    if response.status_code == 200:
        st.success("User created successfully...")
    else:
        st.error(f"Error: {response.json().get('detail', response.text)}")
