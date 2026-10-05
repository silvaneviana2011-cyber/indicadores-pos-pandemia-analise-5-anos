# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:46:49 2026

@author: silva
"""

#%% Explorarar as variáveis do Pordata

# ----------------------------------------------------------
# BLOCO 1 — CARREGAR DADOS PORDATA
# ----------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt 

print("="*60)
print("ÓBITOS POR CAUSAS DE MORTE — PORDATA")
print("="*60)

ficheiro = (
    "02_dados_originais/"
    "obidos_2020_2024_pordata.xlsx"
)

df_pordata = pd.read_excel(ficheiro)

print("\nFicheiro carregado com sucesso.")

print("\nDimensões:")
print(df_pordata.shape)

print("\nNomes das colunas:")
print(df_pordata.columns.tolist())

print("\nPrimeiras linhas:")
print(df_pordata.head(10))

#%% A explorar estrutura

# ----------------------------------------------------------
# BLOCO 2 — EXPLORAR ESTRUTURA DOS DADOS
# ----------------------------------------------------------

print("\n" + "="*60)
print("ESTRUTURA DOS DADOS PORDATA")
print("="*60)

print("\nDimensões:")
print(df_pordata.shape)

print("\nColunas:")
print(df_pordata.iloc[6].dropna().tolist())

print("\nAnos disponíveis:")
print(df_pordata.iloc[7:, 0].dropna().tolist())

print("\nPrimeiras linhas dos dados:")
print(df_pordata.iloc[6:12, :10].to_string(index=False))

#%% Limpar e Organizar

# ----------------------------------------------------------
# BLOCO 3 — LIMPAR E ORGANIZAR OS DADOS
# ----------------------------------------------------------

dados_pordata = df_pordata.iloc[7:12, :12].copy()

dados_pordata.columns = (
    ["Ano"] +
    df_pordata.iloc[6, 1:12].tolist()
)

print("\n" + "="*60)
print("DADOS PORDATA ORGANIZADOS")
print("="*60)

print("\nDimensões:")
print(dados_pordata.shape)

print("\nDados:")
print(dados_pordata.to_string(index=False))

#%% A verificar os dados

# ----------------------------------------------------------
# BLOCO 4 — VERIFICAR OS DADOS
# ----------------------------------------------------------

print("\n" + "="*60)
print("VERIFICAÇÃO DOS DADOS")
print("="*60)

print("\nTipos de dados:")
print(dados_pordata.dtypes)

print("\nValores em falta:")
print(dados_pordata.isna().sum())

print("\nValores duplicados:")
print(dados_pordata.duplicated().sum())

print("\nNúmero de anos:")
print(dados_pordata["Ano"].nunique())

print("\nAnos:")
print(dados_pordata["Ano"].tolist())

#%% A converter valores 

# ----------------------------------------------------------
# BLOCO 5 — CONVERTER VALORES PARA NUMÉRICOS
# ----------------------------------------------------------

colunas_numericas = dados_pordata.columns[1:]

dados_pordata[colunas_numericas] = dados_pordata[
    colunas_numericas
].apply(pd.to_numeric, errors="coerce")

dados_pordata["Ano"] = pd.to_numeric(
    dados_pordata["Ano"],
    errors="coerce"
).astype(int)

print("\n" + "="*60)
print("TIPOS DE DADOS APÓS CONVERSÃO")
print("="*60)

print(dados_pordata.dtypes)

#%% Selecionar variáveis principais

# ----------------------------------------------------------
# BLOCO 6 — GUARDAR DATASET PORDATA TRATADO
# ----------------------------------------------------------

ficheiro_saida = (
    "03_dados_tratados/"
    "obitos_pordata_2020_2024.csv"
)

dados_pordata.to_csv(
    ficheiro_saida,
    index=False,
    encoding="utf-8-sig"
)

print("\n" + "="*60)
print("DATASET PORDATA GUARDADO")
print("="*60)

print("\nFicheiro guardado com sucesso:")
print(ficheiro_saida)

print("\nDimensões finais:")
print(dados_pordata.shape) 

#%% 
# ============================================================
# BLOCO 7 — EVOLUÇÃO DAS DOENÇAS DO APARELHO CIRCULATÓRIO
# ============================================================

# Ler o dataset PORDATA já tratado
df_grafico = pd.read_csv(
    "03_dados_tratados/obitos_pordata_2020_2024.csv"
)

# Selecionar os dados necessários
anos = df_grafico.iloc[:, 0]
obitos_circulatorio = df_grafico.iloc[:, 1]

# Criar gráfico
plt.figure(figsize=(10, 6))

plt.plot(
    anos,
    obitos_circulatorio,
    marker="o",
    linewidth=2
)

plt.title(
    "Evolução dos óbitos por doenças do aparelho circulatório\n"
    "Portugal, 2020–2024"
)

plt.xlabel("Ano")
plt.ylabel("Número de óbitos")

plt.xticks(anos)

plt.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

plt.show() 

#%% A fazer a comparação das principais causas mortes 

# ============================================================
# BLOCO 8 — COMPARAÇÃO DAS PRINCIPAIS CAUSAS DE MORTE
# ============================================================

# Ler o dataset PORDATA já tratado
df_grafico = pd.read_csv(
    "03_dados_tratados/obitos_pordata_2020_2024.csv"
)

# ------------------------------------------------------------
# Dados
# ------------------------------------------------------------

anos = df_grafico.iloc[:, 0]

circulatorio = df_grafico.iloc[:, 1]
tumores = df_grafico.iloc[:, 2]
respiratorio = df_grafico.iloc[:, 6]
covid = df_grafico.iloc[:, 11]


# ------------------------------------------------------------
# Criar gráfico
# ------------------------------------------------------------

plt.figure(figsize=(11, 6))


# Doenças do aparelho circulatório
plt.plot(
    anos,
    circulatorio,
    marker="o",
    linewidth=2,
    label="Doenças do aparelho circulatório"
)


# Tumores malignos
plt.plot(
    anos,
    tumores,
    marker="o",
    linewidth=2,
    label="Tumores malignos"
)


# Doenças do aparelho respiratório
plt.plot(
    anos,
    respiratorio,
    marker="o",
    linewidth=2,
    label="Doenças do aparelho respiratório"
)


# COVID-19
plt.plot(
    anos,
    covid,
    marker="o",
    linewidth=2,
    label="COVID-19"
)


# ------------------------------------------------------------
# Destacar o ponto máximo da COVID-19
# ------------------------------------------------------------

indice_max_covid = covid.idxmax()

ano_max_covid = anos.loc[indice_max_covid]

valor_max_covid = covid.loc[indice_max_covid]


# Linha vertical no ano do pico
plt.axvline(
    x=ano_max_covid,
    linestyle="--",
    alpha=0.6
)


# ------------------------------------------------------------
# Título e eixos
# ------------------------------------------------------------

plt.title(
    "Evolução das principais causas de morte\n"
    "Portugal, 2020–2024",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Ano")

plt.ylabel("Número de óbitos")


# Anos no eixo X
plt.xticks(anos)


# Grelha
plt.grid(
    True,
    linestyle="--",
    alpha=0.3
)


# Legenda
plt.legend()


# Ajustar apresentação
plt.tight_layout()


# Mostrar gráfico
plt.show()

#%% A variação percentual

# ============================================================
# BLOCO 9 — VARIAÇÃO DOS ÓBITOS ENTRE 2020 E 2024
# ============================================================

# Valores de 2020
valores_2020 = df_grafico.iloc[0, 1:]

# Valores de 2024
valores_2024 = df_grafico.iloc[-1, 1:]

# Calcular variação percentual
variacao_percentual = (
    (valores_2024 - valores_2020)
    / valores_2020
) * 100

# Criar dataframe com os resultados
df_variacao = pd.DataFrame({
    "Causa de morte": valores_2020.index,
    "Variação (%)": variacao_percentual.values
})

# Retirar COVID-19 para analisar primeiro as causas gerais
df_variacao = df_variacao[
    df_variacao["Causa de morte"] != "COVID-19"
]

# Ordenar da maior para a menor variação
df_variacao = df_variacao.sort_values(
    "Variação (%)",
    ascending=False
)

print("\n--- VARIAÇÃO DOS ÓBITOS 2020–2024 ---")
print(df_variacao)



# ============================================================
# GRÁFICO
# ============================================================

plt.figure(figsize=(11, 6))

plt.barh(
    df_variacao["Causa de morte"],
    df_variacao["Variação (%)"],
    color="#0FF1F5"
)

plt.axvline(
    x=0,
    linestyle="-",
    linewidth=1
)

plt.title(
    "Variação percentual dos óbitos por causa de morte\n"
    "Portugal, 2020–2024",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Variação (%)")
plt.ylabel("Causa de morte")

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()

plt.show()

#%% Bloco 9 Grafico com o percentual

# ============================================================
# BLOCO 10 — PESO PERCENTUAL DA COVID-19 NA MORTALIDADE
# ============================================================

# Anos
anos_covid = [2020, 2021, 2022, 2023, 2024]

# Percentagem de óbitos atribuídos à COVID-19
percentagem_covid = [5.8, 10.4, 6.2, 2.1, 1.1]


# ============================================================
# GRÁFICO
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    anos_covid,
    percentagem_covid,
    marker="o",
    linewidth=2.5,
    color="#0FF1F5"
)


# ------------------------------------------------------------
# Valores sobre os pontos
# ------------------------------------------------------------

for x, y in zip(
    anos_covid,
    percentagem_covid
):
    plt.annotate(
        f"{y:.1f}%",
        (x, y),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center",
        fontsize=10,
        fontweight="bold"
    )


# ------------------------------------------------------------
# Destacar o pico de 2021
# ------------------------------------------------------------

indice_max = percentagem_covid.index(
    max(percentagem_covid)
)

ano_max = anos_covid[indice_max]
valor_max = percentagem_covid[indice_max]

plt.axvline(
    x=ano_max,
    linestyle="--",
    alpha=0.6
)

plt.annotate(
    f"Pico: {valor_max:.1f}%",
    xy=(ano_max, valor_max),
    xytext=(ano_max + 0.15, valor_max - 1),
    arrowprops=dict(
        arrowstyle="->",
        linewidth=1.5
    ),
    fontsize=10,
    fontweight="bold"
)


# ------------------------------------------------------------
# Título e eixos
# ------------------------------------------------------------

plt.title(
    "Peso da COVID-19 no total de óbitos\n"
    "Portugal, 2020–2024",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Ano")

plt.ylabel("Óbitos por COVID-19 (%)")

plt.xticks(anos_covid)

plt.ylim(0, 12)

plt.grid(
    True,
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()

plt.show() 


#%% Ranking causa mortes

# ============================================================
# BLOCO 11 — RANKING DAS CAUSAS DE MORTE EM 2024
# ============================================================

# Ler o dataset PORDATA já tratado
df_grafico = pd.read_csv(
    "03_dados_tratados/obitos_pordata_2020_2024.csv"
)

# Selecionar a última linha = 2024
dados_2024 = df_grafico.iloc[-1, 1:]

# Criar dataframe para o ranking
df_ranking_2024 = pd.DataFrame({
    "Causa de morte": dados_2024.index,
    "Óbitos": dados_2024.values
})

# Garantir que os óbitos são numéricos
df_ranking_2024["Óbitos"] = pd.to_numeric(
    df_ranking_2024["Óbitos"]
)

# Ordenar do menor para o maior
df_ranking_2024 = df_ranking_2024.sort_values(
    "Óbitos",
    ascending=True
)


# ============================================================
# GRÁFICO
# ============================================================

plt.figure(figsize=(11, 7))

# Paleta do projeto:
# púrpura → lilás → verde → azul/ciano

cores = [
    "#5B2C83",
    "#70449A",
    "#8E5BB7",
    "#A875C4",
    "#B58AD4",
    "#7BC96F",
    "#52C58B",
    "#35C9A5",
    "#32B8C7",
    "#3FA7D6",
    "#0FF1F5"
]

plt.barh(
    df_ranking_2024["Causa de morte"],
    df_ranking_2024["Óbitos"],
    color=cores[:len(df_ranking_2024)]
)


# ============================================================
# VALORES NO FINAL DAS BARRAS
# ============================================================

for i, valor in enumerate(df_ranking_2024["Óbitos"]):

    plt.text(
        valor + 300,
        i,
        f"{valor:,.0f}".replace(",", "."),
        va="center",
        fontsize=9
    )


# ============================================================
# TÍTULO E EIXOS
# ============================================================

plt.title(
    "Principais causas de morte em Portugal\n"
    "2024",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Número de óbitos")

plt.ylabel("Causa de morte")


# ============================================================
# GRELHA
# ============================================================

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.25
)


# ============================================================
# LIMPEZA VISUAL
# ============================================================

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_visible(False)

plt.tight_layout()

plt.show() 

#%%  Quadro comparativo

# ============================================================
# BLOCO 12 — COMPARAÇÃO DAS CAUSAS DE MORTE
# 2020 vs. 2024
# ============================================================

# Ler o dataset PORDATA já tratado
df_comparacao = pd.read_csv(
    "03_dados_tratados/obitos_pordata_2020_2024.csv"
)

# ------------------------------------------------------------
# Selecionar 2020 e 2024
# ------------------------------------------------------------

dados_2020 = df_comparacao.iloc[0, 1:]
dados_2024 = df_comparacao.iloc[-1, 1:]

# Criar dataframe
df_comparacao_causas = pd.DataFrame({
    "Causa de morte": dados_2020.index,
    "2020": dados_2020.values,
    "2024": dados_2024.values
})

# Garantir valores numéricos
df_comparacao_causas["2020"] = pd.to_numeric(
    df_comparacao_causas["2020"]
)

df_comparacao_causas["2024"] = pd.to_numeric(
    df_comparacao_causas["2024"]
)

# Ordenar pela quantidade de mortes em 2024
df_comparacao_causas = df_comparacao_causas.sort_values(
    "2024",
    ascending=True
)


# ============================================================
# GRÁFICO
# ============================================================

import numpy as np

plt.figure(figsize=(12, 8))

posicoes = np.arange(
    len(df_comparacao_causas)
)

largura = 0.35


# 2020
plt.barh(
    posicoes - largura / 2,
    df_comparacao_causas["2020"],
    height=largura,
    color="#5B2C83",
    label="2020"
)


# 2024
plt.barh(
    posicoes + largura / 2,
    df_comparacao_causas["2024"],
    height=largura,
    color="#0FF1F5",
    label="2024"
)


# ------------------------------------------------------------
# Nomes das causas
# ------------------------------------------------------------

plt.yticks(
    posicoes,
    df_comparacao_causas["Causa de morte"]
)


# ------------------------------------------------------------
# Título
# ------------------------------------------------------------

plt.title(
    "Comparação das causas de morte\n"
    "Portugal — 2020 vs. 2024",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Número de óbitos")

plt.ylabel("Causa de morte")


# ------------------------------------------------------------
# Grelha
# ------------------------------------------------------------

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.25
)


# ------------------------------------------------------------
# Legenda
# ------------------------------------------------------------

plt.legend()


# ------------------------------------------------------------
# Limpeza visual
# ------------------------------------------------------------

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_visible(False)

plt.tight_layout()

plt.show()

#%% Correlações 💜💚💙

# ============================================================
# BLOCO 13 — HEATMAP DAS CAUSAS DE MORTE
# Portugal, 2020–2024
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# Ler o dataset PORDATA já tratado
# ------------------------------------------------------------

df_heatmap = pd.read_csv(
    "03_dados_tratados/obitos_pordata_2020_2024.csv"
)

# ------------------------------------------------------------
# Preparar os dados
# ------------------------------------------------------------

df_heatmap = df_heatmap.set_index("Ano")

dados_heatmap = df_heatmap.T

# ------------------------------------------------------------
# Criar o heatmap
# ------------------------------------------------------------

plt.figure(figsize=(14, 8))

sns.heatmap(
    dados_heatmap,
    annot=True,
    fmt=".0f",
    cmap="Reds",
    linewidths=0.5,
    cbar_kws={
        "label": "Número de óbitos"
    }
)

# ------------------------------------------------------------
# Título
# ------------------------------------------------------------

plt.title(
    "Heatmap das causas de morte em Portugal\n"
    "2020–2024",
    fontsize=16,
    fontweight="bold"
)

# ------------------------------------------------------------
# Eixos
# ------------------------------------------------------------

plt.xlabel("Ano")
plt.ylabel("Causa de morte")

# ------------------------------------------------------------
# Ajustar o gráfico
# ------------------------------------------------------------

plt.tight_layout()

plt.show()

#%% Comparação Covid e Doenças respiratórias

# ============================================================
# BLOCO 14 — COVID-19 VS. DOENÇAS RESPIRATÓRIAS
# Portugal, 2020–2024
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Ler o dataset PORDATA já tratado
# ------------------------------------------------------------

df_covid_resp = pd.read_csv(
    "03_dados_tratados/obitos_pordata_2020_2024.csv"
)

# ------------------------------------------------------------
# Selecionar os dados
# ------------------------------------------------------------

anos = df_covid_resp.iloc[:, 0]

respiratorio = df_covid_resp.iloc[:, 6]

covid = df_covid_resp.iloc[:, 11]

# ------------------------------------------------------------
# Criar o gráfico
# ------------------------------------------------------------

plt.figure(figsize=(11, 6))

plt.plot(
    anos,
    respiratorio,
    marker="o",
    linewidth=2.5,
    color="#5B2C83",
    label="Doenças do aparelho respiratório"
)

plt.plot(
    anos,
    covid,
    marker="o",
    linewidth=2.5,
    color="#0FF1F5",
    label="COVID-19"
)

# ------------------------------------------------------------
# Destacar o pico da COVID-19
# ------------------------------------------------------------

indice_max = covid.idxmax()

ano_max = anos.loc[indice_max]

valor_max = covid.loc[indice_max]

plt.axvline(
    x=ano_max,
    linestyle="--",
    alpha=0.5
)

plt.annotate(
    f"Pico COVID-19: {valor_max:,.0f}".replace(",", "."),
    xy=(ano_max, valor_max),
    xytext=(ano_max + 0.15, valor_max + 1000),
    arrowprops=dict(
        arrowstyle="->",
        linewidth=1.5
    ),
    fontsize=10,
    fontweight="bold"
)

# ------------------------------------------------------------
# Título e eixos
# ------------------------------------------------------------

plt.title(
    "COVID-19 e doenças do aparelho respiratório\n"
    "Portugal, 2020–2024",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Ano")
plt.ylabel("Número de óbitos")

plt.xticks(anos)

plt.grid(
    linestyle="--",
    alpha=0.25
)

plt.legend()

# ------------------------------------------------------------
# Ajustes finais
# ------------------------------------------------------------

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.tight_layout()

plt.show()

#%% Covid x Principais causas

# ============================================================
# BLOCO 15 — POSIÇÃO DA COVID-19 FACE ÀS PRINCIPAIS CAUSAS
# Portugal, 2020–2024
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Ler o dataset PORDATA já tratado
# ------------------------------------------------------------

df_posicao = pd.read_csv(
    "03_dados_tratados/obitos_pordata_2020_2024.csv"
)

# ------------------------------------------------------------
# Selecionar os dados
# ------------------------------------------------------------

anos = df_posicao.iloc[:, 0]

circulatorio = df_posicao.iloc[:, 1]

tumores = df_posicao.iloc[:, 2]

respiratorio = df_posicao.iloc[:, 6]

covid = df_posicao.iloc[:, 11]

# ------------------------------------------------------------
# Criar gráfico
# ------------------------------------------------------------

plt.figure(figsize=(11, 6))

plt.plot(
    anos,
    circulatorio,
    marker="o",
    linewidth=2.5,
    color="#5B2C83",
    label="Doenças circulatórias"
)

plt.plot(
    anos,
    tumores,
    marker="o",
    linewidth=2.5,
    color="#A875C4",
    label="Tumores malignos"
)

plt.plot(
    anos,
    respiratorio,
    marker="o",
    linewidth=2.5,
    color="#35C9A5",
    label="Doenças respiratórias"
)

plt.plot(
    anos,
    covid,
    marker="o",
    linewidth=3,
    color="#0FF1F5",
    label="COVID-19"
)

# ------------------------------------------------------------
# Destacar os valores da COVID
# ------------------------------------------------------------

for x, y in zip(anos, covid):

    plt.annotate(
        f"{y:,.0f}".replace(",", "."),
        (x, y),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center",
        fontsize=9,
        fontweight="bold"
    )

# ------------------------------------------------------------
# Título
# ------------------------------------------------------------

plt.title(
    "Evolução da COVID-19 face às principais causas de morte\n"
    "Portugal, 2020–2024",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Ano")
plt.ylabel("Número de óbitos")

plt.xticks(anos)

plt.grid(
    linestyle="--",
    alpha=0.25
)

plt.legend()

# ------------------------------------------------------------
# Limpeza visual
# ------------------------------------------------------------

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.tight_layout()

plt.show()

#%% Comparação de Óbitos

# ============================================================
# BLOCO 16 — VARIAÇÃO ANUAL DOS ÓBITOS POR COVID-19
# Portugal, 2020–2024
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Ler o dataset PORDATA já tratado
# ------------------------------------------------------------

df_variacao_covid = pd.read_csv(
    "03_dados_tratados/obitos_pordata_2020_2024.csv"
)

# ------------------------------------------------------------
# Selecionar os dados da COVID-19
# ------------------------------------------------------------

anos = df_variacao_covid.iloc[:, 0]

covid = pd.to_numeric(
    df_variacao_covid.iloc[:, 11]
)

# ------------------------------------------------------------
# Calcular a variação percentual anual
# ------------------------------------------------------------

variacao_anual = covid.pct_change() * 100

# ------------------------------------------------------------
# Criar DataFrame
# ------------------------------------------------------------

df_variacao = pd.DataFrame({
    "Ano": anos,
    "Óbitos COVID-19": covid,
    "Variação anual (%)": variacao_anual
})

# ------------------------------------------------------------
# Mostrar os resultados
# ------------------------------------------------------------

print("\nVariação anual dos óbitos por COVID-19:")
print(df_variacao)

# ------------------------------------------------------------
# Criar gráfico
# ------------------------------------------------------------

plt.figure(figsize=(11, 6))

# Retirar 2020 porque não existe ano anterior
dados_grafico = df_variacao.iloc[1:]

plt.bar(
    dados_grafico["Ano"],
    dados_grafico["Variação anual (%)"],
    color="#0FF1F5"
)

# ------------------------------------------------------------
# Linha de referência
# ------------------------------------------------------------

plt.axhline(
    y=0,
    linewidth=1,
    alpha=0.6
)

# ------------------------------------------------------------
# Valores nas barras
# ------------------------------------------------------------

for x, y in zip(
    dados_grafico["Ano"],
    dados_grafico["Variação anual (%)"]
):

    plt.text(
        x,
        y + (2 if y >= 0 else -5),
        f"{y:.1f}%",
        ha="center",
        va="bottom" if y >= 0 else "top",
        fontsize=10,
        fontweight="bold"
    )

# ------------------------------------------------------------
# Título e eixos
# ------------------------------------------------------------

plt.title(
    "Variação anual dos óbitos por COVID-19\n"
    "Portugal, 2021–2024",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Ano")
plt.ylabel("Variação em relação ao ano anterior (%)")

plt.xticks(dados_grafico["Ano"])

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.25
)

# ------------------------------------------------------------
# Limpeza visual
# ------------------------------------------------------------

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.tight_layout()

plt.show()

#%% Calcular as médias por doença

# ============================================================
# BLOCO 17 — MÉDIA DE ÓBITOS POR CAUSA
# Portugal, 2020–2024
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Ler o dataset PORDATA já tratado
# ------------------------------------------------------------

df_media = pd.read_csv(
    "03_dados_tratados/obitos_pordata_2020_2024.csv"
)

# ------------------------------------------------------------
# Calcular a média de cada causa
# ------------------------------------------------------------

dados_causas = df_media.iloc[:, 1:]

media_obitos = dados_causas.mean()

# ------------------------------------------------------------
# Criar DataFrame
# ------------------------------------------------------------

df_media_causas = pd.DataFrame({
    "Causa de morte": media_obitos.index,
    "Média de óbitos": media_obitos.values
})

# ------------------------------------------------------------
# Ordenar da menor para a maior média
# ------------------------------------------------------------

df_media_causas = df_media_causas.sort_values(
    "Média de óbitos",
    ascending=True
)

# ------------------------------------------------------------
# Mostrar resultados
# ------------------------------------------------------------

print("\nMédia de óbitos por causa — 2020–2024:")
print(
    df_media_causas.to_string(index=False)
)

# ------------------------------------------------------------
# Criar gráfico
# ------------------------------------------------------------

plt.figure(figsize=(11, 7))

plt.barh(
    df_media_causas["Causa de morte"],
    df_media_causas["Média de óbitos"],
    color="#7BC96F"
)

# ------------------------------------------------------------
# Valores nas barras
# ------------------------------------------------------------

for i, valor in enumerate(
    df_media_causas["Média de óbitos"]
):

    plt.text(
        valor + 200,
        i,
        f"{valor:,.0f}".replace(",", "."),
        va="center",
        fontsize=9
    )

# ------------------------------------------------------------
# Título e eixos
# ------------------------------------------------------------

plt.title(
    "Média anual de óbitos por causa\n"
    "Portugal, 2020–2024",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Média anual de óbitos")
plt.ylabel("Causa de morte")

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.25
)

# ------------------------------------------------------------
# Limpeza visual
# ------------------------------------------------------------

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_visible(False)

plt.tight_layout()

plt.show()

#%% Top 5 de Causas de mortes em Portugal

# ============================================================
# BLOCO 18 — TOP 5 CAUSAS DE MORTE
# Média anual — Portugal, 2020–2024
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Ler o dataset tratado
# ------------------------------------------------------------

df_top5 = pd.read_csv(
    "03_dados_tratados/obitos_pordata_2020_2024.csv"
)

# ------------------------------------------------------------
# Calcular a média de óbitos por causa
# ------------------------------------------------------------

dados_causas = df_top5.iloc[:, 1:]

media_obitos = dados_causas.mean()

# ------------------------------------------------------------
# Criar DataFrame
# ------------------------------------------------------------

df_top5 = pd.DataFrame({
    "Causa de morte": media_obitos.index,
    "Média de óbitos": media_obitos.values
})

# ------------------------------------------------------------
# Selecionar Top 5
# ------------------------------------------------------------

df_top5 = df_top5.nlargest(
    5,
    "Média de óbitos"
)

# Ordenar para o gráfico
df_top5 = df_top5.sort_values(
    "Média de óbitos",
    ascending=True
)

# ------------------------------------------------------------
# Mostrar o Top 5
# ------------------------------------------------------------

print("\nTOP 5 — Média anual de óbitos (2020–2024):")
print(
    df_top5.to_string(index=False)
)

# ------------------------------------------------------------
# Degradê púrpura
# ------------------------------------------------------------

cores = [
    "#D8B4E2",
    "#B58AD4",
    "#9365BD",
    "#70449A",
    "#5B2C83"
]

# ------------------------------------------------------------
# Criar gráfico
# ------------------------------------------------------------

plt.figure(figsize=(11, 6))

plt.barh(
    df_top5["Causa de morte"],
    df_top5["Média de óbitos"],
    color=cores
)

# ------------------------------------------------------------
# Valores nas barras
# ------------------------------------------------------------

for i, valor in enumerate(
    df_top5["Média de óbitos"]
):

    plt.text(
        valor + 200,
        i,
        f"{valor:,.0f}".replace(",", "."),
        va="center",
        fontsize=10,
        fontweight="bold"
    )

# ------------------------------------------------------------
# Título e eixos
# ------------------------------------------------------------

plt.title(
    "Top 5 causas de morte em Portugal\n"
    "Média anual de óbitos — 2020–2024",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Média anual de óbitos")
plt.ylabel("Causa de morte")

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.25
)

# ------------------------------------------------------------
# Limpeza visual
# ------------------------------------------------------------

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_visible(False)

plt.tight_layout()

plt.show() 