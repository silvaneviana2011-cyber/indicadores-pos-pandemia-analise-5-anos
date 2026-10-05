# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:39:54 2026

@author: silva
"""

# ============================================================
# PROJETO COVID-19 EM PORTUGAL
# 04 — VERIFICAÇÃO DOS DADOS TRATADOS
# ============================================================

import pandas as pd

print("=" * 60)
print("PROJETO COVID-19 EM PORTUGAL")
print("VERIFICAÇÃO DOS DADOS TRATADOS")
print("=" * 60)


# ============================================================
# 1. CARREGAR DADOS TRATADOS
# ============================================================

print("\nA carregar dados tratados...")

excesso = pd.read_csv(
    "03_dados_tratados/excesso_mortalidade_pt.csv"
)

vacinacao = pd.read_csv(
    "03_dados_tratados/vacinacao_pt.csv"
)

mortes_covid = pd.read_csv(
    "03_dados_tratados/mortes_covid_pt_semanal.csv"
)


# ============================================================
# 2. DIMENSÕES
# ============================================================

print("\n" + "=" * 60)
print("DIMENSÕES")
print("=" * 60)

print("\nExcesso de mortalidade:")
print(excesso.shape)

print("\nVacinação:")
print(vacinacao.shape)

print("\nMortes COVID:")
print(mortes_covid.shape)


# ============================================================
# 3. COLUNAS
# ============================================================

print("\n" + "=" * 60)
print("COLUNAS")
print("=" * 60)

print("\nExcesso:")
print(excesso.columns.tolist())

print("\nVacinação:")
print(vacinacao.columns.tolist())

print("\nMortes COVID:")
print(mortes_covid.columns.tolist())


# ============================================================
# 4. PERÍODOS
# ============================================================

print("\n" + "=" * 60)
print("PERÍODOS")
print("=" * 60)

print("\nExcesso de mortalidade:")
print(
    excesso["Semana"].min(),
    "até",
    excesso["Semana"].max()
)

print("\nVacinação:")
print(
    vacinacao["Day"].min(),
    "até",
    vacinacao["Day"].max()
)

print("\nMortes COVID:")
print(
    mortes_covid["Semana"].min(),
    "até",
    mortes_covid["Semana"].max()
)


# ============================================================
# 5. AMOSTRA DOS DADOS
# ============================================================

print("\n" + "=" * 60)
print("PRIMEIRAS LINHAS")
print("=" * 60)

print("\nExcesso:")
print(excesso.head())

print("\nVacinação:")
print(vacinacao.head())

print("\nMortes COVID:")
print(mortes_covid.head())


# ============================================================
# FIM
# ============================================================

print("\n" + "=" * 60)
print("VERIFICAÇÃO CONCLUÍDA")
print("=" * 60) 

#%% Padronizar as datas

# ============================================================
# BLOCO 2 — PADRONIZAÇÃO DAS DATAS
# ============================================================

print("\n" + "=" * 60)
print("PADRONIZAÇÃO DAS DATAS")
print("=" * 60)


# ------------------------------------------------------------
# 1. EXCESSO DE MORTALIDADE
# ------------------------------------------------------------

excesso["Semana"] = excesso["Semana"].astype(str)

# Converter semana ISO (ex.: 2020-W01) para uma data
excesso["data_semana"] = pd.to_datetime(
    excesso["Semana"] + "-1",
    format="%G-W%V-%u"
)


# ------------------------------------------------------------
# 2. MORTES COVID
# ------------------------------------------------------------

mortes_covid["Semana"] = mortes_covid["Semana"].astype(str)

# Utilizar o primeiro dia da semana
mortes_covid["data_semana"] = pd.to_datetime(
    mortes_covid["Semana"].str.split("/").str[0]
)


# ------------------------------------------------------------
# 3. VACINAÇÃO
# ------------------------------------------------------------

vacinacao["Day"] = pd.to_datetime(
    vacinacao["Day"]
)

# A vacinação já possui uma data semanal
vacinacao["data_semana"] = vacinacao["Day"]


# ============================================================
# VERIFICAR
# ============================================================

print("\nExcesso de mortalidade:")
print(
    excesso[
        ["Semana", "data_semana"]
    ].head()
)

print("\nMortes COVID:")
print(
    mortes_covid[
        ["Semana", "data_semana"]
    ].head()
)

print("\nVacinação:")
print(
    vacinacao[
        ["Day", "data_semana"]
    ].head()
)

print("\nDatas padronizadas com sucesso.")

# ============================================================
# BLOCO 3 — JUNTAR MORTALIDADE E MORTES COVID
# ============================================================

print("\n" + "=" * 60)
print("JUNÇÃO DOS DADOS DE MORTALIDADE")
print("=" * 60)

# Selecionar apenas as variáveis necessárias
excesso_comparacao = excesso[
    [
        "data_semana",
        "excesso_cumulativo_por_milhao"
    ]
].copy()

mortes_comparacao = mortes_covid[
    [
        "data_semana",
        "mortes_covid"
    ]
].copy()


# ------------------------------------------------------------
# Fazer a junção
# ------------------------------------------------------------

mortalidade = pd.merge(
    excesso_comparacao,
    mortes_comparacao,
    on="data_semana",
    how="inner"
)


# Ordenar cronologicamente
mortalidade = mortalidade.sort_values(
    "data_semana"
).reset_index(drop=True)


# ============================================================
# VERIFICAR RESULTADO
# ============================================================

print("\nDimensões da tabela final:")
print(mortalidade.shape)

print("\nPrimeiras linhas:")
print(mortalidade.head(10))

print("\nÚltimas linhas:")
print(mortalidade.tail(10))

print("\nPeríodo:")
print(mortalidade["data_semana"].min())
print("até")
print(mortalidade["data_semana"].max())

print("\nTabela de mortalidade criada com sucesso.") 

#%% Incorporar dados vacinação 

# ============================================================
# BLOCO 4 — INCORPORAR A VACINAÇÃO
# ============================================================

print("\n" + "=" * 60)
print("INCORPORAÇÃO DA VACINAÇÃO")
print("=" * 60)

# Preparar vacinação
vacinacao_comparacao = vacinacao[
    [
        "data_semana",
        "cobertura_vacinal"
    ]
].copy()

# Ordenar as duas tabelas pela data
mortalidade = mortalidade.sort_values(
    "data_semana"
)

vacinacao_comparacao = vacinacao_comparacao.sort_values(
    "data_semana"
)

# Associar a cada semana a última cobertura vacinal
# disponível até essa data
dataset_final = pd.merge_asof(
    mortalidade,
    vacinacao_comparacao,
    on="data_semana",
    direction="backward"
)

# ============================================================
# VERIFICAR RESULTADO
# ============================================================

print("\nDimensões:")
print(dataset_final.shape)

print("\nPrimeiras linhas:")
print(dataset_final.head(10))

print("\nLinhas próximas do início da vacinação:")
print(
    dataset_final[
        (dataset_final["data_semana"] >= "2020-12-01") &
        (dataset_final["data_semana"] <= "2021-03-31")
    ].head(20)
)

print("\nÚltimas linhas:")
print(dataset_final.tail(10))

print("\nColunas:")
print(dataset_final.columns.tolist())

print("\nVacinação incorporada com sucesso.")

#%% Guardar o dataset 

# ============================================================
# BLOCO 5 — GUARDAR O DATASET FINAL
# ============================================================

print("\n" + "=" * 60)
print("GUARDAR DATASET FINAL")
print("=" * 60)

dataset_final.to_csv(
    "03_dados_tratados/dataset_final_covid_portugal.csv",
    index=False
)

print("\n✓ Dataset final guardado.")

print("\nFicheiro:")
print(
    "03_dados_tratados/dataset_final_covid_portugal.csv"
)

print("\nDimensões:")
print(dataset_final.shape)

print("\nColunas:")
print(dataset_final.columns.tolist())

print("\n" + "=" * 60)
print("DATASET FINAL GUARDADO COM SUCESSO")
print("=" * 60)