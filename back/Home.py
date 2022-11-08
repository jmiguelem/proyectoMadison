from distutils.command.clean import clean
#from json import load
from unicodedata import name
import streamlit as st
import pandas as pd
from pandasql import sqldf
import plotly.express as px
from PIL import Image

#LOGIN
import pickle
from pathlib import Path
import streamlit_authenticator  as stauth  #pip install streamlit_authenticator
from streamlit_option_menu import option_menu #pip install streamlit_option_menu
import yaml

from Load_file import treated_data
from Performance import display_page

def login():
    #LOGO
    col1, col2 = st.columns([3, 1])

    with col1:
        madison = Image.open('Logo-Madison.png')
        st.image(madison,width=250)
    with col2:
        ib = Image.open('ib-Logo.png')
        st.image(ib,width=100)

    
    with open('../config.yaml') as file:
        config = yaml.load(file, Loader=yaml.SafeLoader)
        authenticator = stauth.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days'],
            config['preauthorized'])

    name, authentication_status, username = authenticator.login('Login', 'main')

    if authentication_status:
        selected = option_menu(
            menu_title = None,
            options = ["Home", "Load File", "Performance"],
            icons= ["house", "upload", "eye"],
            menu_icon = "cast",
            default_index = 0,
            orientation = "horizontal"
        )
        
        if selected == "Home":
            main()
        if selected == "Load File":
            treated_data()
        if selected == "Performance":
            display_page()
        authenticator.logout('Logout', 'main')
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')


def main():

    #st.subheader('Madison campus Monterrey')
    st.title("Concentrado de calificaciones")
    st.caption("Bienvenido aqui podras encontrar el resumen del desempeño de nuestros estudiantes.")
    st.caption("Favor de subir un archivo con calificaciones en la página \"Load file\" para que se vea la representación de las calificaciones")
    col1, col2 = st.columns(2)
    

    #with col1:
        #st.header("Lorem Ipsum")
        #st.caption("Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...")

    #with col2:
        #st.header("Lorem Ipsum")
        #st.caption("Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...")
            
    #st.sidebar.write()

    

   
    # display_page()


login()
