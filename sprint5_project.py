import pandas as pd
import plotly.express as px
import streamlit as st

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

vehicles = pd.read_csv('vehicles.csv')
hist_button = st.button('Criar Histograma')
scat_button = st.button('Criar Gráfico de Dispersão')

if hist_button:
    st.write("Criando um histograma para o conjunto de dados")
    hist = px.histogram(vehicles, x='odometer')
    st.plotly_chart(hist, use_container_width=True)

if scat_button:
    st.write("Criando um gráfico de dispersão para o conjunto de dados")
    scat = px.scatter(vehicles, x='odometer', y='price')
    st.plotly_chart(scat, use_container_width=True)
