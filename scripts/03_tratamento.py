# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:55:24 2026

@author: silva
"""

# ============================================================
# PROJETO COVID-19 EM PORTUGAL
# 03 — TRATAMENTO DOS DADOS
# ============================================================

import pandas as pd
import os


print("=" * 60)
print("PROJETO COVID-19 EM PORTUGAL")
print("TRATAMENTO DOS DADOS")
print("=" * 60)


# ============================================================
# 1. EXCESSO DE MORTALIDADE
# ============================================================

print("\nA carregar excesso de mortalidade...")

df_excesso = pd.read_csv(
    "02_dados_originais/excesso_mortalidade.csv"
)

excesso_pt = df_excesso[
    df_excesso["Entity"] == "Portugal"
].copy()

print("Excesso de mortalidade — Portugal:", excesso_pt.shape)

del df_excesso


# ============================================================
# 2. VACINAÇÃO
# ============================================================

print("\nA carregar vacinação...")

df_vacinacao = pd.read_csv(
    "02_dados_originais/vacinacao.csv"
)

vacinacao_pt = df_vacinacao[
    df_vacinacao["Entity"] == "Portugal"
].copy()

print("Vacinação — Portugal:", vacinacao_pt.shape)

del df_vacinacao


# ============================================================
# 3. MORTES COVID-19
# ============================================================

print("\nA carregar mortes COVID-19...")

mortes_pt_lista = []

for bloco in pd.read_csv(
    "02_dados_originais/mortes_covid.csv",
    chunksize=50000
):
    
    portugal = bloco[
        bloco["Entity"] == "Portugal"
    ].copy()
    
    if not portugal.empty:
        mortes_pt_lista.append(portugal)


mortes_pt = pd.concat(
    mortes_pt_lista,
    ignore_index=True
)

print("Mortes COVID — Portugal:", mortes_pt.shape)


# ============================================================
# 4. CONVERTER DATAS
# ============================================================

vacinacao_pt["Day"] = pd.to_datetime(
    vacinacao_pt["Day"]
)

mortes_pt["Day"] = pd.to_datetime(
    mortes_pt["Day"]
)


# ============================================================
# 5. RESUMO
# ============================================================

print("\n" + "=" * 60)
print("RESUMO — PORTUGAL")
print("=" * 60)

print(
    "Excesso de mortalidade:",
    excesso_pt.shape
)

print(
    "Vacinação:",
    vacinacao_pt.shape
)

print(
    "Mortes COVID:",
    mortes_pt.shape
)

print("\nTratamento inicial concluído.") 

#%% Verificar mortes por semana

# ============================================================
# BLOCO 2 — TRANSFORMAÇÃO DAS MORTES COVID EM DADOS SEMANAIS
# ============================================================

print("\n" + "=" * 60)
print("TRANSFORMAÇÃO DAS MORTES COVID — SEMANAL")
print("=" * 60)


# Criar a semana
mortes_pt["Semana"] = (
    mortes_pt["Day"]
    .dt.to_period("W-SUN")
    .astype(str)
)


# Uma observação por semana
mortes_semanais = (
    mortes_pt
    .drop_duplicates(subset=["Semana"])
    [["Semana", "Weekly deaths"]]
    .reset_index(drop=True)
)


# Renomear a variável
mortes_semanais = mortes_semanais.rename(
    columns={
        "Weekly deaths": "mortes_covid"
    }
)


# ------------------------------------------------------------
# Verificar resultado
# ------------------------------------------------------------

print("\nDimensões antes da transformação:")
print(mortes_pt.shape)

print("\nDimensões depois da transformação:")
print(mortes_semanais.shape)

print("\nPrimeiras semanas:")
print(mortes_semanais.head(15))

print("\nÚltimas semanas:")
print(mortes_semanais.tail(10)) 

#%% Tratamento,a renomear "cum" a criar coluna com novo nome

# ============================================================
# BLOCO 3 — TRATAMENTO DO EXCESSO DE MORTALIDADE
# ============================================================

print("\n" + "=" * 60)
print("TRATAMENTO DO EXCESSO DE MORTALIDADE")
print("=" * 60)

# Criar uma cópia dos dados de Portugal
excesso_semana = excesso_pt.copy()

# Renomear as colunas
excesso_semana = excesso_semana.rename(
    columns={
        "Week": "Semana",
        "cum_excess_per_million_proj_all_ages":
            "excesso_cumulativo_por_milhao"
    }
)

# Manter apenas as colunas necessárias
excesso_semana = excesso_semana[
    [
        "Semana",
        "excesso_cumulativo_por_milhao"
    ]
].copy()

# ============================================================
# VERIFICAR RESULTADO
# ============================================================

print("\nDimensões:")
print(excesso_semana.shape)

print("\nPrimeiras semanas:")
print(excesso_semana.head(10))

print("\nÚltimas semanas:")
print(excesso_semana.tail(10))

print("\nPeríodo:")
print(excesso_semana["Semana"].min())
print("até")
print(excesso_semana["Semana"].max())

#%% Tratamento de dados vacinação

# ============================================================
# BLOCO 4 — TRATAMENTO DA VACINAÇÃO
# ============================================================

print("\n" + "=" * 60)
print("TRATAMENTO DA VACINAÇÃO")
print("=" * 60)

# Selecionar apenas as colunas necessárias
vacinacao_tratada = vacinacao_pt[
    [
        "Day",
        "Share of people with a complete initial protocol"
    ]
].copy()

# Renomear a coluna
vacinacao_tratada = vacinacao_tratada.rename(
    columns={
        "Share of people with a complete initial protocol":
            "cobertura_vacinal"
    }
)

print("\nDimensões:")
print(vacinacao_tratada.shape)

print("\nPrimeiras observações:")
print(vacinacao_tratada.head())

print("\nÚltimas observações:")
print(vacinacao_tratada.tail())

print("\nPeríodo:")
print(vacinacao_tratada["Day"].min())
print("até")
print(vacinacao_tratada["Day"].max())

print("\nCobertura vacinal máxima:")
print(vacinacao_tratada["cobertura_vacinal"].max()) 

#%% Guardar os dados tratados

# ============================================================
# BLOCO 5 — GUARDAR OS DADOS TRATADOS
# ============================================================

print("\n" + "=" * 60)
print("GUARDAR DADOS TRATADOS")
print("=" * 60)

# Criar a pasta, caso ainda não exista
import os

os.makedirs(
    "03_dados_tratados",
    exist_ok=True
)

# ------------------------------------------------------------
# 1. Excesso de mortalidade
# ------------------------------------------------------------

excesso_semana.to_csv(
    "03_dados_tratados/excesso_mortalidade_pt.csv",
    index=False
)

print("\n✓ Excesso de mortalidade guardado.")


# ------------------------------------------------------------
# 2. Vacinação
# ------------------------------------------------------------

vacinacao_tratada.to_csv(
    "03_dados_tratados/vacinacao_pt.csv",
    index=False
)

print("✓ Vacinação guardada.")


# ------------------------------------------------------------
# 3. Mortes COVID — semanais
# ------------------------------------------------------------

mortes_semanais.to_csv(
    "03_dados_tratados/mortes_covid_pt_semanal.csv",
    index=False
)

print("✓ Mortes COVID semanais guardadas.")


# ============================================================
# VERIFICAR FICHEIROS
# ============================================================

print("\nFicheiros na pasta 03_dados_tratados:")

print(
    os.listdir("03_dados_tratados")
)

print("\n" + "=" * 60)
print("DADOS TRATADOS GUARDADOS COM SUCESSO")
print("=" * 60)
