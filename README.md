# Monitoramento de Notícias sobre IA no Piauí

Este projeto coleta notícias sobre Inteligência Artificial no Piauí, processa o texto para limpeza e análise de sentimento, e exibe visualizações em um dashboard interativo.

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
