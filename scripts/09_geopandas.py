# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 12:15:42 2026

@author: silva
"""

#%% A conhecer o conteúdo do ficheiro


# ============================================================
# BLOCO 1 — IMPORTAÇÃO DAS BIBLIOTECAS
# ============================================================

import geopandas as gpd
import matplotlib.pyplot as plt
from dash import html


# Referências:
# GeoPandas Documentation:
# https://geopandas.org/
#
# Matplotlib Documentation:
# https://matplotlib.org/


import geopandas as gpd

mapa = gpd.read_file(
    r"C:\Users\silva\Desktop\Projeto_Covid_Portugal\04_geopandas\Continente_CAOP2025.gpkg",
    layer="cont_municipios"
)

print(mapa.shape)
print(mapa.columns)
print(mapa.crs)

#%% Confirmar leitura do mapa

# ============================================================
# BLOCO 2 — CARREGAMENTO DOS DADOS GEOGRÁFICOS
# ============================================================

ficheiro_mapa = (
    r"C:\Users\silva\Desktop\Projeto_Covid_Portugal"
    r"\04_geopandas\Continente_CAOP2025.gpkg"
)

mapa = gpd.read_file(
    ficheiro_mapa,
    layer="cont_municipios"
)

# Fonte dos dados geográficos:
# Direção-Geral do Território (DGT)
# Carta Administrativa Oficial de Portugal (CAOP) 2025
# Portugal Continental
#
# https://www.dgterritorio.gov.pt/atividades/cartografia/cartografia-tematica/caop

#%% Ver o mapa

# ============================================================
# BLOCO 3 — VERIFICAÇÃO DA GEO-DATAFRAME
# ============================================================

print("Dimensão:", mapa.shape)

print("\nColunas:")
print(mapa.columns)

print("\nSistema de Coordenadas:")
print(mapa.crs)

# Fonte:
# CAOP2025 — Direção-Geral do Território (DGT)

# ============================================================
# BLOCO 4 — MAPA BASE DOS MUNICÍPIOS
# ============================================================

fig, ax = plt.subplots(figsize=(10, 10))

mapa.plot(
    ax=ax,
    color="#3A7D44",
    edgecolor="black",
    linewidth=0.3
)

ax.set_title(
    "Municípios de Portugal Continental — CAOP 2025",
    fontsize=14
)

ax.axis("off")

plt.show()

# Fonte dos dados geográficos:
# Direção-Geral do Território (DGT)
# CAOP 2025 — Portugal Continental
#
# Visualização:
# GeoPandas + Matplotlib

# ============================================================
# BLOCO 5 — CARREGAMENTO DOS DADOS COVID POR CONCELHO
# ============================================================

import pandas as pd

ficheiro_covid = (
    r"C:\Users\silva\Desktop\Projeto_Covid_Portugal"
    r"\04_geopandas\data_concelhos.csv"
)

dados_covid = pd.read_csv(ficheiro_covid)


# Verificação inicial
print("\nDimensão dos dados COVID:")
print(dados_covid.shape)

print("\nColunas:")
print(dados_covid.columns)

print("\nPrimeiros registos:")
print(dados_covid.head())


# Fonte:
# DSSG Portugal — COVID-19 Portugal Data
# Dados originalmente provenientes de fontes da DGS.
# https://github.com/dssg-pt/covid19pt-data

# ============================================================
# BLOCO 6 — TRANSFORMAÇÃO PARA FORMATO LONGO
# ============================================================
#
# Fonte dos dados originais:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
#
# Transformação realizada com Pandas (melt).
# ============================================================

dados_covid_long = dados_covid.melt(
    id_vars="data",
    var_name="municipio",
    value_name="casos_covid"
)

print("\nDimensão após transformação:")
print(dados_covid_long.shape)

print("\nPrimeiros registos:")
print(dados_covid_long.head())

# ============================================================
# BLOCO 7 — VERIFICAÇÃO DOS MUNICÍPIOS
# ============================================================
#
# Objetivo:
# Comparar os nomes dos municípios presentes nos dados
# COVID com os municípios existentes na CAOP 2025.
#
# Fonte dos dados COVID:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
#
# Fonte geográfica:
# Direção-Geral do Território — CAOP 2025
# https://www.dgterritorio.gov.pt/
# ============================================================

municipios_covid = set(dados_covid_long["municipio"].dropna())
municipios_mapa = set(mapa["municipio"].dropna())

# Municípios existentes nos dados COVID mas não no mapa
nao_estao_mapa = municipios_covid - municipios_mapa

# Municípios existentes no mapa mas não nos dados COVID
nao_estao_covid = municipios_mapa - municipios_covid

print("\nMunicípios dos dados COVID que não estão na CAOP:")
print(sorted(nao_estao_mapa))

print("\nMunicípios da CAOP que não estão nos dados COVID:")
print(sorted(nao_estao_covid))

print("\nNúmero de municípios COVID:", len(municipios_covid))
print("Número de municípios CAOP:", len(municipios_mapa))

# ============================================================
# BLOCO 8 — IDENTIFICAÇÃO DAS DIFERENÇAS GEOGRÁFICAS
# ============================================================
#
# Objetivo:
# Identificar os municípios presentes nos dados COVID que
# não possuem correspondência direta na CAOP 2025.
#
# Fonte dos dados COVID:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
#
# Fonte geográfica:
# Direção-Geral do Território — CAOP 2025
# https://www.dgterritorio.gov.pt/
# ============================================================

print("\nMunicípios COVID sem correspondência direta na CAOP 2025:")

for municipio in sorted(nao_estao_mapa):
    print(municipio)

print("\nTotal:", len(nao_estao_mapa)) 

# ============================================================
# BLOCO 9 — NORMALIZAÇÃO DOS NOMES DOS MUNICÍPIOS
# ============================================================
#
# Objetivo:
# Uniformizar a capitalização dos nomes dos municípios para
# permitir a correspondência entre os dados COVID e a CAOP.
#
# Os nomes originais são preservados nas colunas originais.
#
# Fonte dos dados COVID:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
#
# Fonte geográfica:
# Direção-Geral do Território — CAOP 2025
# https://www.dgterritorio.gov.pt/
# ============================================================

dados_covid_long["municipio_merge"] = (
    dados_covid_long["municipio"].str.strip().str.upper()
)

mapa["municipio_merge"] = (
    mapa["municipio"].str.strip().str.upper()
)

print("\nExemplo de nomes COVID:")
print(dados_covid_long["municipio_merge"].head())

print("\nExemplo de nomes CAOP:")
print(mapa["municipio_merge"].head())

# Comparação após normalização

municipios_covid = set(
    dados_covid_long["municipio_merge"].dropna()
)

municipios_mapa = set(
    mapa["municipio_merge"].dropna()
)

nao_estao_mapa = municipios_covid - municipios_mapa
nao_estao_covid = municipios_mapa - municipios_covid

print("\nMunicípios COVID sem correspondência na CAOP:")
print(sorted(nao_estao_mapa))

print("\nMunicípios CAOP sem correspondência nos dados COVID:")
print(sorted(nao_estao_covid))

print("\nNúmero de municípios COVID:", len(municipios_covid))
print("Número de municípios CAOP:", len(municipios_mapa))

# ============================================================
# BLOCO 10 — FILTRAGEM DOS MUNICÍPIOS DO CONTINENTE
# ============================================================
#
# Objetivo:
# Selecionar dos dados COVID apenas os municípios presentes
# na CAOP 2025 utilizada neste projeto, correspondente ao
# território de Portugal Continental.
#
# Fonte dos dados COVID:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
#
# Fonte geográfica:
# Direção-Geral do Território — CAOP 2025
# https://www.dgterritorio.gov.pt/
# ============================================================

dados_covid_continente = dados_covid_long[
    dados_covid_long["municipio_merge"].isin(
        mapa["municipio_merge"]
    )
].copy()

print("\nDimensão dos dados COVID — Continente:")
print(dados_covid_continente.shape)

print(
    "\nNúmero de municípios:",
    dados_covid_continente["municipio_merge"].nunique()
) 

# ============================================================
# BLOCO 11 — ANÁLISE DO PERÍODO DOS DADOS COVID
# ============================================================
#
# Objetivo:
# Verificar as datas disponíveis nos dados COVID filtrados
# para Portugal Continental.
#
# Fonte:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
# ============================================================

dados_covid_continente["data"] = pd.to_datetime(
    dados_covid_continente["data"],
    format="%d-%m-%Y"
)

print("\nData inicial:")
print(dados_covid_continente["data"].min())

print("\nData final:")
print(dados_covid_continente["data"].max())

print("\nNúmero de datas:")
print(dados_covid_continente["data"].nunique())

# ============================================================
# BLOCO 12 — COBERTURA DOS DADOS COVID
# ============================================================
#
# Objetivo:
# Avaliar a quantidade de valores disponíveis ao longo
# do período analisado.
#
# Fonte:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
# ============================================================

cobertura = (
    dados_covid_continente
    .groupby("data")["casos_covid"]
    .count()
)

print("\nNúmero de municípios com dados por data:")
print(cobertura)

print("\nMaior cobertura:")
print(cobertura.max())

print("\nData(s) com maior cobertura:")
print(cobertura[cobertura == cobertura.max()])

# ============================================================
# BLOCO 13 — SELEÇÃO DA DATA PARA O MAPA
# ============================================================
#
# Objetivo:
# Selecionar os dados de 26 de outubro de 2020, data que
# apresenta a maior cobertura disponível no conjunto analisado.
#
# Fonte:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
# ============================================================

data_mapa = pd.Timestamp("2020-10-26")

covid_2020_10_26 = dados_covid_continente[
    dados_covid_continente["data"] == data_mapa
].copy()

print("\nData selecionada:")
print(data_mapa)

print("\nDimensão:")
print(covid_2020_10_26.shape)

print("\nMunicípios com dados:")
print(covid_2020_10_26["casos_covid"].count())

print("\nPrimeiros registos:")
print(covid_2020_10_26.head())

# ============================================================
# BLOCO 14 — IDENTIFICAÇÃO DOS MUNICÍPIOS SEM DADOS
# ============================================================
#
# Objetivo:
# Identificar os municípios sem valor disponível para
# casos COVID-19 na data selecionada.
#
# Nota metodológica:
# A ausência de valor (NaN) não será interpretada como
# zero casos.
#
# Fonte:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
# ============================================================

municipios_sem_dados = covid_2020_10_26[
    covid_2020_10_26["casos_covid"].isna()
]["municipio"].tolist()

print("\nMunicípios sem dados em 26/10/2020:")

for municipio in municipios_sem_dados:
    print(municipio)

print("\nTotal de municípios sem dados:", len(municipios_sem_dados))

# ============================================================
# BLOCO 15 — JUNÇÃO DOS DADOS COVID COM A CAOP
# ============================================================
#
# Objetivo:
# Associar os casos COVID-19 de 26/10/2020 à geometria
# dos municípios de Portugal Continental.
#
# Chave de ligação:
# municipio_merge
#
# Fonte dos dados COVID:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
#
# Fonte geográfica:
# Direção-Geral do Território — CAOP 2025
# https://www.dgterritorio.gov.pt/
# ============================================================

mapa_covid = mapa.merge(
    covid_2020_10_26[
        ["municipio_merge", "casos_covid"]
    ],
    on="municipio_merge",
    how="left"
)

print("\nDimensão do mapa após o merge:")
print(mapa_covid.shape)

print("\nColunas:")
print(mapa_covid.columns)

print("\nMunicípios com dados COVID:")
print(mapa_covid["casos_covid"].count())

print("\nMunicípios sem dados COVID:")
print(mapa_covid["casos_covid"].isna().sum())

# ============================================================
# BLOCO 16 — MAPA COROPLÉTICO DOS CASOS COVID
# ============================================================
#
# Objetivo:
# Representar espacialmente o número de casos COVID-19
# por município em 26/10/2020.
#
# Fonte dos dados COVID:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
#
# Fonte geográfica:
# Direção-Geral do Território — CAOP 2025
# https://www.dgterritorio.gov.pt/
#
# Visualização:
# GeoPandas + Matplotlib
# ============================================================

fig, ax = plt.subplots(figsize=(12, 10))

mapa_covid.plot(
    column="casos_covid",
    ax=ax,
    cmap="Greens",
    edgecolor="black",
    linewidth=0.3,
    legend=True,
    missing_kwds={
        "color": "lightgrey",
        "edgecolor": "black",
        "label": "Sem dados"
    }
)

ax.set_title(
    "Casos COVID-19 por Município — 26/10/2020",
    fontsize=15
)

ax.axis("off")

plt.show()

# ============================================================
# BLOCO 17 — PREPARAÇÃO PARA O MAPA INTERATIVO
# ============================================================
#
# Objetivo:
# Preparar a GeoDataFrame para utilização com Folium.
#
# O Folium utiliza coordenadas geográficas em WGS84 (EPSG:4326).
#
# Fonte geográfica:
# Direção-Geral do Território — CAOP 2025
# https://www.dgterritorio.gov.pt/
#
# Fonte dos dados COVID:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
# ============================================================

mapa_interativo = mapa_covid.to_crs(epsg=4326)

print("\nCRS original:")
print(mapa_covid.crs)

print("\nCRS para o mapa interativo:")
print(mapa_interativo.crs)

# ============================================================
# BLOCO 18 — MAPA INTERATIVO COM FOLIUM
# ============================================================

import folium

mapa_folium = folium.Map(
    location=[39.6, -8.0],
    zoom_start=7,
    tiles=None
)

# Mapa-base Esri
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/"
          "World_Street_Map/MapServer/tile/{z}/{y}/{x}",
    attr="Esri, HERE, Garmin, © OpenStreetMap contributors, "
         "and the GIS user community",
    name="Esri World Street Map",
    overlay=False,
    control=True
).add_to(mapa_folium)

print("\nMapa interativo criado com sucesso.")

# ============================================================
# BLOCO 19 — CAMADA INTERATIVA DOS MUNICÍPIOS
# ============================================================

folium.GeoJson(
    mapa_interativo,
    name="Municípios",
    tooltip=folium.GeoJsonTooltip(
        fields=["municipio", "casos_covid"],
        aliases=["Município:", "Casos COVID:"],
        localize=True,
        sticky=False
    )
).add_to(mapa_folium)

# Guardar o mapa como HTML
ficheiro_mapa = (
    r"C:\Users\silva\Desktop\Projeto_Covid_Portugal"
    r"\mapa_covid_interativo.html"
)

mapa_folium.save(ficheiro_mapa)

print("\nMapa interativo guardado em:")
print(ficheiro_mapa)

import webbrowser

webbrowser.open(ficheiro_mapa)

print("\nMapa interativo guardado e aberto no navegador.")

# ============================================================
# BLOCO 20 — MAPA COROPLÉTICO INTERATIVO
# ============================================================
#
# Objetivo:
# Representar a distribuição espacial dos casos COVID-19
# por município em 26/10/2020.
#
# A intensidade da cor representa o número de casos.
#
# Fonte dos dados COVID:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
#
# Fonte geográfica:
# Direção-Geral do Território — CAOP 2025
# https://www.dgterritorio.gov.pt/
#
# Ferramentas:
# GeoPandas + Folium
# ============================================================

import folium
import branca.colormap as cm
import pandas as pd


# ------------------------------------------------------------
# 1. Criar mapa sem mapa-base
# ------------------------------------------------------------

mapa_folium = folium.Map(
    location=[39.6, -8.0],
    zoom_start=7,
    tiles=None
)


# ------------------------------------------------------------
# 2. Escala de cores
# ------------------------------------------------------------

max_casos = mapa_interativo["casos_covid"].max()

escala = cm.LinearColormap(
    colors=[
        "#E8F5E9",
        "#A5D6A7",
        "#66BB6A",
        "#388E3C",
        "#1B5E20"
    ],
    vmin=0,
    vmax=max_casos
)

escala.caption = "Casos COVID-19 por município — 26/10/2020"


# ------------------------------------------------------------
# 3. Estilo dos municípios
# ------------------------------------------------------------

def estilo_municipio(feature):

    valor = feature["properties"]["casos_covid"]

    # Municípios sem dados
    if pd.isna(valor):

        return {
            "fillColor": "#D9D9D9",
            "color": "#666666",
            "weight": 0.5,
            "fillOpacity": 0.8
        }

    # Municípios com dados
    return {
        "fillColor": escala(float(valor)),
        "color": "#444444",
        "weight": 0.5,
        "fillOpacity": 0.85
    }


# ------------------------------------------------------------
# 4. Adicionar municípios
# ------------------------------------------------------------

folium.GeoJson(
    mapa_interativo,
    name="Casos COVID",
    style_function=estilo_municipio,

    tooltip=folium.GeoJsonTooltip(
        fields=[
            "municipio",
            "casos_covid"
        ],

        aliases=[
            "Município:",
            "Casos COVID:"
        ],

        localize=True,
        sticky=False
    )
).add_to(mapa_folium)


# ------------------------------------------------------------
# 5. Adicionar legenda
# ------------------------------------------------------------

escala.add_to(mapa_folium)


# ------------------------------------------------------------
# 6. Guardar mapa
# ------------------------------------------------------------

mapa_folium.save(ficheiro_mapa)

print("\nMapa coroplético interativo criado.")

ficheiro_mapa = (
    r"C:\Users\silva\Desktop\Projeto_Covid_Portugal"
    r"\mapa_covid_interativo_v2.html"
)

mapa_folium.save(ficheiro_mapa)

print("\nNovo mapa guardado em:")
print(ficheiro_mapa)

# ============================================================
# BLOCO 21 — MAPA INTERATIVO POR CLASSES DE CASOS
# ============================================================

import folium
import pandas as pd

# ------------------------------------------------------------
# Criar novo mapa
# ------------------------------------------------------------

mapa_covid_interativo = folium.Map(
    location=[39.6, -8.0],
    zoom_start=7,
    tiles=None
)

# ------------------------------------------------------------
# Mapa-base Esri
# ------------------------------------------------------------

folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/"
          "Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
    attr="Esri, HERE, Garmin, © OpenStreetMap contributors, "
         "and the GIS user community",
    name="Mapa-base",
    overlay=False,
    control=True
).add_to(mapa_covid_interativo)


# ------------------------------------------------------------
# Função de classificação
# ------------------------------------------------------------

def obter_cor(valor):

    if pd.isna(valor):
        return "#D9D9D9"

    if valor <= 25:
        return "#E8F5E9"

    elif valor <= 50:
        return "#A5D6A7"

    elif valor <= 100:
        return "#66BB6A"

    elif valor <= 250:
        return "#388E3C"

    else:
        return "#1B5E20"


# ------------------------------------------------------------
# Estilo dos municípios
# ------------------------------------------------------------

def estilo_covid(feature):

    valor = feature["properties"]["casos_covid"]

    return {
        "fillColor": obter_cor(valor),
        "color": "#555555",
        "weight": 0.5,
        "fillOpacity": 0.85
    }


# ------------------------------------------------------------
# Adicionar municípios
# ------------------------------------------------------------

folium.GeoJson(
    mapa_interativo,
    name="Casos COVID",

    style_function=estilo_covid,

    tooltip=folium.GeoJsonTooltip(
        fields=[
            "municipio",
            "casos_covid"
        ],
        aliases=[
            "Município:",
            "Casos COVID:"
        ],
        localize=True,
        sticky=False
    )
).add_to(mapa_covid_interativo)


# ------------------------------------------------------------
# Legenda
# ------------------------------------------------------------

legenda = """
<div style="
position: fixed;
bottom: 30px;
left: 30px;
width: 190px;
background-color: white;
border: 2px solid grey;
z-index: 9999;
padding: 10px;
font-size: 13px;
">

<b>Casos COVID — 26/10/2020</b><br><br>

<i style="background:#E8F5E9;
width:18px;height:18px;display:inline-block"></i>
0–25<br>

<i style="background:#A5D6A7;
width:18px;height:18px;display:inline-block"></i>
26–50<br>

<i style="background:#66BB6A;
width:18px;height:18px;display:inline-block"></i>
51–100<br>

<i style="background:#388E3C;
width:18px;height:18px;display:inline-block"></i>
101–250<br>

<i style="background:#1B5E20;
width:18px;height:18px;display:inline-block"></i>
>250<br>

<i style="background:#D9D9D9;
width:18px;height:18px;display:inline-block"></i>
Sem dados

</div>
"""

mapa_covid_interativo.get_root().html.add_child(
    folium.Element(legenda)
)


# ------------------------------------------------------------
# Guardar
# ------------------------------------------------------------

ficheiro_mapa = (
    r"C:\Users\silva\Desktop\Projeto_Covid_Portugal"
    r"\mapa_covid_classes.html"
)

mapa_covid_interativo.save(ficheiro_mapa)

print("\nMapa por classes criado:")
print(ficheiro_mapa)

print("\nMapa criado.")
print("Ficheiro:", ficheiro_mapa)

# ============================================================
# BLOCO 22 — POPUP INTERATIVO DOS MUNICÍPIOS
# ============================================================
#
# Objetivo:
# Adicionar um popup ao clicar em cada município,
# apresentando informação detalhada sobre os casos COVID.
#
# Fonte dos dados COVID:
# DSSG Portugal — COVID-19 Portugal Data
# https://github.com/dssg-pt/covid19pt-data
#
# Fonte geográfica:
# Direção-Geral do Território — CAOP 2025
# https://www.dgterritorio.gov.pt/
#
# Ferramentas:
# GeoPandas + Folium
# ============================================================

def criar_popup(feature):

    municipio = feature["properties"]["municipio"]
    casos = feature["properties"]["casos_covid"]

    if pd.isna(casos):
        casos_texto = "Sem dados"
    else:
        casos_texto = f"{int(casos):,}".replace(",", ".")

    html = f"""
    <div style="font-family: Arial; width: 180px;">

        <h4 style="margin-bottom: 8px;">
            {municipio}
        </h4>

        <b>Casos COVID:</b> {casos_texto}<br>

        <b>Data:</b> 26/10/2020

    </div>
    """

    return folium.Popup(
        html,
        max_width=250
    )


# Adicionar popup ao mapa
folium.GeoJson(
    mapa_interativo,
    name="Informação por município",

    style_function=estilo_covid,

    tooltip=folium.GeoJsonTooltip(
        fields=["municipio", "casos_covid"],
        aliases=["Município:", "Casos COVID:"],
        localize=True,
        sticky=False
    ),

    popup=folium.GeoJsonPopup(
        fields=["municipio", "casos_covid"],
        aliases=["Município:", "Casos COVID:"],
        localize=True,
        labels=True
    )
).add_to(mapa_covid_interativo)


# Guardar nova versão

ficheiro_popup = (
    r"C:\Users\silva\Desktop\Projeto_Covid_Portugal"
    r"\mapa_covid_popup.html"
)

mapa_covid_interativo.save(ficheiro_popup)

print("\nMapa final guardado em:")
print(ficheiro_popup)

import webbrowser

webbrowser.open_new_tab(
    "file:///" + ficheiro_popup.replace("\\", "/")
)

# ============================================================
# BLOCO 23 — PREPARAÇÃO DO MAPA PARA O DASH
# ============================================================
#
# Objetivo:
# Guardar o mapa Folium na pasta assets do projeto,
# para posterior integração no Dashboard Dash.
#
# O ficheiro HTML será incorporado no 06_dashboard.py.
# ============================================================

import os

# Pasta assets do projeto
pasta_assets = (
    r"C:\Users\silva\Desktop\Projeto_Covid_Portugal"
    r"\assets"
)

# Criar a pasta caso ainda não exista
os.makedirs(pasta_assets, exist_ok=True)

# Caminho final do mapa
ficheiro_dash = os.path.join(
    pasta_assets,
    "mapa_covid_interativo.html"
)

# Guardar o mapa
mapa_covid_interativo.save(ficheiro_dash)

print("\nMapa preparado para o Dashboard.")
print("Local:")
print(ficheiro_dash)

