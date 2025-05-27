import streamlit as st
import pandas as pd
import plotly_express as px
import calendar
asignaciones=['AR-0506-M - CAMPO ROSAL', 'AR-0496 - CAMPO RUSCO','A-0296-2M - CAMPO SAMARIA', 'AR-0475 - CAMPO RIO BRAVO','AR-0455 - CAMPO RICOS', 'AR-0453 - CAMPO RIACHUELO','A-0288-M - CAMPO REYNOSA', 
              'AR-0510-M - CAMPO RENO', 'AE-0392-M - PANUCO', 'AR-0451-2M - CAMPO REMOLINO','AE-0385-5M - SOLEDAD', 'A-0286-2M - CAMPO RANCHO NUEVO','A-0284-3M - CAMPO RABASA', 'A-0113-2M - CAMPO CULEBRA',
              'AE-0395-2M - MAGALLANES-TUCAN-PAJONAL', 'A-0308-3M - CAMPO SIHIL','A-0291-M - CAMPO RIO NUEVO', 'A-0320-2M - CAMPO SUR DE AMATLAN','A-0292-2M - CAMPO RODADOR', 'AE-0391-M - EBANO',
              'A-0299-2M - CAMPO SAN PABLO', 'A-0300-M - CAMPO SAN RAMON','A-0309-2M - CAMPO SINAN', 'A-0312-2M - CAMPO SITIO GRANDE','A-0310-2M - CAMPO SINI', 'AR-0457 - CAMPO SAN BERNARDO','AR-0520-M - CAMPO SOCAVON', 
              'A-0136-2M - CAMPO FUNDADOR','A-0280-4M - CAMPO POZA RICA','AR-0449-2M - CAMPO PRESIDENTE ALEMAN','AR-0450-M - CAMPO PRESIDENTE ALEMAN PR','AR-0481 - CAMPO PRIMAVERA', 'A-0282-2M - CAMPO PUERTO CEIBA',
              'AE-0398-M - MISION', 'AR-0420-3M - CAMPO FURBERO','A-0301-2M - CAMPO SANTA AGUEDA','A-0132-M - CAMPO EZEQUIEL ORDOÑEZ','AR-0507-2M - CAMPO EXPLORADOR','A-0061 - CAMPO CAPARROSO-PIJIJE-ESCUINTLE',
              'A-0112-3M - CAMPO CUITLAHUAC', 'A-0399-M - MONCLOVA','A-0128-M - CAMPO ESCOBAL', 'A-0135-2M - CAMPO FRONTERIZO','A-0383-M - CUERVITO', 'A-0285-2M - CAMPO RABEL','A-0298-2M - CAMPO SAN DIEGO CHICONCILLO',
              'A-0302-2M - CAMPO SANTA ANITA', 'A-0126-2M - CAMPO ENLACE','A-0305-2M - CAMPO SEN', 'A-0393-M - SAN ANDRES','AR-0418 - CAMPO DUNA', 'A-0116-2M - CAMPO DRAGON','A-0114-2M - CAMPO CUNDUACAN', 
              'A-0287-M - CAMPO RASHA','A-0290-M - CAMPO RINCON PACHECO', 'AR-0488 - CAMPO ECATL','A-0303-2M - CAMPO SANTA ROSALIA', 'AR-0416-2M - CAMPO COYOL','A-0396 - SANTUARIO', 'A-0094-5M - CAMPO COAPECHACA',
              'A-0124-M - CAMPO EMU', 'A-0122-2M - CAMPO ELTREINTA','A-0121 - CAMPO EL GOLPE', 'A-0120-M - CAMPO EK','A-0194-2M - CAMPO LOMITAS', 'AR-0437 - CAMPO MOLOACAN','A-0234-M - CAMPO NEJO', 
              'A-0109-2M - CAMPO CUATRO MILPAS','A-0244-M - CAMPO OGARRIO', 'A-0236-3M - CAMPO NISPERO','A-0216-2M - CAMPO MIAHUAPAN', 'A-0240-M - CAMPO OASIS','A-0243-M - CAMPO OCOTEPEC', 'A-0103-M - CAMPO CORRALILLO',
              'A-0107-4M - CAMPO COYULA', 'AR-0106-2M - CAMPO COYOTES','A-0211-2M - CAMPO MECAYUCAN', 'A-0004-4M - CAMPO AGUA FRIA','A-0401-M - PIRINEO', 'A-0215-M - CAMPO MESA CERRADA','AE-0388-2M - MIQUETLA', 
              'AR-0435 - CAMPO MIGUEL HIDALGO','AE-0387-5M - HUMAPA', 'A-0247-M - CAMPO OROZCO','A-0250-2M - CAMPO PACHE', 'A-0111-2M - CAMPO CUERVITO','A-0323-2M - CAMPO TAMAULIPAS CONSTITUCIONES','A-0245-3M - CAMPO ONEL',
              'A-0101-M - CAMPO COPITE','AR-0415 - CAMPO CORINDON', 'A-0100-M - CAMPO COPAL','A-0321-M - CAMPO TAJIN', 'A-0104 - CAMPO COSTERO','A-0225-2M - CAMPO MONTERREY', 'A-0226-M - CAMPO MORA',
              'A-0227-2M - CAMPO MORALILLO', 'AR-0439-M - CAMPO MUREX','A-0223-2M - CAMPO MOJARREÑAS', 'A-0228-2M - CAMPO MOZUTLA','A-0229-M - CAMPO MURO','A-0319-2M - CAMPO SUR CHINAMPA NORTE DE AMATLAN',
              'A-0232 - CAMPO NARVAEZ', 'A-0230-M - CAMPO MUSPAC','AE-0235-2M - CAMPO NELASH', 'A-0241-M - CAMPO OBERTURA','A-0242-2M - CAMPO OCH', 'A-0218-M - CAMPO MIRALEJOS','AR-0417 - CAMPO CUICHAPA-PONIENTE', 
              'A-0269-2M - CAMPO PERDIZ','AR-0482 - CAMPO PICADILLO', 'AR-0478 - CAMPO PIPILA','A-0254-2M - CAMPO PALMITO', 'AR-0443 - CAMPO PEÑA BLANCA','AR-0486 - CAMPO PATRIOTA', 'AR-0509-M - CAMPO OVEJA',
              'A-0197 - CAMPO LUNA-PALAPA', 'AR-0513-2M - CAMPO PALEOARCOS','A-0255-M - CAMPO PALO BLANCO', 'A-0267 - CAMPO PATLACHE','A-0275-2M - CAMPO PLATANAL', 'A-0278-2M - CAMPO POL','AE-0394-2M - TIERRA BLANCA', 
              'A-0259 - CAMPO PANDURA','A-0261-M - CAMPO PAPAN', 'A-0262-M - CAMPO PAPANTLA','A-0263-3M - CAMPO PAREDON', 'AR-0005-3M - CAMPO AGUA NACIDA','A-0264-3M - CAMPO PARETO', 'A-0044-2M - CAMPO BAYO',
              'A-0046-2M - CAMPO BELLOTA', 'AE-0389-M - ALTAMIRA','A-0047-M - CAMPO BLASILLO', 'A-0345-2M - CAMPO TOPO','A-0249-2M - CAMPO OXIACAQUE', 'A-0252-M - CAMPO PALANGRE','A-0265-2M - CAMPO PASCUALITO', 
              'AR-0266-M - CAMPO PASTORIA','AE-0386-5M - MIAHUAPAN', 'AR-0499 - CAMPO ORGANDI','AR-0485 - CAMPO PAME', 'A-0137-2M - CAMPO GALIA','AR-0502-M - CAMPO PITAL Y MOZUTLA', 'A-0366-2M - CAMPO VIBORITAS',
              'AR-0467 - CAMPO VERNET', 'A-0365-2M - CAMPO VELERO','AR-0504-M - CAMPO BONANZA', 'AR-0516-M - CAMPO VIGILANTE','A-0367-M - CAMPO VISTOSO', 'A-0370-M - CAMPO XOCOTLA','A-0371-3M - CAMPO XUX', 
              'AE-0382-5M - AMATITLAN','A-0359 - CAMPO USUMACINTA', 'A-0358-2M - CAMPO UECH','A-0356-2M - CAMPO TUPILCO', 'A-0349-M - CAMPO TRES HERMANOS','A-0352-3M - CAMPO TSIMIN', 'A-0373-3M - CAMPO YAXCHE',
              'AR-0438 - CAMPO MUNDO NUEVO', 'A-0375-3M - CAMPO ZAAP','A-0372-2M - CAMPO YAGUAL', 'A-0376-M - CAMPO ZACAMIXTLE','AR-0423 - CAMPO GUTIERREZ ZAMORA', 'A-0369-3M - CAMPO XANAB','A-0322-2M - CAMPO TAKIN', 
              'A-0324-2M - CAMPO TARATUNICH','A-0168-3M - CAMPO JUJO-TECOMINOACAN', 'A-0332-3M - CAMPO TERRA','A-0315-M - CAMPO SOLIS TIERRA AMARILLA','A-0316-2M - CAMPO SULTAN', 'A-0317-2M - CAMPO SUNUAPA',
              'A-0335-2M - CAMPO TIGRILLO', 'A-0338-4M - CAMPO TINTAL','AR-0469 - CAMPO VICHE', 'A-0374-2M - CAMPO YUM','A-0346-2M - CAMPO TORRECILLAS', 'AE-0339-2M - CAMPO TIUMUT','A-0340-2M - CAMPO TIZON', 
              'A-0023-2M - CAMPO ARCOS','A-0306-M - CAMPO SHISHITO', 'AR-0426-3M - CAMPO HUMAPA','A-0159-2M - CAMPO IRIDE', 'A-0160-3M - CAMPO IXTAL','A-0139-M - CAMPO GARUFA', 'A-0140-2M - CAMPO GASIFERO',
              'A-0141-3M - CAMPO GAUCHO', 'A-0154 - CAMPO HORMIGUERO','AR-0511-M - CAMPO HUATEMPO', 'A-0155-M - CAMPO HUIZACHE','A-0152-M - CAMPO HORCON', 'A-0151-3M - CAMPO HOMOL','A-0143-2M - CAMPO GENERAL', 
              'AR-0514-M - CAMPO GIGANTE','AR-0490 - CAMPO GRANADITAS', 'A-0400 - OLMOS','AR-0424 - CAMPO HALLAZGO', 'A-0193-2M - CAMPO LIZAMBA','A-0329-3M - CAMPO TEOTLECO', 'A-0331-M - CAMPO TEPETITAN',
              'A-0333 - CAMPO TERREGAL', 'A-0347-2M - CAMPO TOTECO CERRO AZUL','A-0342-2M - CAMPO TOKAL', 'A-0210-3M - CAMPO MAY','AR-0434 - CAMPO MAREOGRAFO', 'A-0208-2M - CAMPO MATA PIONCHE',
              'A-0195-3M - CAMPO LOS SOLDADOS', 'A-0198-M - CAMPO MACUILE','A-0201-3M - CAMPO MADREFIL', 'A-0203-3M - CAMPO MALOOB','A-0205-3M - CAMPO MANIK', 'AR-0463 - CAMPO TECOLUTLA','A-0169-2M - CAMPO JUSPI', 
              'A-0170-2M - CAMPO KAB','A-0171-M - CAMPO KABUKI', 'A-0172-2M - CAMPO KAMBESAH','A-0164-2M - CAMPO JAUJAL', 'A-0165-2M - CAMPO JILIAPA','AR-0472-M - CAMPO JARAGUAY', 'A-0166-M - CAMPO JOSE COLOMO',
              'A-0162-2M - CAMPO JACINTO', 'A-0161-4M - CAMPO IXTOC','A-0179-M - CAMPO KIBO', 'A-0182-2M - CAMPO KRIPTON','A-0183-4M - CAMPO KU', 'AE-0187-2M - CAMPO LACAMANGO','A-0189-M - CAMPO LANKAHUASA', 
              'AR-0515-M - CAMPO VALIOSO','A-0336-M - CAMPO TIHUATLAN', 'AR-0465 - CAMPO TOPEN','AE-0390-M - ARENQUE', 'A-0025-M - CAMPO ARIS','A-0027-2M - CAMPO ARROYO PRIETO', 'AE-0381-5M - PITEPEC',
              'AR-0406 - CAMPO BARCODON', 'A-0041-M - CAMPO BARUNDA','A-0060-2M - CAMPO CAÑON', 'A-0045-2M - CAMPO BEDEL','AR-0407 - CAMPO BENAVIDES', 'AE-0036-2M - CAMPO BACAL','A-0037-M - CAMPO BAGRE', 
              'A-0039-M - CAMPO BALAM','A-0108-M - CAMPO CRATER', 'A-0035-3M - CAMPO BACAB','A-0029-M - CAMPO ARTESA', 'A-0034-2M - CAMPO AYOCOTE','AR-0508-M - CAMPO AZOR', 'A-0022-2M - CAMPO ARCABUZ',
              'A-0083-M - CAMPO CHIAPAS-COPANO', 'A-0098-3M - CAMPO COMITAS','A-0099-2M - CAMPO COMOAPA', 'A-0097-M - CAMPO COCUITE','A-0081-2M - CAMPO CHAPUL', 'A-0084-M - CAMPO CHICHIMANTLA','A-0086-M - CAMPO CHILAPILLA', 
              'AR-0473-M - CAMPO CHINA','A-0330-2M - CAMPO TEPETATE NORTE CHINAMPA','A-0087-2M - CAMPO CHINCHORRO', 'A-0089-3M - CAMPO CHUC','A-0092-2M - CAMPO CINCO PRESIDENTES', 'A-0003-2M - CAMPO AGAVE',
              'A-0001-5M - CAMPO ABKATUN', 'A-0002-2M - CAMPO ACUATEMPA','A-0008-3M - CAMPO AKAL', 'A-0237-2M - CAMPO NOHOCH','AR-0409 - CAMPO CALIBRADOR', 'A-0053-2M - CAMPO CAAN','A-0054-2M - CAMPO CABEZA', 
              'A-0057-3M - CAMPO CACTUS','AR-0479-M - CAMPO CALABAZA', 'A-0051-2M - CAMPO BRILLANTE','A-0049-2M - CAMPO BOLONTIKU', 'A-0050-2M - CAMPO BRICOL','A-0075-2M - CAMPO CERRO NANCHITAL', 'AR-0483 - CAMPO CHALUPA',
              'A-0079-2M - CAMPO CHANCARRO', 'A-0071-2M - CAMPO CAUCHY','A-0072-2M - CAMPO CAUDALOSO', 'AR-0412 - CAMPO CARRETAS','A-0067-M - CAMPO CASTARRICAL', 'AR-0505-M - CAMPO CARAVANA','A-0063-M - CAMPO CARDENAS', 
              'AR-0480 - CAMPO CARLOS','A-0065-M - CAMPO CARPA', 'A-0110-2M - CAMPO CUCAÑA','AR-0521-M - CAMPO AXON', 'AR-0404-3M - CAMPO AYAPA','A-0032-2M - CAMPO AYATSIL', 'AR-0470-2M - CAMPO ARROYO ZANAPA',
              'A-0042-2M - CAMPO BATAB', 'A-0019-2M - CAMPO ARABE','A-0117-2M - CAMPO DULCE', 'A-0026-M - CAMPO ARQUIMIA','A-0040-M - CAMPO BARAJAS', 'AR-0512-M - CAMPO AZUCAR','A-0078-2M - CAMPO CHAC', 
              'A-0018-M - CAMPO APERTURA','AR-0517-M - CAMPO ANTIGUO', 'AR-0477-M - CAMPO ALONDRA','A-0006-2M - CAMPO AGUACATE', 'A-0016-2M - CAMPO ANGOSTURA','A-0010-M - CAMPO ALAMO SAN ISIDRO', 'AR-0468 - CAMPO ACAHUAL',
              'A-0090-2M - CAMPO CHUHUK', 'A-0095 - CAMPO COBO','A-0074-2M - CAMPO CERRO DEL CARBON', 'AR-0413 - CAMPO CATEDRAL','AR-0408 - CAMPO CAFETO', 'A-0144-2M - CAMPO GIRALDAS','A-0145-2M - CAMPO GUARICHO', 
              'A-0184-2M - CAMPO KUIL','A-0186-2M - CAMPO KUTZ', 'AR-0484-M - CAMPO LOBO','AR-0518-M - CAMPO GRANDE', 'AR-0501 - CAMPO BRAGADO','A-0174-2M - CAMPO KANAAB', 'A-0176-2M - CAMPO KAX',
              'A-0119-2M - CAMPO EDEN-JOLOTE', 'A-0199-M - CAMPO MADERA','AR-0474 - CAMPO JABALINA', 'A-0196-2M - CAMPO LUM','AR-0492 - CAMPO CASTA', 'A-0085-M - CAMPO CHICONCOA','A-0088-M - CAMPO CHIPILIN', 
              'AR-0471-2M - CAMPO LA CENTRAL','AR-0433 - CAMPO MALVA', 'A-0206-M - CAMPO MARSOPA','AR-0493 - CAMPO ITA', 'A-0007-2M - CAMPO AHUATEPEC','A-0129-M - CAMPO ESPEJO', 'AR-0519-M - CAMPO FILADELFIA',
              'AR-0491 - CAMPO FOSIL', 'AR-0494 - CAMPO FITON','A-0055-2M - CAMPO CACAHUATENGO', 'AR-0421 - CAMPO GRAN MORELOS','A-0115-2M - CAMPO CUPACHE', 'A-0138-2M - CAMPO GALLO','A-0200-M - CAMPO MADERACEO', 
              'A-0130-2M - CAMPO ETKAL','AR-0410 - CAMPO CALICANTO', 'A-0021-M - CAMPO ARAL','CNH-R01-L03-A18/2015', 'A-0217-2M - CAMPO MIQUETLA','A-0239-M - CAMPO NUEVO PROGRESO', 'AR-0452 - CAMPO REMOLINO PR',
              'CNH-R01-L03-A2/2015', 'CNH-R01-L03-A7/2015','CNH-R01-L03-A14/2015', 'CNH-R01-L03-A12/2015','AR-0476-M - CAMPO ATAJO', 'CNH-R01-L03-A11/2015','CNH-R01-L03-A8/2015', 'CNH-R01-L03-A15/2015',
              'CNH-R01-L03-A25/2015', 'A-0156-4M - CAMPO HUIZOTATE','CNH-R01-L03-A5/2015', 'CNH-R01-L03-A3/2015','CNH-R01-L03-A6/2015', 'CNH-R01-L03-A1/2015','A-0233-M - CAMPO NAVEGANTE', 'AR-0503-2M - CAMPO PITAHAYA',
              'A-0354-2M - CAMPO TUMUT', 'AR-0432 - CAMPO LA LAJA','A-0082-M - CAMPO CHE', 'CNH-R01-L03-A21/2016','CNH-R01-L03-A20/2016', 'CNH-M1-EK-BALAM/2017','A-0270-M - CAMPO PESERO', 'A-0043-M - CAMPO BATO',
              'CNH-R01-L03-A23/2015', 'CNH-R02-L02-A4.BG/2017','CNH-M2-SANTUARIO-EL GOLPE/2017', 'CNH-R02-L02-A5.BG/2017','CNH-R02-L03-VC-02/2017', 'CNH-R02-L03-BG-01/2017','CNH-R02-L02-A10.CS/2017', 'CNH-R02-L03-CS-01/2017',
              'CNH-R02-L02-A1.BG/2017', 'AE-0055-6M - MEZCALAPA - 05','CNH-M3-MISION/2018', 'CNH-A4.OGARRIO/2018','CNH-A3.CARDENAS-MORA/2018', 'AE-0032-5M - JOACHIN - 02','AR-0460-M - CAMPO SANTIAGO', 'CNH-R01-L03-A17/2016',
              'CNH-R01-L03-A24/2016', 'CNH-R01-L03-A4/2015', 'CNH-M4-EBANO/2018','CNH-M5-MIQUETLA/2018', 'AE-0070-2M - ANHELIDO - 02','CNH-R01-L03-A9/2015', 'AE-0056-4M - MEZCALAPA - 06','CNH-R01-L01-A7/2015', 
              'AE-0073-3M - PUCHUT - 01','CNH-R01-L03-A10/2016', 'CNH-R02-L03-TM-01/2017','CNH-R01-L02-A1/2015', 'AE-0053-4M - MEZCALAPA - 03','AE-0122-2M - TAMPICO MISANTLA', 'AE-0119-M - BURGOS','CNH-R03-L01-AS-CS-15/2018', 
              'AE-0060-5M - MEZCALAPA - 10','AE-0006-9M - AMOCA-YAXCHE - 04', 'A-0127-M - CAMPO ESCARBADO','AE-0154-2M - CHALABIL', 'AE-0151-M - UCHUKIL','CNH-R01-L02-A2/2015', 'AE-0020-3M - OKOM - 03',
              'AE-0009-5M - TUCOO-XAXAMANI - 01', 'AE-0024-3M - OKOM - 07','CNH-R02-L03-VC-01/2018', 'CNH-R02-L02-A7.BG/2017','AE-0142-4M - COMALCALCO', 'AE-0019-3M - OKOM - 02','CNH-R02-L03-VC-03/2017', 
              'AE-0045-7M - AGUA DULCE - 04','AE-0008-5M - AMOCA-YAXCHE - 06', 'CNH-R01-L02-A4/2015','AE-0143-2M - COMALCALCO', 'AE-0140-2M - COMALCALCO','AE-0148-2M - UCHUKIL', 'AE-0135-M - CUICHAPA','AE-0124-2M - LLAVE', 
              'CNH-R02-L03-BG-02/2017','AE-0136-M - CUICHAPA', 'A-0327-M - CAMPO TEKEL','AE-0141-3M - COMALCALCO', 'AE-0182-M - WAYA', 'AE-0130-M - LLAVE','AE-0166-M - CAMPECHE ORIENTE', 'AE-0153-M - UCHUKIL',
              'AE-0149-M - UCHUKIL', 'AE-0147-M - COMALCALCO','AE-0146-M - COMALCALCO', 'AE-0138-2M - CUICHAPA']
asig=st.selectbox('Seleccionar Asignación o Contrato',asignaciones)
#prod = pd.read_excel('Actualización Comportamiento Producción/prod_asignaciones_0125_01.xlsx')
#prod_2 = pd.read_excel('Actualización Comportamiento Producción/prod_asignaciones_0125_02.xlsx')
prod_3 = pd.read_excel('Actualización Comportamiento Producción/prod_asignaciones_0125_03.xlsx')
#prod=prod.drop('Unnamed: 0',axis=1)
#prod_2=prod_2.drop('Unnamed: 0',axis=1)
prod_3=prod_3.drop('Unnamed: 0',axis=1)
#prod_asig=pd.concat([prod,prod_2,prod_3])
#asig=st.selectbox('Seleccionar Asignación o Contrato',prod_asig['Asignación_o_Contrato'].unique())
#asig=st.selectbox('Seleccionar Asignación o Contrato',prod_3['Asignación_o_Contrato'].unique())
asig_df=prod_3[prod_3['Asignación_o_Contrato']==asig]
asig_tot=asig_df.groupby(['Fecha','Asignación_o_Contrato'])[['Petróleo_(Mbd)','Condensado_(Mbd)','Gas_(MMpcd)','Fw (%)']].sum()
asig_tot=asig_tot.reset_index()
if asig_tot['Petróleo_(Mbd)'].sum()>0:
    acep=px.line(asig_tot,x='Fecha',y='Petróleo_(Mbd)',title=f"Producción de aceite de la Asignación {asig}",
                 color_discrete_sequence=px.colors.qualitative.Antique)
if asig_tot['Condensado_(Mbd)'].sum()>0:
    acep=px.line(asig_tot,x='Fecha',y='Condensado_(Mbd)',title=f"Producción de condensado de la Asignación {asig}",
                 color_discrete_sequence=px.colors.qualitative.Antique)
gasp=px.line(asig_tot,x='Fecha',y='Gas_(MMpcd)',title=f"Producción de gas de la Asignación {asig}",
             color_discrete_sequence=px.colors.qualitative.Antique)
agup=px.scatter(asig_tot,x='Fecha',y='Fw (%)',title=f"Producción de agua de la Asignación {asig}",
                color_continuous_scale='Emerald')
st.plotly_chart(acep)
st.plotly_chart(gasp,use_container_width=True)
st.plotly_chart(agup)
#Podemos intentar hacerla más rápida si primero seleccionamos la asignación, luego creamos el df únicamente con esos datos.
#Revisar cálculos de agua Fw

'''
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
'''
