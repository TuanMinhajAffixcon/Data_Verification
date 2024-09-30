# # from template import *
# import pandas as pd
# # import snowflake.connector
# from main import country
# import streamlit as st

# st.header(":red[AFFIX Data Verification System]", divider=True)


# # st.success("Connected to Snowflake successfully!")
# country()


#------------------------------------------------------------------------------------------------

from template import *
import requests
from requests.auth import HTTPBasicAuth
import streamlit as st
import pandas as pd

import pickle
from pathlib import Path

import pandas as pd  # pip install pandas openpyxl
import streamlit_authenticator as stauth  # pip install streamlit-authenticator

st.header(":red[AFFIX Data Verification System]", divider=True)

# --- USER AUTHENTICATION ---
names = ["testuser"]
usernames = ["testuser"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    base_url = "https://verification-system-production.up.railway.app"

    endpoint = "/verify_user/"

    username = "testuser"  
    password = "affixcon1234"  

    col1, col2, col3 = st.columns((0.4, 0.40, 0.2))

    with col1:
        first_name = st.text_input('First Name', value='Jila')
        middle_name = st.text_input('Middle Name', value='Fakour')
        sur_name = st.text_input('Last Name', value='Tahmasebi')
        dob = st.text_input('DOB', value='1958-07-05')
        col11,col12,col13,col14=st.columns((4))
        with col11:
            address_line1 = st.text_input('Address Line 1', value="4 Melissa St")
        with col12:
            suburb = st.text_input('Suburb', value="DUNCRAIG")
        with col13:
            state = st.text_input('State', value="WA")
        with col14:
            postcode = st.text_input('Postcode', value="6023")
        mobile = st.text_input('Mobile', value='421074419')
        email = st.text_input('Email Address', value='jila_fakour@yahoo.co.uk')

        payload = {
        "first_name": first_name, 
        "middle_name": middle_name,
        "sur_name": sur_name, 
        "dob": dob, 
        "address_line1": address_line1, 
        "suburb": suburb, 
        "state": state, 
        "postcode": postcode, 
        "mobile": mobile, 
        "email": email

        }
        response = requests.post(
            base_url + endpoint,
            json=payload,  
            auth=HTTPBasicAuth(username, password)  
        )

        if st.button('Submit'):
            with col2:
            # Check if the request was successful
                if response.status_code == 200:
                    # Parse and print the JSON response data
                    data = response.json()
                    # df = pd.DataFrame(data)
                    # df.columns = ['Results']
                    st.dataframe(data, width=550, height=900)  

                    
                else:
                    # Print the error
                    st.write(f"Error: {response.status_code} - {response.text}")


