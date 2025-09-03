import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import os

st.set_page_config(page_title="Monitoramento IA no Piauí", layout="wide")
st.title("Monitoramento de Percepção Pública sobre IA no Piauí")
st.markdown("---")

# carregar dados
caminho_csv = os.path.join(os.path.dirname(__file__), "..", "data", "noticias_processadas.csv")
df = pd.read_csv(caminho_csv)

df['Data'] = pd.to_datetime(df['Data'], errors='coerce')

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
# métricas principais
# -----------------------------
total = len(df)
positivas = len(df[df['Sentimento']=="Positivo"])
negativas = len(df[df['Sentimento']=="Negativo"])
neutras = len(df[df['Sentimento']=="Neutro"])

st.subheader("Resumo Geral")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Notícias", total)
col2.metric("Positivas", positivas)
col3.metric("Negativas", negativas)
col4.metric("Neutras", neutras)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# gráficos principais lado a lado
# -----------------------------
col1, col2 = st.columns([1,2])

# -----------------------------
# 1. gráfico de pizza
# -----------------------------
with col1:
    st.subheader("Distribuição dos Sentimentos")
    sentimentos = df["Sentimento"].value_counts()
    cores = {"Positivo":"green", "Neutro":"gray", "Negativo":"red"}
    fig1, ax1 = plt.subplots(figsize=(4,4))
    ax1.pie(
        sentimentos,
        labels=sentimentos.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=[cores[label] for label in sentimentos.index],
        textprops={'fontsize': 12},
        labeldistance=1.1,
        pctdistance=0.6
    )
    ax1.axis("equal")
    st.pyplot(fig1)

# -----------------------------
# 2. nuvem de palavras
# -----------------------------
with col2:
    st.subheader("Nuvem de Palavras")
    texto_completo = " ".join(df["Texto_Completo"].astype(str))
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white",
        colormap="viridis",
        stopwords=stopwords_pt
    ).generate(texto_completo)
    fig2, ax2 = plt.subplots(figsize=(10,5))
    ax2.imshow(wordcloud, interpolation="bilinear")
    ax2.axis("off")
    st.pyplot(fig2)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# 3. tabela interativa
# -----------------------------
st.subheader("Tabela de Notícias Classificadas")
st.dataframe(df[["Titulo", "Sentimento", "Data", "Link", "Termo", "Texto_Completo"]])

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# 4. qtd de vezes que as palavras mais frequentes aparecem
# -----------------------------
st.subheader("Distribuição das Palavras Mais Frequentes")

def distribuicao_de_palavras_em_noticias(df):
    stopwords_extra = {
        "de","da","do","das","dos","a","o","as","os",
        "em","no","na","nos","nas","para","por","com","que",
        "um","uma","uns","umas","e","ou","se","ao","à","às",
        "lo","la","nosso","nossa","seu","sua","meu","minha",
        "estão","sobre", "nesta", "leva"
    }

    lista_palavras = []
    for texto in df['Texto_Completo'].dropna():
        palavras = set(texto.lower().split())
        palavras_filtradas = [p for p in palavras if p not in stopwords_extra and len(p) > 2]
        lista_palavras.extend(palavras_filtradas)

    palavras_freq = pd.Series(lista_palavras).value_counts().reset_index()
    palavras_freq.columns = ['Palavra', 'Noticias']
    palavras_freq = palavras_freq.head(50)

    fig = px.treemap(
        palavras_freq,
        path=['Palavra'],
        values='Noticias',
        color='Noticias',
        color_continuous_scale='Viridis',
        title=""
    )
    fig.update_layout(margin=dict(t=10, l=10, r=10, b=10), paper_bgcolor='white')
    st.plotly_chart(fig, use_container_width=True)

distribuicao_de_palavras_em_noticias(df)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# 5. ética e transparência
# -----------------------------
st.markdown("---")
st.subheader("Ética e Transparência")

st.markdown("⚠️ **Aviso sobre a análise de sentimento:** Esta análise é baseada em regras simples e pode não capturar sarcasmo ou contextos complexos.\n")

st.markdown("💡 **Como eu desenvolvi este dashboard:**")

st.markdown("**Etapas 100% realizadas por mim:**")
st.markdown("""
- **Coleta de notícias:** Leitura de arquivos CSV e integração de dados coletados.
- **Limpeza e normalização de textos:** Remoção de tags HTML, caracteres especiais e tratamento de strings.
- **Definição de palavras-chave para análise de sentimento:** Criação de listas de palavras positivas e negativas.
- **Classificação de sentimentos:** Implementação da lógica de identificação de sentimentos baseada em regras.
- **Construção de gráficos e tabelas:**
  - Gráfico de pizza da distribuição de sentimentos.
  - Nuvem de palavras com palavras filtradas.
  - Treemap mostrando palavras mais frequentes em diferentes notícias.
  - Tabela interativa com todos os dados processados.
""")

st.markdown("**Uso de IA como suporte:**")
st.markdown("""
- Filtragem de stopwords personalizadas: Escolha de palavras irrelevantes para a nuvem de palavras e treemap.
- Implementação da lógica de contagem de palavras: Quantificação de ocorrência das palavras nas notícias.
- Organização do layout no Streamlit: Definição de colunas, subheaders e disposição visual dos elementos.
- Ajustes de espaçamento, alinhamento e proporção de gráficos.
""")
