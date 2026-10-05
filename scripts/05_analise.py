# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:57:04 2026

@author: silva
"""

# ============================================================
# PROJETO COVID-19 EM PORTUGAL
# 05 — ANÁLISE EXPLORATÓRIA
# ============================================================

import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

print("=" * 60)
print("PROJETO COVID-19 EM PORTUGAL")
print("ANÁLISE EXPLORATÓRIA")
print("=" * 60)


# ============================================================
# BLOCO 1 — CARREGAR DATASET FINAL
# ============================================================

dataset = pd.read_csv(
    "03_dados_tratados/dataset_final_covid_portugal.csv"
)

# Converter a data
dataset["data_semana"] = pd.to_datetime(
    dataset["data_semana"]
)

# Ordenar cronologicamente
dataset = dataset.sort_values(
    "data_semana"
).reset_index(drop=True)


print("\nDataset carregado com sucesso.")

print("\nDimensões:")
print(dataset.shape)

print("\nColunas:")
print(dataset.columns.tolist())

print("\nPeríodo:")
print(dataset["data_semana"].min())
print("até")
print(dataset["data_semana"].max())


# ============================================================
# BLOCO 2 — PRIMEIRA VISUALIZAÇÃO
# EXCESSO DE MORTALIDADE
# ============================================================

fig = px.line(
    dataset,
    x="data_semana",
    y="excesso_cumulativo_por_milhao",
    title="Evolução do excesso cumulativo de mortalidade — Portugal",
    labels={
        "data_semana": "Data",
        "excesso_cumulativo_por_milhao":
            "Excesso cumulativo de mortes por milhão"
    }
)

fig.show() 

print("GRÁFICO 1 — EXCESSO DE MORTALIDADE") 

#%% Criar gráfico

# ============================================================
# BLOCO 3 — EVOLUÇÃO DAS MORTES COVID-19
# ============================================================

print("\nA criar gráfico das mortes COVID-19...")

fig = px.line(
    dataset,
    x="data_semana",
    y="mortes_covid",
    title="Evolução semanal das mortes por COVID-19 — Portugal",
    labels={
        "data_semana": "Data",
        "mortes_covid": "Mortes COVID-19 por semana"
    },
    color_discrete_sequence=["#12DADF"]
)



fig.show(renderer="browser")

print("Gráfico apresentado.")

print("GRÁFICO 2 — MORTES COVID-19")

#%% Evolução da Cobertura Vacinal

# ============================================================
# BLOCO 4 — EVOLUÇÃO DA COBERTURA VACINAL
# ============================================================

print("\nA criar gráfico da cobertura vacinal...")

fig = px.line(
    dataset,
    x="data_semana",
    y="cobertura_vacinal",
    title="Evolução da cobertura vacinal — Portugal",
    labels={
        "data_semana": "Data",
        "cobertura_vacinal": "Cobertura vacinal (%)"
    },
    color_discrete_sequence=["#12DADF"]
)

fig.update_yaxes(
    range=[0, 100]
)

# Linha indicando a cobertura vacinal máxima
valor_maximo = dataset["cobertura_vacinal"].max()

fig.add_vline(
    x=dataset.loc[
        dataset["cobertura_vacinal"].idxmax(),
        "data_semana"
    ],
    line_color="#DFAB39",
    line_width=2,
    line_dash="dash"
) 


fig.show(renderer="browser")

print("GRÁFICO 3 — COBERTURA VACINAL") 



#%% Matriz de correlação

# ============================================================
# BLOCO 5 — MATRIZ DE CORRELAÇÃO
# ============================================================

print("\nA calcular matriz de correlação...")

# Selecionar apenas as variáveis numéricas
variaveis_numericas = dataset.select_dtypes(
    include="number"
)

# Calcular correlação
correlacao = variaveis_numericas.corr()

print("\nMATRIZ DE CORRELAÇÃO:")
print(correlacao.round(2))


# Criar heatmap
plt.figure(figsize=(12, 8))

sns.heatmap(
    correlacao,
    annot=True,
    fmt=".2f",
    cmap="PuBuGn",
    center=0,
    linewidths=0.5
)

plt.title(
    "Matriz de correlação dos indicadores de saúde"
)

plt.tight_layout()
plt.show()

print("\nGRÁFICO 4 — MATRIZ DE CORRELAÇÃO") 

#%% Análise da relação entre vacinação e mortes gráfico de dispersão

# ============================================================
# BLOCO 6 — COBERTURA VACINAL VS MORTES COVID-19
# ============================================================

print("\nA analisar a relação entre cobertura vacinal e mortes COVID-19...")

fig = px.scatter(
    dataset,
    x="cobertura_vacinal",
    y="mortes_covid",
    title="Relação entre cobertura vacinal e mortes por COVID-19",
    labels={
        "cobertura_vacinal": "Cobertura vacinal (%)",
        "mortes_covid": "Mortes COVID-19 por semana"
    },
    trendline="ols"
)

fig.show(renderer="browser")

print("GRÁFICO 5 — COBERTURA VACINAL VS MORTES COVID-19")

#%% Cobertura vacinal vs excesso de mortalidade

# ============================================================
# BLOCO 7 — COBERTURA VACINAL VS. EXCESSO CUMULATIVO
# ============================================================

print("\nA analisar a relação entre cobertura vacinal e excesso cumulativo de mortalidade...")

fig = px.scatter(
    dataset,
    x="cobertura_vacinal",
    y="excesso_cumulativo_por_milhao",
    title="Relação entre cobertura vacinal e excesso cumulativo de mortalidade",
    labels={
        "cobertura_vacinal": "Cobertura vacinal (%)",
        "excesso_cumulativo_por_milhao":
            "Excesso cumulativo de mortalidade por milhão"
    },
    trendline="ols"
)

fig.show(renderer="browser")

print("GRÁFICO 6 — COBERTURA VACINAL VS. EXCESSO CUMULATIVO") 

#%% Evolução do excesso cumulativo

# ============================================================
# BLOCO 8 — EVOLUÇÃO DO EXCESSO CUMULATIVO
# ============================================================

print("\nA analisar a evolução do excesso cumulativo...")

# Identificar o valor máximo
indice_max = dataset["excesso_cumulativo_por_milhao"].idxmax()

valor_max = dataset.loc[
    indice_max,
    "excesso_cumulativo_por_milhao"
]

data_max = dataset.loc[
    indice_max,
    "data_semana"
]

print("\nMAIOR VALOR DE EXCESSO CUMULATIVO:")
print(f"Valor: {valor_max:.2f} por milhão")
print(f"Data: {data_max.strftime('%d-%m-%Y')}")


# Criar gráfico
fig = px.line(
    dataset,
    x="data_semana",
    y="excesso_cumulativo_por_milhao",
    title="Evolução do excesso cumulativo de mortalidade — Portugal",
    labels={
        "data_semana": "Data",
        "excesso_cumulativo_por_milhao":
            "Excesso cumulativo de mortalidade por milhão"
    }
)

# Destacar o ponto máximo
fig.add_scatter(
    x=[data_max],
    y=[valor_max],
    mode="markers+text",
    text=[f"Máximo: {valor_max:.0f}"],
    textposition="top center",
    name="Valor máximo"
)

fig.show(renderer="browser")

print("GRÁFICO 7 — EVOLUÇÃO DO EXCESSO CUMULATIVO") 

#%% Análise integrada por ano

# ============================================================
# BLOCO 9 — ANÁLISE INTEGRADA DOS INDICADORES
# ============================================================

print("\nA realizar análise integrada dos indicadores...")

# Criar coluna com o ano
dataset["ano"] = dataset["data_semana"].dt.year


# ------------------------------------------------------------
# RESUMO ANUAL
# ------------------------------------------------------------

resumo_anual = dataset.groupby("ano").agg(
    mortes_covid_total=("mortes_covid", "sum"),
    cobertura_vacinal_max=("cobertura_vacinal", "max"),
    excesso_cumulativo_final=(
        "excesso_cumulativo_por_milhao",
        "last"
    )
).reset_index()


print("\nRESUMO ANUAL DOS INDICADORES:")
print(resumo_anual.round(2).to_string(index=False))


# ------------------------------------------------------------
# IDENTIFICAR ANOS COM MAIOR MORTALIDADE COVID-19
# ------------------------------------------------------------

ano_maior_mortalidade = resumo_anual.loc[
    resumo_anual["mortes_covid_total"].idxmax(),
    "ano"
]

maior_mortalidade = resumo_anual.loc[
    resumo_anual["mortes_covid_total"].idxmax(),
    "mortes_covid_total"
]

print("\nANO COM MAIOR NÚMERO TOTAL DE MORTES COVID-19:")
print(f"Ano: {ano_maior_mortalidade}")
print(f"Mortes: {maior_mortalidade:.0f}")


# ------------------------------------------------------------
# ANO COM MAIOR COBERTURA VACINAL
# ------------------------------------------------------------

ano_maior_vacinacao = resumo_anual.loc[
    resumo_anual["cobertura_vacinal_max"].idxmax(),
    "ano"
]

maior_vacinacao = resumo_anual.loc[
    resumo_anual["cobertura_vacinal_max"].idxmax(),
    "cobertura_vacinal_max"
]

print("\nMAIOR COBERTURA VACINAL OBSERVADA:")
print(f"Ano: {ano_maior_vacinacao}")
print(f"Cobertura: {maior_vacinacao:.2f}%")


# ------------------------------------------------------------
# GRÁFICO — MORTES COVID-19 POR ANO
# ------------------------------------------------------------

fig = px.bar(
    resumo_anual,
    x="ano",
    y="mortes_covid_total",
    title="Total anual de mortes por COVID-19 — Portugal",
    labels={
        "ano": "Ano",
        "mortes_covid_total": "Total de mortes COVID-19"
    }
)

fig.show(renderer="browser")

print("\nGRÁFICO 8 — MORTES COVID-19 POR ANO")


# ------------------------------------------------------------
# GRÁFICO — COBERTURA VACINAL POR ANO
# ------------------------------------------------------------

fig = px.line(
    resumo_anual,
    x="ano",
    y="cobertura_vacinal_max",
    markers=True,
    title="Evolução da cobertura vacinal máxima por ano",
    labels={
        "ano": "Ano",
        "cobertura_vacinal_max": "Cobertura vacinal máxima (%)"
    }
)

fig.update_yaxes(range=[0, 100])

fig.show(renderer="browser")

print("GRÁFICO 9 — COBERTURA VACINAL")


# ------------------------------------------------------------
# GRÁFICO — EXCESSO CUMULATIVO NO FINAL DE CADA ANO
# ------------------------------------------------------------

fig = px.line(
    resumo_anual,
    x="ano",
    y="excesso_cumulativo_final",
    markers=True,
    title="Evolução anual do excesso cumulativo de mortalidade",
    labels={
        "ano": "Ano",
        "excesso_cumulativo_final":
            "Excesso cumulativo de mortalidade por milhão"
    }
)

fig.show(renderer="browser")

print("GRÁFICO 10 — EXCESSO CUMULATIVO")