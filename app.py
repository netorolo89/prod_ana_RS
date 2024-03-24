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
col1, col2 = st.columns(2)
with col1:
    agua = st.checkbox('Incluir comportamiento de agua producida')
with col2:
    anal = st.button('Analizar')
st.divider()
if anal:
    st.subheader('Producción de petróleo acumulada')
    st.markdown("Producción acumulada por pozo (MMb)")
    asig_df = prod[prod['Asignación_o_Contrato'] == asig]
    acum = asig_df.groupby('Nombre_del_pozo')['Np (MMb)'].sum()
    pozos = asig_df['Nombre_del_pozo'].unique()
    Np_pozos = px.histogram(x=pozos, y=acum, labels={
        'x': 'Pozos', 'y': 'Np (MMb)'})
    Np_pozos
    st.markdown(
        "Cantidad de pozos que han alcanzado cierta producción acumulada (MMb)")
    Np_count = px.histogram(x=acum, labels={'x': 'Np (MMb)'})
    Np_count
