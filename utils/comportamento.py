from scripts.query_bigquery import run_bigquery_query
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def comportamento_trabalho():
    st.header("Análise de Comportamento: Trabalho")

    st.markdown("""
    **Motivo da Análise**  
    A pandemia alterou profundamente o mercado de trabalho, com uma grande parte da população migrando para o trabalho remoto.
    Essa análise busca entender o percentual de pessoas que continuaram trabalhando de casa, comparando com aqueles que saíram para trabalhar ou perderam seus empregos.
    """)

    query = """
    SELECT
        CASE
            WHEN CAST(c013 AS INT64) = 1 THEN 'Sim, Trabalho Remoto'
            WHEN CAST(c013 AS INT64) = 2 THEN 'Não, Trabalho Presencial'
            ELSE 'Desconhecido'
        END AS trabalho_remoto,
        COUNT(*) AS total_pessoas
    FROM 
        `basedosdados.br_ibge_pnad_covid.microdados`
    WHERE
        CAST(c013 AS INT64) IN (1, 2)
        AND (ano = 2020 AND mes IN (9, 10, 11))
    GROUP BY 
        trabalho_remoto
    ORDER BY 
        trabalho_remoto;
    """

    df = run_bigquery_query(query)
    st.dataframe(df)

    colors = sns.color_palette("Blues", n_colors=len(df))

    ax = df.plot(kind='bar', x='trabalho_remoto', color=colors, figsize=(10, 5))
    plt.title('Distribuição da População por Trabalho Remoto ou Presencial')
    plt.xlabel('Situação de Trabalho')
    plt.ylabel('Número de Pessoas')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    st.pyplot(plt)
    plt.close()

def comportamento_distanciamento_social():
    st.header("Análise de Comportamento: Distanciamento Social")

    st.markdown("""
    **Motivo da Análise**  
    O distanciamento social foi uma das medidas mais amplamente recomendadas para prevenir a disseminação do vírus.
    Esta análise busca identificar quantas pessoas aderiram à prática e quantas continuaram com suas atividades habituais.
    """)

    query = """
    SELECT
        CASE
            WHEN CAST(b011 AS INT64) = 1 THEN 'Não Restringiu'
            WHEN CAST(b011 AS INT64) = 2 THEN 'Restringiu Parcialmente'
            WHEN CAST(b011 AS INT64) = 3 THEN 'Restringiu Rigorosamente'
            WHEN CAST(b011 AS INT64) = 4 THEN 'Restringiu Totalmente'
            ELSE 'Desconhecido'
        END AS distanciamento_social,
        COUNT(*) AS total_pessoas
    FROM 
        `basedosdados.br_ibge_pnad_covid.microdados`
    WHERE
        CAST(b011 AS INT64) IN (1, 2, 3, 4)
        AND (ano = 2020 AND mes IN (9, 10, 11))
    GROUP BY 
        distanciamento_social
    ORDER BY 
        distanciamento_social;
    """

    df = run_bigquery_query(query)
    st.dataframe(df)

    colors = sns.color_palette("OrRd", n_colors=len(df))

    ax = df.plot(kind='bar', x='distanciamento_social', color=colors, figsize=(10, 5))
    plt.title('Adesão ao Distanciamento Social')
    plt.xlabel('Adesão ao Distanciamento')
    plt.ylabel('Número de Pessoas')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    st.pyplot(plt)
    plt.close()

