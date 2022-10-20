#from distutils.command.clean import clean
#from multiprocessing import AuthenticationError
#from json import load
#from unicodedata import name

#import pandas as pd
#from pandasql import sqldf
#import plotly.express as px
#from pages.Performance import display_page

#from pages.Load_file import treated_data
from PIL import Image

#Required for LOGIN
import streamlit as st
import pickle
from pathlib import Path
import streamlit_authenticator  as stauth
import yaml

def login():
    
    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)
        authenticator = stauth.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days'],
            config['preauthorized']
)

    name, authentication_status, username = authenticator.login('Login', 'main')

    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{name}*')
        #display()
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')

def main():
    image = Image.open('./back/Logo-Madison.png')
    st.image(image)
    #st.sidebar.write()
    
main()
login()