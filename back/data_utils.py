from typing import Optional
import pandas as pd
from pandasql import sqldf
import streamlit as st

def load_data() -> Optional[pd.DataFrame]:

    # Leemos el CVS de califiacaiones
    data_file = st.file_uploader("Upload CSV", type=["csv"])
    if data_file is not None:
        df2 = pd.read_csv(data_file)          
        return df2
    else:
        return None
    


# Limpieza de datos
def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    # Selecionamos las columnas que queremos
    df = df[['CGIDs', 'GP3', 'Gd3', 'Unnamed: 65']]
    # Borramos las filas que contienen NAN
    df = df.dropna()
    # Le asignamos el nombre Grades a la columna Sin nombre
    df.rename(columns={'Unnamed: 65': 'Grades'}, inplace=True)
    # transform_data(df)
    return df

# Conversión a SEP


def assign_grades(row):
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


# Transformación de datos
def transform_data(df: pd.DataFrame) -> pd.DataFrame:

    # Selecionamos la info que queremos, y agrupamos por alumno y materia para sacar calificación
    df = sqldf(
        'Select CGIDs,GP3, SUM(Grades) AS Grade FROM df GROUP BY  CGIDs,GP3')
    df['Grade'] = df['Grade'].astype(int)
    # Agregamos la conversión a SEP
    df['SEP'] = df.apply(assign_grades, axis=1)
    # Orednamos por Calificación (Ayuda en la parte de vizualiczón)
    df = df.sort_values('Grade', ascending=False)
    return df
