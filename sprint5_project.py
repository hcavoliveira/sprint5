import pandas as pd
import plotly.express as px
import streamlit as st

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

st.title('Análise de dados de veículos')
st.write('Para gerar um histograma ou gráfico de dispersão, clique nos botões abaixo')

vehicles = pd.read_csv('vehicles.csv')
hist_button = st.button('Criar Histograma')
scat_button = st.button('Criar Gráfico de Dispersão')

if hist_button:
    st.write("Criando um histograma com os valores dos odômetros de cada veículo")
    hist = px.histogram(vehicles, x='odometer')
    hist.update_layout(
        xaxis_title="Odômetro",
        yaxis_title="Contagem"
    )
    st.plotly_chart(hist, use_container_width=True)

if scat_button:
    st.write("Criando um gráfico de dispersão com os valores dos odômetros e os preços de cada veículo")
    scat = px.scatter(vehicles, x='odometer', y='price')
    scat.update_layout(
        xaxis_title="Odômetro",
        yaxis_title="Preço"
    )
    st.plotly_chart(scat, use_container_width=True)
