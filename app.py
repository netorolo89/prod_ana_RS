import streamlit as st
import pandas as pd
import plotly_express as px
import calendar
prod = pd.read_csv(
    r'prod_ana_RS\notebooks\Prod_Asig_Worked.csv')
st.title('Seguimiento a la Producción')
st.header('Comportamiento de la producción de Hidrocarburos (2016-2024)')
st.subheader('En esta aplicación se puede visualizar el comportamiento de la producción de aceite, gas, y agua de las asignaciones pertenecientes a las cuencas del sureste.')
st.divider()
st.subheader('Indicaciones:')
st.markdown("1. Seleccionar la asignación a revisar, puede comenzar a escribir en la selección de asignación para facilitar la búsqueda.")
st.markdown(
    "2. Puede incluir la revisión a un pozo, seleccionando la casilla Revisar Pozo.")
st.markdown("3. Dar click en el botón Revisar.")
st.divider()
asig = st.selectbox('Seleccionar asignación',
                    prod['Asignación_o_Contrato'].unique())
st.write(f"Se ha seleccionado la asignación {asig}")
asig_df = prod[prod['Asignación_o_Contrato'] == asig]
col1, col2 = st.columns(2)
with col1:
    anal_p = st.checkbox('Revisar pozo')
    if anal_p:
        pozo = st.selectbox('Seleccionar pozo',
                            asig_df['Nombre_del_pozo'].unique())
with col2:
    anal = st.button('Revisar')
st.divider()
if anal:
    st.subheader('Producción de aceite acumulada')
    st.markdown("Producción acumulada por pozo (MMb)")
    acum = asig_df.groupby('Nombre_del_pozo')['Np (MMb)'].sum()
    pozos = asig_df['Nombre_del_pozo'].unique()
    Np_pozos = px.histogram(x=pozos, y=acum, labels={
        'x': 'Pozos', 'y': 'Np (MMb)'}, color_discrete_sequence=['darkOliveGreen'])
    st.plotly_chart(Np_pozos, use_container_width=True)
    st.markdown(
        "Cantidad de pozos (eje vertical) en cada rango de producción acumulada (MMb)")
    Np_count = px.histogram(
        x=acum, labels={'x': 'Np (MMb)'}, color_discrete_sequence=['darkOliveGreen'], nbins=10)
    st.plotly_chart(Np_count, use_container_width=True)
    st.divider()
    st.subheader('Producción de gas acumulada')
    st.markdown("Producción acumulada por pozo (MMMpc)")
    acumg = asig_df.groupby('Nombre_del_pozo')['Gp (MMMpc)'].sum()
    Gp_pozos = px.histogram(x=pozos, y=acumg, labels={
        'x': 'Pozos', 'y': 'Gp (MMMpc)'}, color_discrete_sequence=['firebrick'])
    st.plotly_chart(Gp_pozos, use_container_width=True)
    st.markdown(
        "Cantidad de pozos (eje vertical) en cada rango de producción acumulada (MMMpc)")
    Gp_count = px.histogram(
        x=acumg, labels={'x': 'Gp (MMMpc)'}, color_discrete_sequence=['firebrick'], nbins=10)
    st.plotly_chart(Gp_count, use_container_width=True)
    st.divider()
    st.markdown("Producción de agua por pozo (%)")
    asig_df['Fecha'] = pd.to_datetime(asig_df['Fecha'], format='%Y-%m-%d')
    Fw_p = px.scatter(asig_df, x='Fecha', y='Fw (%)', color='Nombre_del_pozo',
                      color_discrete_sequence=px.colors.sequential.Emrld, labels={'Nombre_del_pozo': 'Pozos'})
    st.plotly_chart(Fw_p, use_container_width=True)
    st.markdown(
        'Dando click en los nombres de los pozos (lado derecho) se pueden quitar o agregar al gráfico.')
    st.divider()
    if anal_p:
        st.subheader('Revisión de producción por pozo')
        st.write(f"Se ha seleccionado el pozo {pozo}")
        pozo_df = asig_df[asig_df['Nombre_del_pozo'] == pozo]
        st.markdown("Comportamiento de producción de hidrocarburos")
        compp = px.line(pozo_df, x='Fecha', y=[
                        'Petróleo_(Mbd)', 'Gas_asociado_(MMpcd)'], color_discrete_map={'Petróleo_(Mbd)': '#014135', 'Gas_asociado_(MMpcd)': '#BC8F8F'}, labels={'value': 'Promedio diario mensual', 'variable': 'Hidrocarburo'})
        st.plotly_chart(compp, use_container_width=True)
        st.markdown("Comportamiento de producción de agua")
        pozo_df['Fecha'] = pd.to_datetime(pozo_df['Fecha'], format='%Y-%m-%d')
        compa = px.scatter(pozo_df, x='Fecha', y='Fw (%)').update_traces(
            marker=dict(color='turquoise'))
        st.plotly_chart(compa, use_container_width=True)
