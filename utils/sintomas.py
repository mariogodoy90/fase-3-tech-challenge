from scripts.query_bigquery import run_bigquery_query
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Sintomas por Idade
def sintomas_por_idade():
    st.header("Distribuição de Sintomas por Faixa Etária")

    # Análise
    st.markdown("""
    **Análise:**
    A análise por faixa etária é fundamental para entender como diferentes grupos etários foram afetados pela COVID-19. 
    Crianças e adolescentes (0-17) tendem a apresentar sintomas mais leves, enquanto idosos (60+) são mais vulneráveis 
    a sintomas graves. Com essa análise, podemos observar padrões específicos e oferecer subsídios para o desenvolvimento 
    de políticas públicas, como campanhas de vacinação e alocação de recursos médicos.
    """)


    query = """
    SELECT 
        CASE
            WHEN CAST(a002 AS INT64) BETWEEN 0 AND 17 THEN '0-17'
            WHEN CAST(a002 AS INT64) BETWEEN 18 AND 29 THEN '18-29'
            WHEN CAST(a002 AS INT64) BETWEEN 30 AND 44 THEN '30-44'
            WHEN CAST(a002 AS INT64) BETWEEN 45 AND 59 THEN '45-59'
            WHEN CAST(a002 AS INT64) >= 60 THEN '60+'
            ELSE 'Desconhecido'
        END AS faixa_etaria,
        SUM(CAST(b0011 AS INT64)) AS total_febre,
        SUM(CAST(b0012 AS INT64)) AS total_tosse,
        SUM(CAST(b0014 AS INT64)) AS total_dificuldade_respiratoria,
        SUM(CAST(b00111 AS INT64)) AS total_perda_cheiro_sabor
    FROM 
        `basedosdados.br_ibge_pnad_covid.microdados`
    WHERE 
        (ano = 2020 AND mes IN (9, 10, 11))
    GROUP BY 
        faixa_etaria
    ORDER BY 
        faixa_etaria;
    """
    df = run_bigquery_query(query)

    st.write("Sintomas por Faixa Etária")
    st.dataframe(df)

    # Aplicar uma paleta de cores com degradê (Blues)
    colors = sns.color_palette("Blues", n_colors=len(df))

    # Gráfico de barras lado a lado com faixas etárias e aplicação do degradê
    ax = df.plot(kind='bar', x='faixa_etaria', color=colors, figsize=(10, 5))  # Remover stacked=True
    plt.title('Distribuição de Sintomas por Faixa Etária')
    plt.xlabel('Faixa Etária')
    plt.ylabel('Frequência')

    # Mover a legenda para fora do gráfico, se necessário
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot(plt)
    plt.close()
    
# 2. Sintomas por Sexo
def sintomas_por_sexo():
    st.header("Distribuição de Sintomas por Sexo")

    # Análise
    st.markdown("""
    **Análise:**
    A análise por sexo ajuda a identificar se homens e mulheres foram afetados de maneira diferente pela COVID-19. 
    Estudos indicam que homens são mais propensos a desenvolver sintomas graves, enquanto mulheres, em geral, 
    relatam sintomas mais leves. Compreender essas diferenças pode ajudar a direcionar políticas de saúde específicas 
    para cada grupo.
    """)

    query = """
    SELECT
        CASE
            WHEN CAST(a003 AS INT64) = 1 THEN 'Homem'
            WHEN CAST(a003 AS INT64) = 2 THEN 'Mulher'
            ELSE 'Desconhecido'
        END AS sexo,
        SUM(CAST(b0011 AS INT64)) AS total_febre,
        SUM(CAST(b0012 AS INT64)) AS total_tosse,
        SUM(CAST(b0014 AS INT64)) AS total_dificuldade_respiratoria,
        SUM(CAST(b00111 AS INT64)) AS total_perda_cheiro_sabor
    FROM 
        `basedosdados.br_ibge_pnad_covid.microdados`
    WHERE 
        (ano = 2020 AND mes IN (9, 10, 11))
    GROUP BY 
        sexo
    ORDER BY 
        sexo;
    """
    df = run_bigquery_query(query)

    st.write("Sintomas por Sexo")
    st.dataframe(df)

    # Aplicar paleta de cores (OrRd)
    colors = sns.color_palette("OrRd", n_colors=len(df))

    # Gráfico de barras lado a lado com aplicação do degradê
    ax = df.plot(kind='bar', x='sexo', color=colors, figsize=(10, 5))
    plt.title('Distribuição de Sintomas por Sexo')
    plt.xlabel('Sexo')
    plt.ylabel('Frequência')

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot(plt)
    plt.close()

# 3. Sintomas e Uso de Máscara
def sintomas_uso_mascara():
    st.header("Distribuição de Sintomas por Uso de Máscara")

    # Análise
    st.markdown("""
    **Análise:**
    O uso de máscaras foi amplamente recomendado como uma medida preventiva contra a COVID-19. 
    Esta análise explora se aqueles que usaram máscaras regularmente tiveram menos sintomas 
    comparados aos que não seguiram essa recomendação. Ela também pode mostrar a eficácia das máscaras 
    na prevenção de sintomas graves.
    """)

    query = """
    SELECT
        CASE
            WHEN CAST(f002a3 AS INT64) = 1 THEN 'Sim'
            WHEN CAST(f002a3 AS INT64) = 2 THEN 'Não'
            WHEN CAST(f002a3 AS INT64) = 3 THEN 'Não Sabe'
            ELSE 'Desconhecido'
        END AS uso_mascara,
        SUM(CAST(b0011 AS INT64)) AS total_febre,
        SUM(CAST(b0012 AS INT64)) AS total_tosse,
        SUM(CAST(b0014 AS INT64)) AS total_dificuldade_respiratoria,
        SUM(CAST(b00111 AS INT64)) AS total_perda_cheiro_sabor
    FROM 
        `basedosdados.br_ibge_pnad_covid.microdados`
    WHERE 
        (ano = 2020 AND mes IN (9, 10, 11))
    GROUP BY 
        uso_mascara
    ORDER BY 
        uso_mascara;
    """
    df = run_bigquery_query(query)

    st.write("Sintomas e Uso de Máscara")
    st.dataframe(df)

    # Aplicar paleta de cores (Blues)
    colors = sns.color_palette("Blues", n_colors=len(df))

    # Gráfico de barras lado a lado com aplicação do degradê
    ax = df.plot(kind='bar', x='uso_mascara', color=colors, figsize=(10, 5))
    plt.title('Distribuição de Sintomas por Uso de Máscara')
    plt.xlabel('Uso de Máscara')
    plt.ylabel('Frequência')

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot(plt)
    plt.close()

# 4. Sintomas e Uso de Máscara
def sintomas_por_regiao():
    st.header("Distribuição de Sintomas por Região")

    # Análise Goal
    st.markdown("""
    **Análise:**
    As regiões do Brasil variam amplamente em termos de infraestrutura de saúde, condições climáticas e densidade populacional. 
    Este cruzamento permite observar as disparidades regionais na prevalência de sintomas e na gravidade da COVID-19, 
    destacando as áreas que podem ter sido mais afetadas e que necessitam de maior suporte.
    """)

    query = """
    SELECT 
        sigla_uf AS Regiao,
        SUM(CAST(b0011 AS INT64)) AS Febre,
        SUM(CAST(b0012 AS INT64)) AS Tose,
        SUM(CAST(b0014 AS INT64)) AS Dificuldade_Respiratoria,
        SUM(CAST(b00111 AS INT64)) AS Perda_Olfato_Paladar
    FROM 
        `basedosdados.br_ibge_pnad_covid.microdados`
    WHERE 
        (ano = 2020 AND mes IN (9, 10, 11))
    GROUP BY 
        Regiao
    ORDER BY 
        Regiao;
    """
    df = run_bigquery_query(query)

    st.write("Sintomas por Região")
    st.dataframe(df)

    # Aplicar paleta de cores (OrRd)
    colors = sns.color_palette("OrRd", n_colors=len(df))

    # Gráfico de barras lado a lado com aplicação do degradê
    ax = df.plot(kind='bar', x='Regiao', color=colors, figsize=(10, 5))
    plt.title('Distribuição de Sintomas por Região')
    plt.xlabel('Região')
    plt.ylabel('Frequência')

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot(plt)
    plt.close()

# 5. Sintomas e Plano de Saude
def sintomas_por_plano_saude():
    st.header("Distribuição de Sintomas por Plano de Saúde")

 # Análise Goal
    st.markdown("""
    **Análise:**
    O acesso à saúde é um fator crítico na gestão da COVID-19. Esta análise revela se pessoas com plano de saúde, 
    seja público ou privado, apresentaram menos sintomas graves em comparação àquelas sem cobertura.
    """)

    query = """
    SELECT
        CASE
            WHEN CAST(b008 AS INT64) = 1 THEN 'Sim'
            WHEN CAST(b008 AS INT64) = 2 THEN 'Não'
            ELSE 'Desconhecido'
        END AS plano_saude,
        SUM(CAST(b0011 AS INT64)) AS total_febre,
        SUM(CAST(b0012 AS INT64)) AS total_tosse,
        SUM(CAST(b0014 AS INT64)) AS total_dificuldade_respiratoria,
        SUM(CAST(b00111 AS INT64)) AS total_perda_cheiro_sabor
    FROM 
        `basedosdados.br_ibge_pnad_covid.microdados`
    WHERE
        CAST(b008 AS INT64) IN (1, 2) -- Filtrar apenas Sim e Não para plano de saúde
        AND (ano = 2020 AND mes IN (9, 10, 11))
    GROUP BY 
        plano_saude
    ORDER BY 
        plano_saude;
    """
    df = run_bigquery_query(query)

    st.write("Sintomas por Plano de Saúde")
    st.dataframe(df)

    # Aplicar paleta de cores (Blues)
    colors = sns.color_palette("Blues", n_colors=len(df))

    # Gráfico de barras lado a lado com aplicação do degradê
    ax = df.plot(kind='bar', x='plano_saude', color=colors, figsize=(10, 5))
    plt.title('Distribuição de Sintomas por Plano de Saúde')
    plt.xlabel('Plano de Saúde')
    plt.ylabel('Frequência')

    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    st.pyplot(plt)
    plt.close()