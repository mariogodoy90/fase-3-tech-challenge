from scripts.query_bigquery import run_bigquery_query
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def economia_renda_familiar():
    st.header("Análise Econômica: Renda Familiar")

    st.markdown("""
    **Motivo da Análise**  
    A crise causada pela COVID-19 impactou diretamente a renda familiar.  
    Esta análise avalia a distribuição da renda das famílias, com foco nas classes mais afetadas.
    """)

    query = """
    SELECT
        CASE
            WHEN CAST(c01012 AS FLOAT) <= 1000 THEN 'Até R$1000'
            WHEN CAST(c01012 AS FLOAT) BETWEEN 1001 AND 2000 THEN 'R$1001 - R$2000'
            WHEN CAST(c01012 AS FLOAT) BETWEEN 2001 AND 3000 THEN 'R$2001 - R$3000'
            WHEN CAST(c01012 AS FLOAT) BETWEEN 3001 AND 5000 THEN 'R$3001 - R$5000'
            WHEN CAST(c01012 AS FLOAT) > 5000 THEN 'Acima de R$5000'
            ELSE 'Desconhecido'
        END AS faixa_renda,
        COUNT(*) AS total_familias
    FROM 
        `basedosdados.br_ibge_pnad_covid.microdados`
    WHERE 
        (ano = 2020 AND mes IN (9, 10, 11))
    GROUP BY 
        faixa_renda
    ORDER BY 
        faixa_renda;
    """

    df = run_bigquery_query(query)
    st.dataframe(df)

    colors = sns.color_palette("Blues", n_colors=len(df))

    ax = df.plot(kind='bar', x='faixa_renda', color=colors, figsize=(10, 5))
    plt.title('Distribuição de Renda Familiar durante a Pandemia')
    plt.xlabel('Faixa de Renda')
    plt.ylabel('Número de Famílias')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    st.pyplot(plt)
    plt.close()

def economia_auxilio_emergencial():
    st.header("Análise Econômica: Acesso ao Auxílio Emergencial")

    st.markdown("""
    **Motivo da Análise**  
    O auxílio emergencial foi uma medida crítica para ajudar as famílias mais vulneráveis durante a pandemia.  
    Esta análise busca identificar quantas pessoas precisaram e receberam o auxílio, comparando com as regiões e faixas de renda.
    """)

    query = """
    SELECT
        CASE
            WHEN CAST(d0051 AS INT64) = 1 THEN 'Recebeu Auxílio'
            WHEN CAST(d0051 AS INT64) = 2 THEN 'Não Recebeu Auxílio'
            ELSE 'Desconhecido'
        END AS acesso_auxilio,
        COUNT(*) AS total_pessoas
    FROM 
        `basedosdados.br_ibge_pnad_covid.microdados`
    WHERE 
        (ano = 2020 AND mes IN (9, 10, 11))
    GROUP BY 
        acesso_auxilio
    ORDER BY 
        acesso_auxilio;
    """

    df = run_bigquery_query(query)
    st.dataframe(df)

    colors = sns.color_palette("OrRd", n_colors=len(df))

    ax = df.plot(kind='bar', x='acesso_auxilio', color=colors, figsize=(10, 5))
    plt.title('Acesso ao Auxílio Emergencial durante a Pandemia')
    plt.xlabel('Acesso ao Auxílio')
    plt.ylabel('Número de Pessoas')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    st.pyplot(plt)
    plt.close()
