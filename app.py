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
                    prod['Asignación_o_Contrato'].unique())
st.write(f"Se ha seleccionado la asignación {asig}")
col1, col2 = st.columns(2)
with col1:
    anal_p = st.checkbox('Realizar análisis de producción por pozo')
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
    st.divider()
    st.subheader('Producción de gas acumulada')
    st.markdown("Producción acumulada por pozo (MMMpc)")
    acumg = asig_df.groupby('Nombre_del_pozo')['Gp (MMMpc)'].sum()
    Gp_pozos = px.histogram(x=pozos, y=acumg, labels={
        'x': 'Pozos', 'y': 'Gp (MMMpc)'})
    Gp_pozos
    st.markdown(
        "Cantidad de pozos que han alcanzado cierta producción acumulada (MMMpc)")
    Gp_count = px.histogram(x=acumg, labels={'x': 'Gp (MMMpc)'})
    Gp_count
    st.divider()
    if anal_p:
        st.subheader('Análisis de producción por pozo')
        pozo = st.selectbox('Seleccionar pozo a analizar', pozos)
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Se ha seleccionado el pozo {pozo}")
        with col2:
            pozoa = st.button('Analizar pozo')
        # if pozo:
        # st.markdown(f"Comportamiento de producción del pozo {pozo}")
        # compp = px.line(asig_df.query("Nombre_del_pozo==pozo"), x='Fecha', y=[
        #    'Petróleo_(Mbd)', 'Gas_asociado_(MMpcd)'])
        # compp
