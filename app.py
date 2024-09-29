import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.sintomas import sintomas_por_idade, sintomas_por_sexo, sintomas_uso_mascara, sintomas_por_regiao, sintomas_por_plano_saude
from utils.comportamento import comportamento_trabalho, comportamento_distanciamento_social
from utils.economia import economia_renda_familiar, economia_auxilio_emergencial
from utils.recomendacoes import pagina_recomendacoes

# Função da página inicial
def pagina_inicial():
    st.title("Análise do Impacto da COVID-19 no Brasil")

    st.markdown("""
    ## Projeto de Análise da COVID-19
    Este projeto tem como objetivo realizar uma análise detalhada sobre o impacto da pandemia de COVID-19 no Brasil, utilizando dados da **PNAD-COVID-19** coletados pelo **IBGE** durante o ano de 2020. Através de uma série de cruzamentos de variáveis, investigamos três áreas principais:
    
    ### 1. Sintomas de COVID-19
    Analisamos como diferentes grupos demográficos foram afetados pelos sintomas da COVID-19, levando em consideração fatores como idade, sexo, uso de máscaras e região de residência. Nosso objetivo é identificar padrões que possam ajudar a direcionar intervenções de saúde pública.

    ### 2. Comportamento da População
    Exploramos como a pandemia afetou o comportamento social e de trabalho da população, incluindo a adoção do trabalho remoto e a adesão ao distanciamento social. Essa análise é crucial para entender como as mudanças comportamentais contribuíram para a contenção ou disseminação do vírus.

    ### 3. Impactos Econômicos
    Avaliamos os efeitos econômicos da pandemia, com foco na perda de renda e no acesso a auxílios emergenciais. Através dessa análise, buscamos identificar as populações mais vulneráveis economicamente e como o auxílio governamental impactou essas famílias.

    ## Período de Análise
    Utilizamos os dados de três meses chave: **setembro, outubro e novembro de 2020**. Esses meses foram selecionados por representarem um período em que o Brasil enfrentava desafios significativos tanto na saúde pública quanto na economia, oferecendo uma visão abrangente do impacto da pandemia ao longo do tempo.

    ## Fontes de Dados
    A análise foi realizada com base nos microdados da Pesquisa Nacional por Amostra de Domicílios (PNAD) COVID-19, disponibilizada pelo IBGE. As variáveis selecionadas incluem:
    - **Sintomas reportados**: Febre, tosse, dificuldade respiratória, entre outros.
    - **Comportamento social**: Trabalho remoto, distanciamento social.
    - **Impactos econômicos**: Renda familiar, acesso ao auxílio emergencial.

    Cada gráfico e análise foi elaborado para fornecer uma visão clara sobre como a pandemia afetou diversos aspectos da sociedade brasileira, oferecendo insights que podem ajudar no planejamento de futuras políticas públicas.

    ### Instruções de Navegação:
    - No menu à esquerda, você pode explorar cada um dos temas principais (**Sintomas**, **Comportamento** e **Economia**), onde encontrará gráficos detalhados e as análises correspondentes.
    """)

# Menu lateral principal com submenus
menu_principal = st.sidebar.selectbox("Selecione a categoria", ["Página Inicial", "Sintomas", "Comportamento", "Economia", "Recomendações"])

# Página Inicial
if menu_principal == "Página Inicial":
    pagina_inicial()

# Menus relacionados a Sintomas
elif menu_principal == "Sintomas":
    submenu_sintomas = st.sidebar.selectbox("Selecione a análise de sintomas", [
        "Sintomas por Idade", "Sintomas por Sexo","Sintomas e Uso de Máscara", "Sintomas por Região", "Sintomas e Planos de Saude"
    ])
    
    if submenu_sintomas == "Sintomas por Idade":
        sintomas_por_idade()
    elif submenu_sintomas == "Sintomas por Sexo":
        sintomas_por_sexo()
    elif submenu_sintomas == "Sintomas e Uso de Máscara":
        sintomas_uso_mascara()
    elif submenu_sintomas == "Sintomas por Região":
        sintomas_por_regiao()
    elif submenu_sintomas == "Sintomas e Planos de Saude":
        sintomas_por_plano_saude()

# Menus relacionados a Comportamento
elif menu_principal == "Comportamento":
    submenu_comportamento = st.sidebar.selectbox("Selecione a análise de comportamento", [
        "Comportamento Trabalho", "Distanciamento Social"
    ])
    
    if submenu_comportamento == "Comportamento Trabalho":
        comportamento_trabalho()
    elif submenu_comportamento == "Distanciamento Social":
        comportamento_distanciamento_social()

# Menus relacionados a Economia
elif menu_principal == "Economia":
    submenu_economia = st.sidebar.selectbox("Selecione a análise econômica", [
        "Renda Familiar", "Auxilio Emergenial"
    ])
    
    if submenu_economia == "Renda Familiar":
        economia_renda_familiar()
    elif submenu_economia == "Auxilio Emergenial":
        economia_auxilio_emergencial()

elif menu_principal == "Recomendações":
    pagina_recomendacoes()