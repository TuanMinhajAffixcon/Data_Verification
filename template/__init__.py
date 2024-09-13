import streamlit as st
from dotenv import load_dotenv
import os 
import snowflake.connector

st.set_page_config(page_title='Data Verification', page_icon='',layout='wide')

load_dotenv()
conn = snowflake.connector.connect(
    user=os.getenv('user'),
    password=os.getenv('password'),
    account=os.getenv('account'),
    warehouse=os.getenv('warehouse'),
    database=os.getenv('database'),
    schema=os.getenv('schema'),
    role=os.getenv('role')
    )
