# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 20:56:41 2026

@author: silva
"""

# ============================================================
# PROJETO COVID-19 EM PORTUGAL
# 06 — EXPLORAÇÃO DOS ÓBITOS POR CAUSAS DE MORTE
# ============================================================

import pandas as pd

print("=" * 60)
print("ÓBITOS POR CAUSAS DE MORTE — INE")
print("=" * 60)


# ============================================================
# BLOCO 1 — CARREGAR FICHEIRO DO INE
# ============================================================

print("\nA carregar ficheiro do INE...")

ficheiro = (
    "02_dados_originais/"
    "dados_mortes_causas_portugal.xls"
)

df_obitos = pd.read_excel(
    ficheiro,
    engine="xlrd"
)

print("\nFicheiro carregado com sucesso.")


# ============================================================
# VERIFICAR ESTRUTURA
# ============================================================

print("\nDimensões:")
print(df_obitos.shape)

print("\nNomes das colunas:")
print(df_obitos.columns.tolist())

print("\nPrimeiras linhas:")
print(df_obitos.head(10))


# ============================================================
# FIM
# ============================================================

print("\n" + "=" * 60)
print("EXPLORAÇÃO DO FICHEIRO CONCLUÍDA")
print("=" * 60)

print("\n" + "="*60)
print("CONTEÚDO DAS PRIMEIRAS 26 LINHAS")
print("="*60)

pd.set_option("display.max_columns", 10)
pd.set_option("display.width", 150)

print(df_obitos.iloc[:, :10].to_string())

print("\n" + "="*60)
print("LINHAS 0 A 20")
print("="*60)

for i in range(17):
    print(f"\n--- LINHA {i} ---")
    print(df_obitos.iloc[i].dropna().tolist())
    
print("\n--- CABEÇALHO ---")
print(df_obitos.iloc[13].dropna().tolist())

#%% Ainda a identificar as linhas

for i in range(9, 17):
    print(f"\n--- LINHA {i} ---")
    print(df_obitos.iloc[i].dropna().tolist()[:15]) 

#%% Bloco dois

# ----------------------------------------------------------
# BLOCO 2 — ORGANIZAÇÃO DOS DADOS
# ----------------------------------------------------------

causas = df_obitos.iloc[10].dropna().tolist()

dados = df_obitos.iloc[12:15, :len(causas)].copy()

dados.columns = causas

dados.insert(0, "Ano", df_obitos.iloc[12:15, 0].values)

print("\n" + "="*60)
print("DADOS ORGANIZADOS")
print("="*60)

print("\nDimensões:")
print(dados.shape)

print("\nColunas:")
print(dados.columns.tolist())

print("\nPrimeiras linhas:")
print(dados.iloc[:, :10]) 

print("\n" + "="*60)
print("ESTRUTURA DA TABELA")
print("="*60)

for i in range(8, 15):
    print(f"\nLINHA {i}:")
    print(df_obitos.iloc[i, :8].tolist())
    
print(df_obitos.iloc[12, :8].tolist())

#%% Ainda identificando valores

print("\n" + "="*60)
print("DOENÇAS CEREBROVASCULARES")
print("="*60)

for coluna in range(df_obitos.shape[1]):
    valor = df_obitos.iloc[10, coluna]

    if valor == "Doenças cerebrovasculares":
        print("Coluna encontrada:", coluna)
        print("2024:", df_obitos.iloc[12, coluna])
        print("2023:", df_obitos.iloc[13, coluna])
        print("2022:", df_obitos.iloc[14, coluna])
#%% A identificar os blocos

print("\n" + "="*60)
print("ESTRUTURA DOS BLOCOS")
print("="*60)

for i in range(5, 12):
    print(f"\nLINHA {i}:")
    print(df_obitos.iloc[i, :10].tolist())

#%% A entender os Cabeçalhos

print("\n" + "="*60)
print("CABECALHOS DOS BLOCOS")
print("="*60)

for i in range(0, 10):
    valores = df_obitos.iloc[i].dropna().tolist()
    print(f"\nLINHA {i}:")
    print(valores[:20])
    
#%% A tirar repetidos e a buscar valores limpos

# ----------------------------------------------------------
# BLOCO 3 — DADOS TOTAIS (HM)
# ----------------------------------------------------------

# Primeira coluna de cada causa no bloco HM
colunas_causas = range(3, 128, 2)

causas_hm = df_obitos.iloc[10, list(colunas_causas)].tolist()

valores_hm = df_obitos.iloc[12:15, list(colunas_causas)].copy()

valores_hm.columns = causas_hm
valores_hm.insert(
    0,
    "Ano",
    df_obitos.iloc[12:15, 0].values
)

print("\n" + "="*60)
print("DADOS TOTAIS — HM")
print("="*60)

print("\nDimensões:")
print(valores_hm.shape)

print("\nTodas as causas:")
print(
    valores_hm[
        ["Ano", "Todas as causas de morte",
         "Doenças do aparelho circulatório",
         "Doenças cerebrovasculares"]
    ]
)

#%% Guardar dados limpos

# ----------------------------------------------------------
# BLOCO 4 — GUARDAR DADOS INE
# ----------------------------------------------------------

ficheiro_saida = (
    "03_dados_tratados/"
    "obitos_causas_ine_2022_2024.csv"
)

valores_hm.to_csv(
    ficheiro_saida,
    index=False,
    encoding="utf-8-sig"
)

print("\nFicheiro guardado com sucesso:")
print(ficheiro_saida)