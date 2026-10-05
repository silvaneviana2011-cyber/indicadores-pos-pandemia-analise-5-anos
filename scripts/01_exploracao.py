# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:38:45 2026

@author: silva
"""

# ============================================================
# PROJETO COVID-19 EM PORTUGAL
# BLOCO 1 — EXPLORAÇÃO INICIAL DOS DATASETS
# ============================================================

import pandas as pd
import os


print("=" * 60)
print("PROJETO COVID-19 EM PORTUGAL")
print("EXPLORAÇÃO INICIAL DOS DATASETS")
print("=" * 60)


# ============================================================
# 1. VERIFICAR A PASTA DE TRABALHO
# ============================================================

print("\nPasta de trabalho atual:")
print(os.getcwd())

print("\nFicheiros encontrados:")
print(os.listdir())


# ============================================================
# 2. CARREGAR OS DATASETS ORIGINAIS
# ============================================================

df_excesso = pd.read_csv(
    "02_dados_originais/excesso_mortalidade.csv"
)

df_vacinacao = pd.read_csv(
    "02_dados_originais/vacinacao.csv"
)

df_mortes = pd.read_csv(
    "02_dados_originais/mortes_covid.csv"
)


# ============================================================
# 3. EXCESSO DE MORTALIDADE
# ============================================================

print("\n" + "=" * 60)
print("DATASET — EXCESSO DE MORTALIDADE")
print("=" * 60)

print("Dimensões:", df_excesso.shape)

print("\nColunas:")
print(df_excesso.columns.tolist())

print("\nPrimeiras linhas:")
print(df_excesso.head())


# ============================================================
# 4. VACINAÇÃO
# ============================================================

print("\n" + "=" * 60)
print("DATASET — VACINAÇÃO")
print("=" * 60)

print("Dimensões:", df_vacinacao.shape)

print("\nColunas:")
print(df_vacinacao.columns.tolist())

print("\nPrimeiras linhas:")
print(df_vacinacao.head())


# ============================================================
# 5. MORTES COVID-19
# ============================================================

print("\n" + "=" * 60)
print("DATASET — MORTES COVID-19")
print("=" * 60)

print("Dimensões:", df_mortes.shape)

print("\nColunas:")
print(df_mortes.columns.tolist())

print("\nPrimeiras linhas:")
print(df_mortes.head())


# ============================================================
# FIM DA EXPLORAÇÃO INICIAL
# ============================================================

print("\n" + "=" * 60)
print("EXPLORAÇÃO INICIAL CONCLUÍDA")
print("=" * 60) 

#%% Diagnóstico dos Dados Portugal

# ============================================================
# BLOCO 2 — DIAGNÓSTICO DOS DADOS DE PORTUGAL
# ============================================================

print("\n" + "=" * 60)
print("DIAGNÓSTICO DOS DADOS DE PORTUGAL")
print("=" * 60)


# ============================================================
# 2.1 — EXCESSO DE MORTALIDADE
# ============================================================

portugal_excesso = df_excesso[
    df_excesso["Entity"] == "Portugal"
].copy()

print("\nEXCESSO DE MORTALIDADE — PORTUGAL")
print("Linhas:", len(portugal_excesso))

print("\nPeríodo:")
print(
    portugal_excesso["Week"].min(),
    "até",
    portugal_excesso["Week"].max()
)

print("\nPrimeiras linhas:")
print(portugal_excesso.head())

print("\nÚltimas linhas:")
print(portugal_excesso.tail())


# ============================================================
# 2.2 — VACINAÇÃO
# ============================================================

portugal_vacinacao = df_vacinacao[
    df_vacinacao["Entity"] == "Portugal"
].copy()

portugal_vacinacao["Day"] = pd.to_datetime(
    portugal_vacinacao["Day"]
)

print("\nVACINAÇÃO — PORTUGAL")
print("Linhas:", len(portugal_vacinacao))

print("\nPeríodo:")
print(
    portugal_vacinacao["Day"].min(),
    "até",
    portugal_vacinacao["Day"].max()
)

print("\nPrimeiras linhas:")
print(portugal_vacinacao.head())

print("\nÚltimas linhas:")
print(portugal_vacinacao.tail())


# ============================================================
# 2.3 — MORTES COVID-19
# ============================================================

portugal_mortes = df_mortes[
    df_mortes["Entity"] == "Portugal"
].copy()

portugal_mortes["Day"] = pd.to_datetime(
    portugal_mortes["Day"]
)

print("\nMORTES COVID-19 — PORTUGAL")
print("Linhas:", len(portugal_mortes))

print("\nPeríodo:")
print(
    portugal_mortes["Day"].min(),
    "até",
    portugal_mortes["Day"].max()
)

print("\nPrimeiras linhas:")
print(portugal_mortes.head())

print("\nÚltimas linhas:")
print(portugal_mortes.tail()) 

