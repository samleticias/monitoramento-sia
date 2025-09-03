import requests
import xml.etree.ElementTree as ET
import pandas as pd
import os
from datetime import datetime

def coletar_noticias(termo_busca, limite=15):
    """
    Função para coleta de notícias do Google News RSS com base em um termo de busca.
    Retorna um DataFrame com título, link e descrição de cada notícia.
    """
    # URL do feed RSS
    url = f"https://news.google.com/rss/search?q={termo_busca}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    resposta = requests.get(url)
    if resposta.status_code != 200:
        print("erro ao acessar o feed:", resposta.status_code)
        return None

    raiz = ET.fromstring(resposta.content)
    noticias = []
    for item in raiz.findall(".//item")[:limite]:
        titulo = item.find("title").text
        link = item.find("link").text
        descricao = item.find("description").text
        pubDate = item.find("pubDate").text if item.find("pubDate") is not None else None
        if pubDate:
            try:
                data_noticia = datetime.strptime(pubDate, "%a, %d %b %Y %H:%M:%S %Z")
            except ValueError:
                data_noticia = None
        else:
            data_noticia = None
        noticias.append([titulo, link, descricao, termo_busca, data_noticia])

    # converte em DataFrame
    return pd.DataFrame(noticias, columns=["Titulo", "Link", "Descricao", "Termo", "Data"])

if __name__ == "__main__":
    termos = ["Inteligência Artificial Piauí", "SIA Piauí"]

    todas_noticias = pd.DataFrame(columns=["Titulo", "Link", "Descricao", "Termo"])
    for termo in termos:
        df = coletar_noticias(termo, limite=15)
        if df is not None:
            todas_noticias = pd.concat([todas_noticias, df], ignore_index=True)

    # remove duplicadas pelo link
    todas_noticias = todas_noticias.drop_duplicates(subset='Link', keep='first')

    # embaralha e pegar apenas 20 notícias
    todas_noticias = todas_noticias.sample(frac=1, random_state=42).head(20)

    print(f"Total de notícias coletadas: {len(todas_noticias)}")
    print("Primeiras notícias coletadas:")
    print(todas_noticias)

    # salva CSV
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pasta_data = os.path.join(base_dir, "data")
    os.makedirs(pasta_data, exist_ok=True)
    caminho_arquivo = os.path.join(pasta_data, "noticias.csv")
    todas_noticias.to_csv(caminho_arquivo, index=False, encoding="utf-8")
    print(f"\narquivo salvo em: {caminho_arquivo}")