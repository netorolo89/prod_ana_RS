import streamlit as st
import pandas as pd
import plotly_express as px
import calendar
prod = pd.read_csv(
    r'C:\Users\rodri\OneDrive\Desktop\TripleTen\Sprint5\Proyecto\prod_ana_RS\notebooks\Prod_Asig_Worked.csv')
st.title('Production Tracker')
st.header('Comportamiento de la producción de Hidrocarburos (2016-2024)')
st.subheader('Pendiente por definir...TERMINA AL FINAL')
st.divider()
st.markdown("Escribir indicaciones de como interactuar")
asig = st.selectbox('Seleccionar asignación a analizar',
                    prod['Asignación_o_Contrato'].unique(), placeholder="Lista de Asignaciones")
st.write(f"Se ha seleccionado la asignación {asig}")
