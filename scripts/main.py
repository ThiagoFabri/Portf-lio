import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Título da Dashboard
st.title("Dashboard de Métricas SaaS - Vendas e Marketing")

# Gerar dados fictícios para análise
data = pd.date_range(start='2024-01-01', periods=12, freq='M')
clientes = np.random.randint(50, 150, size=12)
cac = np.random.uniform(100, 500, size=12)
mrr = np.cumsum(np.random.uniform(5000, 15000, size=12))
churn = np.random.uniform(0.02, 0.15, size=12)

# Criar DataFrame
df = pd.DataFrame({
    'Mês': data,
    'Novos Clientes': clientes,
    'CAC (R$)': cac,
    'MRR (R$)': mrr,
    'Churn Rate': churn
})

# Exibir tabela
tabs = st.tabs(["Visão Geral", "CAC", "MRR", "Churn Rate"])

with tabs[0]:
    st.write(df)

with tabs[1]:
    fig_cac = px.line(df, x='Mês', y='CAC (R$)', title='Custo de Aquisição de Cliente')
    st.plotly_chart(fig_cac)

with tabs[2]:
    fig_mrr = px.line(df, x='Mês', y='MRR (R$)', title='Receita Recorrente Mensal')
    st.plotly_chart(fig_mrr)

with tabs[3]:
    fig_churn = px.line(df, x='Mês', y='Churn Rate', title='Taxa de Cancelamento (%)')
    st.plotly_chart(fig_churn)
