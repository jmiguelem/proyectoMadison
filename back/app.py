from distutils.command.clean import clean
#from json import load
from unicodedata import name
import streamlit as st
import pandas as pd
from pandasql import sqldf
import plotly.express as px
from data_utils import load_data, transform_data,clean_data

from PIL import Image




# Pagina de Display


def display_page():
    # Lista de materias
    materias = ('Language Acquisition - English',
                'Individuos y Sociedades - Formación cívica y ética',
                'Individuos y Sociedades - Historia de México',
                'Language Acquisition -  French', 'Lengua y Literatura - Español',
                'Mathematics', 'Physical and health education',
                'Sciences - Chemistry', 'Technology Education', 'Arts - Music',
                'Individuals and Societies - World History',
                'Lengua y Literatura - Literatura', 'Design', 'Community Project',
                'Arts - Visual Arts', 'Individuos y Sociedades - Geografía',
                'Individuals and societies - World History', 'Sciences - Physics',
                'Visual Arts', 'Sciences - Biology',
                'Sciences - Integrated Science')

    # Display de un select box con la lista de materias
    materia = st.selectbox("Materias", materias, key='2')

    # Cargamos la data tratada
    df = load_data()
    if df is None:
        return
    df = clean_data(df)
    df = transform_data(df)
    # Selecionamos la materia que queremos
    df = df.loc[df['GP3'] == materia]

    # Histograma SEP
    SEP = px.histogram(df, x="SEP", color_discrete_sequence=[
        'blue', 'blue', 'green'])
    SEP.update_layout(title=materia,
                      xaxis_title_text='Calificacones SEP',
                      yaxis_title_text='Cantidad de alumnos')
    # Histograma IB
    IB = px.histogram(df, x="Grade", color_discrete_sequence=[
        'indianred'], nbins=31)
    IB.update_layout(title=materia,
                     xaxis_title_text='Calificacones IB',
                     yaxis_title_text='Cantidad de alumnos')

    # Display de Histogramas SEP-IB
    st.plotly_chart(SEP)
    st.plotly_chart(IB)


def main():
    image = Image.open('Logo-Madison.png')
    st.image(image)
    # Carga de datos
    display_page()



main()
