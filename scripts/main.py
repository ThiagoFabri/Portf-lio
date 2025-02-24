import streamlit as st
import pandas as pd
import plotly.express as px

# Título da Dashboard
st.title("Dashboard de Preços de Combustíveis no Brasil")

# URL do dataset público (exemplo da ANP)
URL = "https://raw.githubusercontent.com/alura-cursos/agilizando-projetos-com-streamlit/main/gasolina.csv"

# Carregar dados
df = pd.read_csv(URL)
df['data'] = pd.to_datetime(df['data'])

# Criar gráfico
fig = px.line(df, x='data', y='venda', title='Variação do Preço da Gasolina', labels={'venda': 'Preço (R$)'})

# Exibir no Streamlit
st.plotly_chart(fig)

# Filtro por estado
estado = st.selectbox("Escolha um estado:", df['estado'].unique())
filtered_df = df[df['estado'] == estado]
fig2 = px.line(filtered_df, x='data', y='venda', title=f'Preço da Gasolina em {estado}')
st.plotly_chart(fig2)
