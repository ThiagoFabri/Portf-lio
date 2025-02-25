import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados (substitua pelo caminho correto do dataset)
df = pd.read_csv('Data/ifood_df.csv')  # Atualize com o nome correto do arquivo

# Configurar a página
st.set_page_config(page_title='Dashboard de Marketing', layout='wide')
st.title('📊 Dashboard de Análise de Clientes')

# Introdução
st.write("""
    ## Segmentação de Clientes para Estratégias de Marketing e Vendas

    O objetivo deste trabalho é realizar uma segmentação de clientes de uma plataforma de delivery (como o iFood) com base em características demográficas, comportamentais e de compra. A segmentação ajuda a personalizar as estratégias de marketing, aumentar a eficácia das campanhas e otimizar os investimentos em ações direcionadas.

    ### Motivos para a Segmentação:
    - **Personalização das campanhas de marketing**
    - **Melhora na alocação de recursos**
    - **Aprimoramento da fidelização**
    - **Identificação de novos segmentos de mercado**

    As variáveis utilizadas nesta segmentação incluem dados de compras, preferências e informações demográficas.
""")

# Apresentação dos Dados
st.write("""
    ### Visão Geral dos Dados
    Abaixo, apresentamos algumas estatísticas gerais dos clientes filtrados pela faixa de renda selecionada.
""")

# Filtros para faixa de renda
st.sidebar.header('Filtros')
income_range = st.sidebar.slider('Faixa de Renda', int(df['Income'].min()), int(df['Income'].max()),
                                 (int(df['Income'].min()), int(df['Income'].max())))
df_filtered = df[(df['Income'] >= income_range[0]) & (df['Income'] <= income_range[1])]

# Estatísticas descritivas
st.dataframe(df_filtered.describe())

# Explicação das Colunas
st.write("""
    ### Explicação das Colunas:
    - **Income**: A renda anual do cliente.
    - **Kidhome**: Quantidade de filhos pequenos (menores de 18 anos) que o cliente tem.
    - **Teenhome**: Quantidade de filhos adolescentes (entre 13 e 18 anos) que o cliente tem.
    - **Recency**: Número de dias desde a última compra do cliente na plataforma.
    - **MntWines**: Gastos do cliente com vinhos.
    - **MntFruits**: Gastos do cliente com frutas.
    - **MntMeatProducts**: Gastos do cliente com produtos de carne.
    - **MntFishProducts**: Gastos do cliente com produtos de peixe.
    - **MntSweetProducts**: Gastos do cliente com produtos doces.
    - **MntGoldProds**: Gastos do cliente com produtos de ouro.
    - **NumDealsPurchases**: Número de compras realizadas com desconto.
    - **NumWebPurchases**: Número de compras realizadas pelo site.
    - **NumCatalogPurchases**: Número de compras realizadas por catálogo.
    - **NumStorePurchases**: Número de compras realizadas na loja física.
    - **NumWebVisitsMonth**: Número de visitas ao site por mês.
    - **AcceptedCmp1**: Indicador binário de aceitação da campanha 1.
    - **AcceptedCmp2**: Indicador binário de aceitação da campanha 2.
    - **AcceptedCmp3**: Indicador binário de aceitação da campanha 3.
    - **AcceptedCmp4**: Indicador binário de aceitação da campanha 4.
    - **AcceptedCmp5**: Indicador binário de aceitação da campanha 5.
    - **Complain**: Se o cliente fez uma reclamação (0 ou 1).
    - **Z_CostContact**: Custo de contato com o cliente.
    - **Z_Revenue**: Receita gerada pelo cliente.
    - **Response**: Se o cliente respondeu à campanha de marketing (0 ou 1).
    - **Age**: Idade do cliente.
    - **Customer_Days**: Número de dias desde que o cliente se registrou na plataforma.
    - **marital_Divorced**: Se o cliente é divorciado (0 ou 1).
    - **marital_Married**: Se o cliente é casado (0 ou 1).
    - **marital_Single**: Se o cliente é solteiro (0 ou 1).
    - **marital_Together**: Se o cliente está em um relacionamento (0 ou 1).
    - **marital_Widow**: Se o cliente é viúvo (0 ou 1).
    - **education_2n Cycle**: Se o cliente tem o ensino secundário (0 ou 1).
    - **education_Basic**: Se o cliente tem ensino fundamental (0 ou 1).
    - **education_Graduation**: Se o cliente tem graduação (0 ou 1).
    - **education_Master**: Se o cliente tem mestrado (0 ou 1).
    - **education_PhD**: Se o cliente tem doutorado (0 ou 1).
    - **MntTotal**: Total gasto em todas as categorias de produtos.
    - **MntRegularProds**: Total gasto em produtos regulares (não promocionais).
    - **AcceptedCmpOverall**: Número total de campanhas de marketing aceitas pelo cliente.
""")


# Gráfico de Distribuição de Gastos
st.write('### Distribuição dos Gastos por Categoria')
categories = ['MntFishProducts', 'MntMeatProducts', 'MntFruits', 'MntSweetProducts', 'MntWines', 'MntGoldProds']
df_melted = df_filtered.melt(id_vars=['Income'], value_vars=categories, var_name='Categoria', value_name='Gasto')

fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=df_melted, x='Categoria', y='Gasto', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Verificação da existência de campanhas antes de gerar gráfico
if any(campaign in df.columns for campaign in
       ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']):
    st.write('### Taxa de Aceitação das Campanhas')
    campaigns = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'Response']
    campaign_counts = df_filtered[campaigns].sum()

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=campaign_counts.index, y=campaign_counts.values, ax=ax)
    ax.set_ylabel('Número de Aceites')
    st.pyplot(fig)
else:
    st.write('### Não há dados de campanhas para exibir')

# Comparação de Compras: Online vs. Loja
st.write('### Comparação de Compras: Online vs. Loja Física')
df_filtered['Total_Online'] = df_filtered['NumWebPurchases'] + df_filtered['NumCatalogPurchases']
df_filtered['Total_Loja'] = df_filtered['NumStorePurchases']
st.bar_chart(df_filtered[['Total_Online', 'Total_Loja']].sum())

st.write('Dashboard atualizado! 🎯')

