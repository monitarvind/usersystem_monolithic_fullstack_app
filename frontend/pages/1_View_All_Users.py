import streamlit as st
import requests
import pandas as pd

st.title("Displaying: All User Details...")

if st.button("Show All"):
    response = requests.get("http://localhost:8000/all_user_list")

    # data = response.json() #receiving data in json's data
    # df = pd.DataFrame([data]) #Coverting Data in Panda's DataFrame
    # st.table(df.T)

    data = response.json()
    df = pd.DataFrame.from_dict(data, orient='index')  # Each user as a row
    st.dataframe(df)


    