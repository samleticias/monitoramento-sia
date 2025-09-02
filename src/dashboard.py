import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import os

# carregar dados
caminho_csv = os.path.join(os.path.dirname(__file__), "..", "data", "noticias_processadas.csv")
df = pd.read_csv(caminho_csv)

st.set_page_config(page_title="Monitoramento IA no Piauí", layout="wide")
st.title("📊 Monitoramento de Percepção Pública sobre IA no Piauí")

# -----------------------------
# stopwords personalizadas
# -----------------------------
stopwords_pt = set(STOPWORDS)
stopwords_pt.update([
    "de", "da", "do", "das", "dos", "em", "para", "por", "com", "sem",
    "ao", "aos", "à", "às", "na", "no", "nas", "nos", "sobre", "entre",
    "se", "são", "foi", "ser", "ter", "estar", "tem", "vai", "sendo",
    "feito", "pigovbr", "govbr", "pelo", "neste", "é"
])

# -----------------------------
# 1. gráfico de pizza
# -----------------------------
st.subheader("Distribuição dos Sentimentos")

sentimentos = df["Sentimento"].value_counts()

cores = {
    "Positivo": "green",
    "Neutro": "gray",
    "Negativo": "red"
}

col1, col2, col3 = st.columns([1, 2, 1])  

with col2:
    fig1, ax1 = plt.subplots(figsize=(1.5, 1.5))  
    ax1.pie(
        sentimentos,
        labels=sentimentos.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=[cores[label] for label in sentimentos.index],
        textprops={'fontsize': 5},   
        labeldistance=1.1,
        pctdistance=0.6
    )
    ax1.axis("equal")
    st.pyplot(fig1)

# -----------------------------
# 2. nuvem de palavras
# -----------------------------
st.subheader("Nuvem de Palavras")

texto_completo = " ".join(df["Texto_Completo"].astype(str))

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    colormap="viridis",
    stopwords=stopwords_pt
).generate(texto_completo)

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.imshow(wordcloud, interpolation="bilinear")
ax2.axis("off")
st.pyplot(fig2)

# -----------------------------
# 3. tabela interativa
# -----------------------------
st.subheader("Tabela de Notícias Classificadas")
st.dataframe(df[["Titulo", "Sentimento", "Link", "Termo", "Texto_Completo"]])
