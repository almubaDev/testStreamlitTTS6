import streamlit as st
import pandas as pd
import plotly_express as px


card_data = pd.read_csv('./vehicles_us.csv')

st.set_page_config(layout="wide", page_icon="🚗")
st.markdown(
    """
    <style>
    h1,h2,h3 {
        color: limegreen;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title('Car Data')
st.header('EDA')
st.subheader('Anuncios de venta de coches de US')


col1, col2 = st.columns(2)

with col1:
    hist_button = st.checkbox('Construir histograma')
    
    if hist_button:
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        fig = px.histogram(card_data, x='odometer')
        st.plotly_chart(fig, use_container_width=True)

with col2:
    scatt_button = st.button('Construir gráfico de dispersión') 

    if scatt_button:
        st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
        fig2 = px.scatter(card_data, x='odometer', y='price')
        st.plotly_chart(fig2, use_container_width=True)