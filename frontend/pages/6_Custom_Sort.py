import streamlit as st
import requests, pandas as pd

st.title("Custom Sort of User Data:")

input_field = st.radio("Select:", ["Date of Birth", "Phone Number"])

if input_field:
    input_order = st.radio("Select the Order :", ["Ascending", "Descending"])
    st.write(f"You want to see the {input_field} of all the users, in {input_order} order")

# Map display values to API parameters. Reference Map
field_map = {"Date of Birth": "dob", "Phone Number": "phone"}
order_map = {"Ascending": "asc", "Descending": "desc"}

if st.button("Sort"):
    sort_by = field_map[input_field]
    order = order_map[input_order]
    
    response = requests.get(f"http://localhost:8000/sorting?sort_by={sort_by}&order={order}")

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)  # API returns a list of user dicts
        st.dataframe(df)
    else:
        st.error(f"Error: {response.json().get('detail', response.text)}")
  