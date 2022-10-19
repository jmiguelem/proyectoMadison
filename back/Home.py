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
    image = Image.open('Logo-Madison.png')
    st.image(image)
    st.sidebar.write()
    

   
    # display_page()


main()
