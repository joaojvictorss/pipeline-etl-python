# Pipeline ETL em Python (Pandas)

Projeto pessoal de ETL (Extract, Transform, Load) desenvolvido em Python para praticar limpeza, tratamento e estruturação de dados de vendas — uma peça de portfólio para vaga de **Analista de Dados júnior**.

##  Sobre o projeto

O script lê uma base de vendas em CSV, aplica um processo de limpeza e transformação de dados, e gera dois arquivos de saída (CSV e Excel) prontos para análise ou geração de relatórios.

### Etapas do pipeline

1. **Extract** — leitura do arquivo `dados_brutos.csv`.
2. **Transform**:
   - Remoção de linhas duplicadas
   - Preenchimento de valores nulos na coluna `produto` (com "Produto Genérico")
   - Preenchimento de valores nulos na coluna `data_venda`
   - Conversão da coluna `valor` para tipo numérico, tratando valores inválidos
   - Criação de uma nova coluna `categoria_ticket`, classificando cada venda como **"Valor padrão"** (≥ R$200) ou **"Padrão"** (< R$200)
3. **Load** — exportação dos dados tratados para `dados_tratados.csv` e `Relatorio_tratado.xlsx`.

## Tecnologias utilizadas

- Python 3
- [pandas](https://pandas.pydata.org/) — manipulação e tratamento de dados
- [openpyxl](https://openpyxl.readthedocs.io/) — exportação para Excel (usado internamente pelo pandas)

##  Estrutura do projeto
