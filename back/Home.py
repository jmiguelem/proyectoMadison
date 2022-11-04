from distutils.command.clean import clean
#from json import load
from unicodedata import name
import streamlit as st
import pandas as pd
from pandasql import sqldf
import plotly.express as px

from pages.Load_file import treated_data
from PIL import Image


def main():

    col1, col2 = st.columns([3, 1])

    with col1:
        madison = Image.open('Logo-Madison.png')
        st.image(madison,width=250)
    with col2:
        ib = Image.open('ib-Logo.png')
        st.image(ib,width=100)

    #st.subheader('Madison campus Monterrey')
    st.title("Concentrado de calificaciones")
    st.caption("Bienvenido aqui podras encontrar el resumen del desempeño de nuestros estudiantes.")
    st.caption("Favor de subir un archivo con calificaciones en la página \"Load file\" para que se vea la representación de las calificaciones")
    col1, col2 = st.columns(2)

    with col1:
        st.header("Lorem Ipsum")
        st.caption("Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...")

    with col2:
        st.header("Lorem Ipsum")
        st.caption("Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...")
            
    st.sidebar.write()

    

   
    # display_page()


main()
