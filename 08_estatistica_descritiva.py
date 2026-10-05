# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 09:18:52 2026

@author: silva
"""

# ============================================================
# BLOCO 1 — IMPORTAÇÃO E LEITURA DOS DADOS
# Estatística Descritiva — Portugal, 2020–2024
# ============================================================

import pandas as pd

# ------------------------------------------------------------
# Ler o dataset PORDATA já tratado
# ------------------------------------------------------------

df_estatistica = pd.read_csv(
    "03_dados_tratados/obitos_pordata_2020_2024.csv"
)

# ------------------------------------------------------------
# Verificar a estrutura dos dados
# ------------------------------------------------------------

print("\n============================================================")
print("DATASET PORDATA — ESTATÍSTICA DESCRITIVA")
print("============================================================")

print("\nDimensões do dataset:")
print(df_estatistica.shape)

print("\nColunas:")
print(df_estatistica.columns.tolist())

print("\nPrimeiras linhas:")
print(df_estatistica.head())

#%%  Variáveis numéricas

# ============================================================
# BLOCO 2 — SELEÇÃO DAS VARIÁVEIS NUMÉRICAS
# ============================================================

# ------------------------------------------------------------
# Selecionar apenas as causas de morte
# ------------------------------------------------------------

dados_causas = df_estatistica.iloc[:, 1:]

# ------------------------------------------------------------
# Garantir que todas as causas são numéricas
# ------------------------------------------------------------

dados_causas = dados_causas.apply(
    pd.to_numeric,
    errors="coerce"
)

# ------------------------------------------------------------
# Verificar os tipos de dados
# ------------------------------------------------------------

print("\n============================================================")
print("VARIÁVEIS UTILIZADAS NA ANÁLISE ESTATÍSTICA")
print("============================================================")

print("\nTipos de dados:")
print(dados_causas.dtypes)

print("\nDimensões:")
print(dados_causas.shape)

#%% Estatística Descritiva

# ============================================================
# BLOCO 3 — ESTATÍSTICA DESCRITIVA + QUARTIS
# Portugal, 2020–2024
# ============================================================

# ------------------------------------------------------------
# Calcular as principais medidas estatísticas
# ------------------------------------------------------------

estatistica_basica = pd.DataFrame({
    "Média": dados_causas.mean(),
    "1.º Quartil (Q1)": dados_causas.quantile(0.25),
    "Mediana (Q2)": dados_causas.median(),
    "3.º Quartil (Q3)": dados_causas.quantile(0.75),
    "Mínimo": dados_causas.min(),
    "Máximo": dados_causas.max()
})

# ------------------------------------------------------------
# Calcular o intervalo interquartil (IQR)
# ------------------------------------------------------------

estatistica_basica["Intervalo interquartil (IQR)"] = (
    estatistica_basica["3.º Quartil (Q3)"]
    - estatistica_basica["1.º Quartil (Q1)"]
)

# ------------------------------------------------------------
# Arredondar os valores
# ------------------------------------------------------------

estatistica_basica = estatistica_basica.round(1)

# ------------------------------------------------------------
# Apresentar os resultados
# ------------------------------------------------------------

print("\n============================================================")
print("ESTATÍSTICA DESCRITIVA — QUARTIS")
print("Portugal, 2020–2024")
print("============================================================\n")

print(
    estatistica_basica.to_string()
) 

#%% Coeficiente de variação

# ============================================================
# BLOCO 4 — COEFICIENTE DE VARIAÇÃO
# Portugal, 2020–2024
# ============================================================

# ------------------------------------------------------------
# Calcular média e desvio-padrão
# ------------------------------------------------------------

media = dados_causas.mean()

desvio_padrao = dados_causas.std()

# ------------------------------------------------------------
# Calcular o coeficiente de variação
# ------------------------------------------------------------

coef_variacao = (
    desvio_padrao / media
) * 100

# ------------------------------------------------------------
# Criar tabela
# ------------------------------------------------------------

df_cv = pd.DataFrame({
    "Média": media,
    "Desvio-padrão": desvio_padrao,
    "Coeficiente de variação (%)": coef_variacao
})

# ------------------------------------------------------------
# Ordenar do maior para o menor CV
# ------------------------------------------------------------

df_cv = df_cv.sort_values(
    "Coeficiente de variação (%)",
    ascending=False
)

# ------------------------------------------------------------
# Arredondar
# ------------------------------------------------------------

df_cv = df_cv.round(2)

# ------------------------------------------------------------
# Apresentar resultados
# ------------------------------------------------------------

print("\n============================================================")
print("COEFICIENTE DE VARIAÇÃO")
print("Portugal, 2020–2024")
print("============================================================\n")

print(
    df_cv.to_string()
)


#%% Amplitude e variação max e min

# ============================================================
# BLOCO 5 — AMPLITUDE E VARIAÇÃO ABSOLUTA
# Portugal, 2020–2024
# ============================================================

maximo = dados_causas.max()
minimo = dados_causas.min()

amplitude = maximo - minimo

df_amplitude = pd.DataFrame({
    "Mínimo": minimo,
    "Máximo": maximo,
    "Amplitude": amplitude
})

df_amplitude = df_amplitude.sort_values(
    "Amplitude",
    ascending=False
)

print("\n============================================================")
print("AMPLITUDE DOS ÓBITOS")
print("Portugal, 2020–2024")
print("============================================================\n")

print(
    df_amplitude.to_string()
)

#%% Variação por cada causa

# ============================================================
# BLOCO 6 — VARIAÇÃO PERCENTUAL 2020 → 2024
# Portugal, 2020–2024
# ============================================================

valor_2020 = dados_causas.iloc[0]
valor_2024 = dados_causas.iloc[-1]

variacao_percentual = (
    (valor_2024 - valor_2020) / valor_2020
) * 100

df_variacao = pd.DataFrame({
    "Óbitos 2020": valor_2020,
    "Óbitos 2024": valor_2024,
    "Variação absoluta": valor_2024 - valor_2020,
    "Variação percentual (%)": variacao_percentual
})

df_variacao = df_variacao.sort_values(
    "Variação percentual (%)",
    ascending=False
)

df_variacao = df_variacao.round(2)

print("\n============================================================")
print("VARIAÇÃO PERCENTUAL DOS ÓBITOS")
print("2020 → 2024")
print("============================================================\n")

print(
    df_variacao.to_string()
)

#%% Análise da dispersão


# ============================================================
# BLOCO 7 — DESVIO-PADRÃO E DISPERSÃO
# Portugal, 2020–2024
# ============================================================

media = dados_causas.mean()
desvio_padrao = dados_causas.std()

df_dispersao = pd.DataFrame({
    "Média": media,
    "Desvio-padrão": desvio_padrao
})

df_dispersao = df_dispersao.sort_values(
    "Desvio-padrão",
    ascending=False
)

df_dispersao = df_dispersao.round(2)

print("\n============================================================")
print("DESVIO-PADRÃO E DISPERSÃO")
print("Portugal, 2020–2024")
print("============================================================\n")

print(
    df_dispersao.to_string()
)
