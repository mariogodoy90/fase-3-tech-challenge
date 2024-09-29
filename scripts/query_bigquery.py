from google.cloud import bigquery
from google.oauth2 import service_account

import pandas as pd

def run_bigquery_query(query):
# Conectar ao BigQuery
    credentials = service_account.Credentials.from_service_account_file('credentials/bigquery_credentials.json')
    client = bigquery.Client(credentials=credentials)

    # Executar a consulta
    query_job = client.query(query)
    results = query_job.result()

    # Carregar os resultados em um DataFrame Pandas
    df = results.to_dataframe()

    return df