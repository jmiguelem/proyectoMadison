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
    st.title("Concentrado de calificaciones Madison")
    image = Image.open('Logo-Madison.png')
    st.image(image)
    st.text("Bienvenidos a la página de concecntrados de calificaciones del Colegio Madison")
    st.text("Favor de subir un archivo con calificaciones en la página \"Load file\" para que se vea la representación de las calificaciones")
    st.sidebar.write()

    

   
    # display_page()


main()
