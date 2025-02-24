import streamlit as st
import pandas as pd
import plotly.express as px

# Título da Dashboard
st.title("Dashboard de Análise de Marketing")

# Carregar os dados
df = pd.read_csv('Data/ifood_df.csv')

# Exibir os dados
st.subheader("Dados Brutos")
st.write(df.head())

# Gráfico de Distribuição de Idade
st.subheader("Distribuição de Idade dos Clientes")
fig = px.histogram(df, x='Idade', nbins=20, title='Distribuição de Idade')
st.plotly_chart(fig)

# Gráfico de Barras: Estado Civil
st.subheader("Estado Civil dos Clientes")
fig = px.bar(df['Estado_Civil'].value_counts().reset_index(),
             x='index', y='Estado_Civil',
             labels={'index': 'Estado Civil', 'Estado_Civil': 'Contagem'},
             title='Contagem por Estado Civil')
st.plotly_chart(fig)

# Gráfico de Pizza: Distribuição de Gênero
st.subheader("Distribuição de Gênero")
fig = px.pie(df, names='Gênero', title='Proporção de Gênero')
st.plotly_chart(fig)

# Gráfico de Dispersão: Renda vs. Idade
st.subheader("Renda vs. Idade")
fig = px.scatter(df, x='Idade', y='Renda_Anual', color='Gênero',
                 title='Renda Anual vs. Idade')
st.plotly_chart(fig)
