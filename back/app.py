import streamlit as st
import pandas as pd
from pandasql import sqldf
import plotly.express as px

from PIL import Image
image = Image.open('Logo-Madison.png')
st.image(image)
# Carga de datos


def load_data():
    # Leemos el CVS de califiacaiones
    return pd.read_csv('Calificaciones.csv')

# Limpieza de datos


def clean_data():
    df = load_data()
    # Selecionamos las columnas que queremos
    df = df[['CGIDs', 'GP3', 'Gd3', 'Unnamed: 65']]
    # Borramos las filas que contienen NAN
    df = df.dropna()
    # Le asignamos el nombre Grades a la columna Sin nombre
    df.rename(columns={'Unnamed: 65': 'Grades'}, inplace=True)
    return df

# Transformación de datos


def transform_data():
    df = clean_data()
    # Selecionamos la info que queremos, y agrupamos por alumno y materia para sacar calificación
    df = sqldf(
        'Select CGIDs,GP3, SUM(Grades) AS Grade FROM df GROUP BY  CGIDs,GP3')
    df['Grade'] = df['Grade'].astype(int)
    # Agregamos la conversión a SEP
    df['SEP'] = df.apply(my_func, axis=1)
    # Orednamos por Calificación (Ayuda en la parte de vizualiczón)
    df = df.sort_values('Grade', ascending=False)
    return df

# Conversión a SEP


def my_func(row):
    if (row['Grade'] < 6):
        val = '5'
    elif row['Grade'] < 10:
        val = '5'
    elif row['Grade'] < 15:
        val = '6'
    elif row['Grade'] < 19:
        val = '7'
    elif row['Grade'] < 24:
        val = '8'
    elif row['Grade'] < 28:
        val = '9'
    else:
        val = '10'
    return val

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
    materia = st.selectbox("Materias", materias)

    # Cargamos la data tratada
    df = transform_data()
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


display_page()
