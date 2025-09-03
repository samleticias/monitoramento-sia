# Monitoramento de Notícias sobre IA no Piauí

Este projeto demonstra um fluxo de trabalho para acompanhar e interpretar notícias sobre Inteligência Artificial (IA) no estado do Piauí. A aplicação faz a extração de conteúdos do Google News por meio de RSS, executa a limpeza e padronização dos textos, aplica uma avaliação de sentimentos baseada em regras simples e apresenta os resultados em um painel interativo com Streamlit.

A solução é organizada em diferentes scripts Python que atuam de forma sequencial, permitindo coletar, processar e disponibilizar os dados de maneira estruturada para facilitar a análise visual.

## Estrutura do Projeto
```bash
monitoramento-ia-piaui/
│
├── src/ # código fonte (coleta, processamento e dashboard)
│   ├── coleta_dados.py
│   ├── processar_noticias.py
│   └── dashboard.py
│
├── data/ # dados coletados e processados
│   ├── noticias.csv
│   └── noticias_processadas.csv
│
├── README.md
├── requirements.txt # bibliotecas necessárias
└── .gitignore
```

## Bibliotecas Utilizadas

- **pandas**: Manipulação e análise de dados.
- **requests**: Coleta de dados via HTTP.
- **streamlit**: Criação de dashboards interativos.
- **matplotlib**: Gráficos estáticos 2D.
- **plotly**: Gráficos interativos.
- **wordcloud**: Geração de nuvens de palavras.

## Setup

1. Clonar repositório:
```bash
git clone https://github.com/samleticias/monitoramento-sia
cd monitoramento-sia
```

2. Criar ambiente virtual (opcional):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependências:
```bash
pip install -r requirements.txt
```

## Execução

1. Coletar notícias:
```bash
python src/coleta_dados.py
```

2. Processar notícias:
```bash
python src/processar_noticias.py
```

3. Executar dashboard:
```bash
streamlit run src/dashboard.py
```

## Observações e Considerações Éticas

- A classificação de sentimentos segue regras simples de palavras-chave e pode não refletir com precisão nuances como ironia, sarcasmo ou contexto cultural.  
- As informações utilizadas são obtidas apenas de fontes públicas (Google News RSS).  
- Para usos estratégicos ou análises críticas, recomenda-se complementar com uma revisão humana.  
- O projeto foi desenvolvido respeitando os termos de uso dos serviços acessados.
- Os resultados apresentados não devem ser interpretados como análises conclusivas sobre a percepção pública.
- Este projeto foi desenvolvido para fins educacionais e de demonstração técnica.  

#### Feito por Sammya Letícia 
[LinkedIn](https://www.linkedin.com/in/sammyavaladao)
