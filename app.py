
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌍 Dashboard - Relatório Mundial da Felicidade (2021)")

df = pd.read_csv("world-happiness-report-2021.csv")

regioes = df['Regional indicator'].unique()
regiao_selecionada = st.selectbox("Selecione uma região", regioes)

df_filtrado = df[df['Regional indicator'] == regiao_selecionada]

st.subheader(f"Tabela de países da região: {regiao_selecionada}")
st.dataframe(df_filtrado)

st.subheader("Gráfico de Linha - Score da felicidade")
fig1, ax1 = plt.subplots()
ax1.plot(df_filtrado['Country name'], df_filtrado['Ladder score'], marker='o')
plt.xticks(rotation=90)
plt.ylabel('Ladder Score')
st.pyplot(fig1)

st.subheader("Gráfico de Barras - GDP per capita")
fig2, ax2 = plt.subplots()
ax2.bar(df_filtrado['Country name'], df_filtrado['Logged GDP per capita'])
plt.xticks(rotation=90)
plt.ylabel('GDP')
st.pyplot(fig2)

st.subheader("Gráfico de Dispersão - Felicidade x PIB per capita")
fig3, ax3 = plt.subplots()
ax3.scatter(df_filtrado['Logged GDP per capita'], df_filtrado['Ladder score'])
ax3.set_xlabel('GDP per capita')
ax3.set_ylabel('Ladder Score')
st.pyplot(fig3)

st.subheader("Gráfico de Pizza - Quantidade de países por região")
regiao_count = df['Regional indicator'].value_counts()
fig4, ax4 = plt.subplots()
ax4.pie(regiao_count, labels=regiao_count.index, autopct='%1.1f%%')
st.pyplot(fig4)
