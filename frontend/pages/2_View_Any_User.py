import streamlit as st
import requests, json, pandas as pd

st.title("Displaying the User Details of 1 User")

userid = st.text_input("Enter your User ID: ")

if st.button("Fetch"):
    
    response = requests.get(f"http://localhost:8000/user_details/{userid}")

#http://localhost:8000/user_details/001

    #st.json(response.json())
    #print(f"Response:{response}")
    data = response.json() #receiving data in json's data
    df = pd.DataFrame([data]) #Coverting Data in Panda's DataFrame
    st.table(df.T) #Displaying in Tabular format