import streamlit as st
import plotly.express as px

from pages.Load_file import ss


# Pagina de Display
def display_page():
    # Lista de materias
    materias = {'Language Acquisition - English':'blue',
                'Individuos y Sociedades - Formación cívica y ética':'pink',
                'Individuos y Sociedades - Historia de México':'yellow',
                'Language Acquisition -  French':'purple', 'Lengua y Literatura - Español':'orange',
                'Mathematics':'red', 'Physical and health education':'black',
                'Sciences - Chemistry':'green', 'Technology Education':'black', 'Arts - Music':'black',
                'Individuals and Societies - World History':'yellow',
                'Lengua y Literatura - Literatura':'light blue', 'Design':'black', 'Community Project':'black',
                'Arts - Visual Arts':'black', 'Individuos y Sociedades - Geografía':'light green',
                'Individuals and societies - World History':'yellow', 'Sciences - Physics':'green',
                'Visual Arts':'black', 'Sciences - Biology':'green',
                'Sciences - Integrated Science':'green'}
    

   
    #st.session_state['Treated_grades'] 
    if 'Treated_grades' in st.session_state:
        # Display de un select box con la lista de materias
        materia = st.selectbox("Materias", materias.keys(), key='2')
        
        df = st.session_state['Treated_grades']
        # st.write(df)
        # Selecionamos la materia que queremos
        df = df.loc[df['GP3'] == materia]

        # Histograma SEP
        SEP = px.histogram(df, x="SEP", color_discrete_sequence=[
            materias[materia]])
        SEP.update_layout(title=materia,
                        xaxis_title_text='Calificacones SEP',
                        yaxis_title_text='Cantidad de alumnos')
        # Histograma IB
        IB = px.histogram(df, x="Grade", color_discrete_sequence=[
            materias[materia]], nbins=31)
        IB.update_layout(title=materia,
                        xaxis_title_text='Calificacones IB',
                        yaxis_title_text='Cantidad de alumnos')

        # Display de Histogramas SEP-IB
        st.plotly_chart(SEP)
        st.plotly_chart(IB)
    else:
        st.header("Por favor suba un archivo con calificaciones")

display_page()
# st.write(st.session_state['Treated_grades'])