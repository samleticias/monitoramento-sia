# DECISIONS - Monitoramento de Notícias sobre IA no Piauí

### 1. Por que você escolheu a abordagem de regras para análise de sentimento (em vez de um modelo de ML)?

Decidi usar uma abordagem baseada em regras (listas de palavras positivas e negativas) em vez de um modelo de Machine Learning pelos seguintes motivos:

- Queria algo simples e transparente, que eu pudesse explicar claramente como cada notícia é classificada.
- Não tinha muitos dados disponíveis (~20 notícias por execução), então um modelo de ML não teria dados suficientes para treinar de forma confiável.
- Com listas de palavras, eu consigo personalizar diretamente quais termos indicam sentimentos positivos ou negativos, considerando o contexto local do Piauí.
- A execução é mais rápida, ideal para um dashboard interativo, sem precisar treinar ou carregar modelos complexos.

### 2. Como você lidou com possíveis erros ou falta de notícias no feed RSS?

- Verifico o status da requisição antes de processar o feed; se houver erro, o programa continua sem travar.
- Caso o feed retorne menos notícias que o limite definido, eu apenas uso o que estiver disponível.
- Para evitar problemas com textos vazios ou incompletos, aplico `fillna` antes da limpeza e classificação.
- Removo links duplicados para não contar a mesma notícia mais de uma vez.