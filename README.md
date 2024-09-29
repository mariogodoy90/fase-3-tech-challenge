
# Projeto Final Fase 3

Focando na análise de dados utilizando Python, BigQuery e Streamlit. O objetivo é analisar diferentes aspectos de um conjunto de dados, cruzando variáveis relacionadas a **Sintomas**, **Comportamento** e **Economia**. O projeto também inclui um sistema de recomendações baseado nos dados analisados.

## Estrutura do Projeto

- **`app.py`**: Arquivo principal da aplicação, responsável por rodar a interface Streamlit e exibir os resultados das análises.
- **`query_bigquery.py`**: Script para realizar consultas no Google BigQuery.
- **`comportamento.py`**: Responsável pelas análises relacionadas ao comportamento.
- **`economia.py`**: Foca na análise de dados econômicos.
- **`sintomas.py`**: Responsável pela análise dos dados de sintomas.
- **`recomendacoes.py`**: Contém a lógica para gerar recomendações baseadas nas análises.

## Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Conta e credenciais do Google Cloud BigQuery

### Configuração

1. Clone o repositório para sua máquina local.

```bash
git clone <url-do-repositorio>
cd <pasta-do-repositorio>
```

2. Instale as dependências necessárias listadas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

As dependências necessárias incluem:
- Streamlit para criação da interface web
- Pandas para manipulação de dados
- Google Cloud BigQuery para consulta do dataset
- Google Auth para autenticação com os serviços da Google
- Matplotlib para geração de gráficos
- Seaborn para visualizações avançadas de dados

### Configuração das Credenciais

As credenciais do Google Cloud BigQuery são carregadas diretamente no código. Certifique-se de que o arquivo de credenciais está no caminho `credentials/bigquery_credentials.json`. O código já está configurado para buscar as credenciais neste local utilizando o seguinte trecho:

```python
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('credentials/bigquery_credentials.json')
```

## Uso

Após configurar tudo, você pode rodar a aplicação executando o seguinte comando:

```bash
streamlit run app.py
```

Isso iniciará um servidor local do Streamlit e abrirá a interface no seu navegador padrão.

## Funcionalidades

### Análise de Sintomas
- **Arquivo**: `sintomas.py`
- Contém várias análises relacionadas aos sintomas clínicos, cruzando variáveis como idade, sexo e região.

### Análise de Comportamento
- **Arquivo**: `comportamento.py`
- Foca em dados comportamentais, cruzando fatores como educação, região e outros dados demográficos.

### Análise Econômica
- **Arquivo**: `economia.py`
- Analisa fatores econômicos, como renda, emprego e auxílios recebidos durante a pandemia.

### Recomendações
- **Arquivo**: `recomendacoes.py`
- Oferece recomendações com base nas análises realizadas, ajudando formuladores de políticas ou pesquisadores a entenderem as principais conclusões.
