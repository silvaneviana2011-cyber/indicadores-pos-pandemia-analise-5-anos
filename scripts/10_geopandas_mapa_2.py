# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 21:44:56 2026

@author: silva
"""

# ============================================================
# BLOCO 1 — IMPORTAÇÕES
# ============================================================

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
import webbrowser

# ============================================================
# BLOCO 2 — CARREGAR CAOP 2025
# ============================================================
#
# Fonte geográfica:
# CAOP 2025 — Direção-Geral do Território (DGT)
#
# Base geográfica utilizada no Mapa 1 e no Mapa 2.
# ============================================================

ficheiro_caop = (
    r"C:\Users\silva\Desktop\Projeto_Covid_Portugal"
    r"\04_geopandas\Continente_CAOP2025.gpkg"
)

mapa = gpd.read_file(ficheiro_caop)

print("Dimensão:")
print(mapa.shape)

print("\nColunas:")
print(mapa.columns)

print("\nSistema de Coordenadas:")
print(mapa.crs)

# ============================================================
# BLOCO 3 — EXPLORAÇÃO DOS DADOS PORDATA
# ============================================================
#
# Fonte:
# PORDATA — Óbitos de residentes em Portugal
# por algumas causas de morte
#
# Causa selecionada:
# Acidentes, envenenamentos e violências
# ============================================================

ficheiro_pordata = (
    r"C:\Users\silva\Desktop\Projeto_Covid_Portugal"
    r"\04_geopandas\pordata.xlsx"
)

pordata = pd.read_excel(ficheiro_pordata)

print("Dimensão:")
print(pordata.shape)

print("\nColunas:")
print(pordata.columns)

print("\nPrimeiros registos:")
print(pordata.head())

print("\nTipos de dados:")
print(pordata.dtypes)

# ============================================================
# BLOCO 4 — LOCALIZAR A ESTRUTURA REAL DO EXCEL
# ============================================================

# Número de células preenchidas por linha
preenchidas_linha = pordata.notna().sum(axis=1)

print("Células preenchidas por linha:")
print(preenchidas_linha.head(30))

print("\nLinhas com informação:")
print(
    pordata.loc[
        preenchidas_linha > 0
    ].head(20).to_string()
)

# ============================================================
# BLOCO 5 — IDENTIFICAR CABEÇALHOS E MUNICÍPIOS
# ============================================================

# Mostrar apenas as primeiras 10 colunas
print("Primeiras 10 colunas:")
print(pordata.iloc[:, :10].to_string())

print("\n--------------------------------------------")
print("Primeiros valores da primeira coluna:")
print(pordata.iloc[:20, 0].to_string())

print("\n--------------------------------------------")
print("Primeiros valores da segunda coluna:")
print(pordata.iloc[:20, 1].to_string())

# ============================================================
# BLOCO 6 — INSPEÇÃO DOS CABEÇALHOS PORDATA
# ============================================================

print("Número de colunas:", len(pordata.columns))

print("\nNomes das primeiras 40 colunas:")
for i, coluna in enumerate(pordata.columns[:40]):
    print(i, "->", repr(coluna))

print("\n--------------------------------------------")

print("Primeira linha do Excel:")
for i, valor in enumerate(pordata.iloc[0, :40]):
    print(i, "->", repr(valor))
    
# ============================================================
# BLOCO 7 — LOCALIZAR O CABEÇALHO DOS INDICADORES
# ============================================================

# Mostrar as linhas 5 a 15 apenas das primeiras 30 colunas
print(
    pordata.iloc[5:16, :30].to_string(
        index=True,
        header=True
    )
) 

# ============================================================
# BLOCO 8 — LOCALIZAR A CAUSA "ACIDENTES, ENVENENAMENTOS
# E VIOLÊNCIAS"
# ============================================================

linha_causas = pordata.iloc[8]

print("Colunas onde aparece 'Acidentes':")

for i, valor in enumerate(linha_causas):
    if pd.notna(valor) and "Acidente" in str(valor):
        print(i, "->", valor)
        
# ============================================================
# BLOCO 8 — LOCALIZAR A CAUSA DE MORTE
# ============================================================

termo = "acidente"

print("Ocorrências de 'acidente' no ficheiro:")

for linha in range(pordata.shape[0]):
    for coluna in range(pordata.shape[1]):

        valor = pordata.iloc[linha, coluna]

        if pd.notna(valor) and termo in str(valor).lower():
            print(
                f"Linha: {linha} | "
                f"Coluna: {coluna} | "
                f"Valor: {repr(valor)}"
            )
            
termo = "viol"

print("\nOcorrências de 'viol' no ficheiro:")

for linha in range(pordata.shape[0]):
    for coluna in range(pordata.shape[1]):

        valor = pordata.iloc[linha, coluna]

        if pd.notna(valor) and termo in str(valor).lower():
            print(
                f"Linha: {linha} | "
                f"Coluna: {coluna} | "
                f"Valor: {repr(valor)}"
            )
            

# ============================================================
# BLOCO 9 — IDENTIFICAR AS CAUSAS E POSIÇÕES DAS COLUNAS
# ============================================================

print("\n" + "=" * 70)
print("BLOCO 9 — CAUSAS DE MORTE E POSIÇÕES DAS COLUNAS")
print("=" * 70)

print("\nLinha identificada como linha de causas:")
print(linha_causas)

print("\nNúmero de elementos na linha de causas:")
print(len(linha_causas))

print("\nConteúdo da linha de causas:")

for i, valor in enumerate(linha_causas):
    print(f"{i:03d} -> {valor}")
    

# ------------------------------------------------------------
# Identificar posições das principais causas
# ------------------------------------------------------------

causas_mapa = [
    "Diabetes",
    "Tumores malignos",
    "Doenças do aparelho circulatório",
    "Suicídio",
    "Tuberculose",
    "Doenças do aparelho respiratório",
    "SIDA",
    "Doenças do aparelho digestivo"
]

print("\nPosições das causas selecionadas:")

for causa in causas_mapa:
    posicoes = linha_causas[linha_causas == causa].index.tolist()
    print(f"{causa} -> {posicoes}")

# ------------------------------------------------------------
# Dicionário: causa -> coluna correspondente
# ------------------------------------------------------------

colunas_causas = {
    "Diabetes": "Unnamed: 2",
    "Tumores malignos": "Unnamed: 8",
    "Doenças do aparelho circulatório": "Unnamed: 14",
    "Suicídio": "Unnamed: 20",
    "Tuberculose": "Unnamed: 26",
    "Doenças do aparelho respiratório": "Unnamed: 32",
    "SIDA": "Unnamed: 38",
    "Doenças do aparelho digestivo": "Unnamed: 44"
}

print("\nDicionário final das causas:")
for causa, coluna in colunas_causas.items():
    print(f"{causa} -> {coluna}")
    
# ============================================================
# BLOCO 10 — LOCALIZAR OS DADOS DOS TERRITÓRIOS
# ============================================================

print("\n" + "=" * 70)
print("BLOCO 10 — LOCALIZAR OS DADOS DOS TERRITÓRIOS")
print("=" * 70)

print("\nPrimeiras 40 linhas do PORDATA:")

print(pordata.iloc[:40, :10].to_string())

# ============================================================
# BLOCO 11 — MUNICÍPIOS E DIABETES EM 2024
# ============================================================

print("\n" + "=" * 70)
print("BLOCO 11 — MUNICÍPIOS E DIABETES EM 2024")
print("=" * 70)

# Selecionar apenas os municípios
dados_municipios = pordata[
    pordata["Unnamed: 0"] == "Município"
].copy()

# Nome do município
dados_municipios["Municipio"] = dados_municipios["Unnamed: 1"]

# Diabetes — 2024

dados_municipios["Diabetes_2024"] = dados_municipios["Unnamed: 7"]

print("\nPrimeiros municípios:")
print(
    dados_municipios[
        ["Municipio", "Diabetes_2024"]
    ].head(10).to_string(index=False)
)

# ============================================================
# VERIFICAR AS COLUNAS DOS ANOS
# ============================================================

print("\nPosições e nomes das primeiras 15 colunas:")

for i, coluna in enumerate(pordata.columns[:15]):
    print(f"{i:02d} -> {coluna}")

# ============================================================
# BLOCO 12 — CAUSAS DE MORTE POR MUNICÍPIO EM 2024
# ============================================================

print("\n" + "=" * 70)
print("BLOCO 12 — CAUSAS DE MORTE POR MUNICÍPIO EM 2024")
print("=" * 70)

# Colunas de 2024 para cada causa
colunas_2024 = {
    "Diabetes": "Unnamed: 7",
    "Tumores malignos": "Unnamed: 13",
    "Doenças do aparelho circulatório": "Unnamed: 19",
    "Suicídio": "Unnamed: 25",
    "Tuberculose": "Unnamed: 31",
    "Doenças do aparelho respiratório": "Unnamed: 37",
    "SIDA": "Unnamed: 43",
    "Doenças do aparelho digestivo": "Unnamed: 49"
}

# Extrair os valores
for causa, coluna in colunas_2024.items():
    dados_municipios[causa] = pd.to_numeric(
        dados_municipios[coluna],
        errors="coerce"
    )

print("\nDados extraídos:")
print(
    dados_municipios[
        ["Municipio"] + list(colunas_2024.keys())
    ].head(10).to_string(index=False)
)

# ============================================================
# IDENTIFICAR CAUSAS ESPECÍFICAS DE INTERESSE
# ============================================================

print("\n" + "=" * 70)
print("CAUSAS ESPECÍFICAS PARA O MAPA 2")
print("=" * 70)

termos_interesse = [
    "viol",
    "parasit",
    "suicid",
    "acident",
    "homicid",
    "extern"
]

for termo in termos_interesse:
    print(f"\nCausas relacionadas com '{termo}':")

    for i, valor in enumerate(linha_causas):
        if pd.notna(valor) and termo.lower() in str(valor).lower():
            print(f"{i:03d} -> {valor}")  

# ============================================================
# BLOCO 13 — COLUNAS DA CAOP
# ============================================================

print("\n" + "=" * 70)
print("BLOCO 13 — COLUNAS DA CAOP")
print("=" * 70)

print("\nColunas disponíveis na CAOP:")
print(mapa.columns.tolist())

print("\nDimensão da CAOP:")
print(mapa.shape)

# ============================================================
# BLOCO 14 — VERIFICAR MUNICÍPIOS DA CAOP
# ============================================================

print("\n" + "=" * 70)
print("BLOCO 14 — VERIFICAÇÃO DOS MUNICÍPIOS")
print("=" * 70)

print("\nNúmero de municípios distintos na CAOP:")
print(mapa["municipio"].nunique())

print("\nPrimeiros municípios da CAOP:")
print(
    mapa["municipio"]
    .drop_duplicates()
    .head(20)
    .to_string(index=False)
)

# ============================================================
# BLOCO 15 — JUNTAR PORDATA À CAOP
# ============================================================

# ============================================================
# 🟡 APRENDIZAGEM — IMPORTANTE
# Aqui depois de filtrar linhas e colunas, diante das dimensões 
# como 3392 (linhas, colunas + ou -)  para encontrar 13 variáveis
# usamos o "merge". Assim vai unir a informação de um Dataframe
# a outro Datafraame. Like as --> Município.
# ============================================================

print("\n" + "=" * 70)
print("BLOCO 15 — JUNÇÃO PORDATA + CAOP")
print("=" * 70)

mapa_causas = mapa.merge(
    dados_municipios,
    left_on="municipio",
    right_on="Municipio",
    how="left"
)

print("\nDimensão após a junção:")
print(mapa_causas.shape)

print("\nColunas das causas:")
print(
    mapa_causas[
        [
            "municipio",
            "Diabetes",
            "Tumores malignos",
            "Doenças do aparelho circulatório",
            "Suicídio",
            "Tuberculose",
            "Doenças do aparelho respiratório",
            "SIDA",
            "Doenças do aparelho digestivo"
        ]
    ].head(10).to_string(index=False)
)

# ============================================================
# 🟡 APRENDIZAGEM — IMPORTANTE
# APRENDIZAGEM: depois do merge, dissolvemos as geometrias
# para obter uma única geometria por município
# Like as garimpo
# ============================================================

# ============================================================
# BLOCO 16 — DISSOLVER GEOMETRIAS POR MUNICÍPIO
# ============================================================

print("\n" + "=" * 70)
print("BLOCO 16 — DISSOLVER POR MUNICÍPIO")
print("=" * 70)

mapa_municipios = mapa_causas.dissolve(
    by="municipio",
    aggfunc="first"
).reset_index()

print("\nDimensão após dissolver:")
print(mapa_municipios.shape)

print("\nNúmero de municípios:")
print(mapa_municipios["municipio"].nunique())

print("\nPrimeiros municípios:")
print(
    mapa_municipios[
        [
            "municipio",
            "Diabetes",
            "Tumores malignos",
            "Doenças do aparelho circulatório"
        ]
    ].head(10).to_string(index=False)
)

# ============================================================
# 🟡 APRENDIZAGEM IMPORTANTE
# Um mapa Folium pode funcionar sem um mapa-base externo.
# Neste caso, usamos diretamente as geometrias da CAOP,
# evitando dependências de APIs ou serviços externos.
# ============================================================

# ============================================================
# BLOCO 17 — MAPA INTERATIVO
# ============================================================

mapa_interativo = folium.Map(
    location=[39.5, -8.0],
    zoom_start=7,
    tiles=None
)

print("\nMapa base criado com sucesso.")

# ============================================================
# 🟡 APRENDIZAGEM IMPORTANTE
# O Folium trabalha com coordenadas geográficas em EPSG:4326.
# Por isso, antes de criar o mapa, devemos converter a
# geometria da CAOP para esse sistema de coordenadas.
# ============================================================

# ============================================================
# BLOCO 17A — CONVERTER CRS PARA FOLIUM
# ============================================================

print("\n" + "=" * 70)
print("BLOCO 17A — CONVERSÃO DO CRS")
print("=" * 70)

print("\nCRS atual:")
print(mapa_municipios.crs)

mapa_municipios = mapa_municipios.to_crs(epsg=4326)

print("\nCRS após conversão:")
print(mapa_municipios.crs)

# ============================================================
# BLOCO 18 — ADICIONAR MUNICÍPIOS AO MAPA
# ============================================================


folium.GeoJson(
    mapa_municipios.to_json(),
    name="Municípios",
    style_function=lambda feature: {
        "fillColor": "#6A5ACD",
        "color": "#333333",
        "weight": 0.5,
        "fillOpacity": 0.5
    }
).add_to(mapa_interativo)

print("Municípios adicionados ao mapa com sucesso.")

# ============================================================
# BLOCO 18A — AJUSTAR ENQUADRAMENTO DO MAPA
# ============================================================

limites = mapa_municipios.total_bounds

mapa_interativo.fit_bounds([
    [limites[1], limites[0]],
    [limites[3], limites[2]]
])

print("Enquadramento do mapa ajustado aos municípios.")

# ============================================================
# BLOCO 19 — MAPA TEMÁTICO: SUICÍDIO
# ============================================================



folium.Choropleth(
    geo_data=mapa_municipios.to_json(),
    data=mapa_municipios,
    columns=["municipio", "Suicídio"],
    key_on="feature.properties.municipio",
    fill_color="Purples",
    fill_opacity=0.7,
    line_opacity=0.3,
    legend_name="Número de suicídios — 2024"
).add_to(mapa_interativo)

print("Mapa temático de suicídio criado com sucesso.")

# ============================================================
# 🟡 APRENDIZAGEM IMPORTANTE
# Um mapa coroplético utiliza a intensidade da cor
# O GeoJsonTooltip permite mostrar informações dos atributos
# de cada município quando passamos o rato sobre a geometria.
# ============================================================
# O tooltip permite apresentar os dados associados a cada
# município diretamente sobre a geometria do mapa.
# ============================================================

# ============================================================
# BLOCO 20 — INFORMAÇÃO AO PASSAR O RATO
# ============================================================

folium.GeoJson(
    mapa_municipios.to_json(),
    name="Dados municipais",
    tooltip=folium.GeoJsonTooltip(
        fields=[
            "municipio",
            "Suicídio"
        ],
        aliases=[
            "Município:",
            "N.º de suicídios:"
        ],
        localize=True,
        sticky=False
    ),
    style_function=lambda feature: {
        "fillColor": "transparent",
        "color": "transparent",
        "weight": 0
    }
).add_to(mapa_interativo)

print("Informação interativa adicionada com sucesso.")

# ============================================================
# BLOCO 21 — TÍTULO E CONTROLO DO MAPA
# ============================================================

titulo = """
<div style="
    position: fixed;
    top: 5px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 9999;
    background-color: white;
    padding: 10px 20px;
    border: 2px solid #555555;
    border-radius: 8px;
    font-size: 15px;
    font-weight: bold;
">
    Mapa 2 — Suicídios por Município — 2024
</div>
"""

mapa_interativo.get_root().html.add_child(
    folium.Element(titulo)
)

folium.LayerControl().add_to(mapa_interativo)

print("Título e controlo do mapa adicionados com sucesso.")

# ============================================================
# BLOCO 22 — GUARDAR E ABRIR O MAPA 2
# ============================================================

# Importante fazer o import webbrowser

ficheiro_mapa_2 = "mapa_2_causas_morte_2024.html"

mapa_interativo.save(ficheiro_mapa_2)

print("\nMapa 2 guardado com sucesso:")
print(ficheiro_mapa_2)

webbrowser.open(ficheiro_mapa_2)

# ========================================================================
# Depois de algumas horas a corrigir bugs no mapa, ficou assim:
#PORDATA → identificação das causas → dados municipais → MERGE com CAOP
#  → DISSOLVE → EPSG:4326 → Folium → mapa interativo
# Depois de algumas horas a corrigir bugs no mapa
# ========================================================================

# ============================================================
# O Folium permite adicionar elementos HTML ao mapa,
# como títulos e textos informativos, tornando a visualização
# mais clara e adequada para apresentação.
# ============================================================

# ============================================================
# 🟡 APRENDIZAGEM IMPORTANTE
# Podemos indicar o caminho completo de uma pasta para guardar
# o ficheiro HTML diretamente no local onde o Dashboard Dash
# consegue acessá-lo através da pasta assets.
# ============================================================

# ============================================================
# BLOCO 23 — GUARDAR O MAPA 2 NA PASTA ASSETS
# ============================================================

ficheiro_mapa_2 = r"C:\Users\silva\Desktop\Projeto_Covid_Portugal\assets\mapa_2_causas_morte_2024.html"

mapa_interativo.save(ficheiro_mapa_2)

print("\nMapa 2 guardado com sucesso:")
print(ficheiro_mapa_2)

webbrowser.open(ficheiro_mapa_2)




