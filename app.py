import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração do título do dashboard
st.title("Dashboard do Mercado Imobiliário em Petrópolis (2018-2024)")

# Leitura dos dados
@st.cache
def load_data():
    np.random.seed(42)
    num_imoveis = 1000
    area = np.random.randint(50, 300, num_imoveis)
    preco = np.random.randint(100000, 1000000, num_imoveis)
    quartos = np.random.randint(1, 6, num_imoveis)
    banheiros = np.random.randint(1, 4, num_imoveis)
    vagas_garagem = np.random.randint(0, 3, num_imoveis)
    ano_construcao = np.random.randint(2018, 2025, num_imoveis)
    data = pd.DataFrame({
        'Área (m²)': area,
        'Preço (R$)': preco,
        'Quartos': quartos,
        'Banheiros': banheiros,
        'Vagas de Garagem': vagas_garagem,
        'Ano de Construção': ano_construcao
    })
    return data

data = load_data()

# Filtro interativo por ano
ano_min = st.slider('Ano Mínimo de Construção', 2018, 2024, 2018)
ano_max = st.slider('Ano Máximo de Construção', 2018, 2024, 2024)
filtered_data = data[(data['Ano de Construção'] >= ano_min) & (data['Ano de Construção'] <= ano_max)]

# Exibição dos dados filtrados
st.subheader("Dados Filtrados")
st.write(filtered_data)

# Gráfico de dispersão - Preço vs Área
st.subheader("Gráfico de Dispersão: Preço vs Área")
fig, ax = plt.subplots()
sns.scatterplot(x='Área (m²)', y='Preço (R$)', data=filtered_data, hue='Ano de Construção', palette='viridis', ax=ax)
st.pyplot(fig)

# Gráficos de barras - Número de Quartos, Banheiros e Vagas de Garagem
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
sns.countplot(x='Quartos', data=filtered_data, palette='muted', ax=axs[0])
axs[0].set_title("Número de Quartos")
sns.countplot(x='Banheiros', data=filtered_data, palette='pastel', ax=axs[1])
axs[1].set_title("Número de Banheiros")
sns.countplot(x='Vagas de Garagem', data=filtered_data, palette='bright', ax=axs[2])
axs[2].set_title("Número de Vagas de Garagem")
st.pyplot(fig)

# Estatísticas descritivas
st.subheader("Estatísticas Descritivas")
st.write(filtered_data.describe())
