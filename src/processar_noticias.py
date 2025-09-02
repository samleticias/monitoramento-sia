import pandas as pd
import re
import os
import html

def limpar_normalizar_texto(texto):
    if not isinstance(texto, str):
        return ""

    texto = html.unescape(texto)
    texto = re.sub(r'<.*?>', '', texto)
    texto = re.sub(r'[^a-zA-ZÀ-ÿ0-9\s]', '', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto.lower()

def classificar_sentimento(texto, palavras_positivas, palavras_negativas):
    positivos = sum(1 for palavra in palavras_positivas if re.search(rf"\b{palavra}\b", texto))
    negativos = sum(1 for palavra in palavras_negativas if re.search(rf"\b{palavra}\b", texto))

    if positivos > negativos:
        return "Positivo"
    elif negativos > positivos:
        return "Negativo"
    else:
        return "Neutro"

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    caminho_arquivo = os.path.join(base_dir, "data", "noticias.csv")

    df = pd.read_csv(caminho_arquivo)

    palavras_positivas = [
        "inovação", "sucesso", "crescimento", "avanço", "positivo", "premiado",
        "parceria", "melhoria", "eficiente", "acessível", "promoção", "incentivo",
        "lançamento", "desenvolvido", "gratuito", "benefícios", "reconhecimento",
        "aprovação", "inauguração", "investimento", "capacitação", "treinamento",
        "premiação", "solução", "sustentável", "integração", "inteligente",
        "valorização", "eficaz", "qualidade", "inclusão", "tecnologia", "futuro",
        "digital", "conectividade", "ensino", "projeto", "ciência", "educação"
    ]

    palavras_negativas = [
        "crise", "problema", "dificuldade", "falha", "atraso", "risco", "insatisfação",
        "queda", "redução", "limitação", "demissão", "prejuízo", "conflito",
        "instabilidade", "corrupção", "falência", "descontrole", "descaso",
        "crítica", "negativo", "insegurança", "abandono", "falta", "polêmica",
        "contestação", "derrota", "insuficiente", "insatisfatório"
    ]

    # concatena título + descrição e limpa
    df["Texto_Completo"] = (df["Descricao"].fillna("")).apply(limpar_normalizar_texto)

    # classifica sentimento
    df["Sentimento"] = df["Texto_Completo"].apply(
        lambda texto: classificar_sentimento(texto, palavras_positivas, palavras_negativas)
    )

    caminho_saida = os.path.join(base_dir, "data", "noticias_processadas.csv")
    df.to_csv(caminho_saida, index=False, encoding="utf-8")

    print(df[["Titulo", "Sentimento"]])
    print(f"\nArquivo processado salvo em: {caminho_saida}")