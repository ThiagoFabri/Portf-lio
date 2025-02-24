import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados (substitua pelo caminho correto do dataset)
df = pd.read_csv('marketing_data.csv')  # Atualize com o nome correto do arquivo

# Configurar a página
st.set_page_config(page_title='Dashboard de Marketing', layout='wide')
st.title('📊 Dashboard de Análise de Clientes')

# Mostrar algumas estatísticas gerais
st.sidebar.header('Filtros')
income_range = st.sidebar.slider('Faixa de Renda', int(df['Income'].min()), int(df['Income'].max()), (int(df['Income'].min()), int(df['Income'].max())))
df_filtered = df[(df['Income'] >= income_range[0]) & (df['Income'] <= income_range[1])]

st.write('### Visão Geral dos Clientes')
st.dataframe(df_filtered.describe())

# Gráfico de Distribuição de Gastos
st.write('### Distribuição dos Gastos por Categoria')
categories = ['MntFishProducts', 'MntMeatProducts', 'MntFruits', 'MntSweetProducts', 'MntWines', 'MntGoldProds']
df_melted = df_filtered.melt(id_vars=['Income'], value_vars=categories, var_name='Categoria', value_name='Gasto')

fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=df_melted, x='Categoria', y='Gasto', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Aceitação de Ofertas
st.write('### Taxa de Aceitação das Campanhas')
campaigns = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'Response (target)']
campaign_counts = df_filtered[campaigns].sum()

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=campaign_counts.index, y=campaign_counts.values, ax=ax)
ax.set_ylabel('Número de Aceites')
st.pyplot(fig)

# Compras Online vs. Lojas
st.write('### Comparação de Compras: Online vs. Loja Física')
df_filtered['Total_Online'] = df_filtered['NumWebPurchases'] + df_filtered['NumCatalogPurchases']
df_filtered['Total_Loja'] = df_filtered['NumStorePurchases']
st.bar_chart(df_filtered[['Total_Online', 'Total_Loja']].sum())

st.write('Dashboard atualizado! 🎯')
