# 🧬 INDICADORES PÓS-PANDEMIA
## Uma Análise Após 5 Anos

<p align="center">
  <strong>Uma análise exploratória dos principais indicadores de saúde e mortalidade em Portugal, cinco anos após o período pandémico.</strong>
</p>

---

## 🔬 Sobre o projeto

Cinco anos após o início da pandemia, este projeto procura observar
**o que aconteceu com alguns dos principais indicadores de saúde e
mortalidade em Portugal.**

A análise integra diferentes fontes de dados e utiliza técnicas de
tratamento, análise estatística, visualização e geoprocessamento para
explorar a evolução desses indicadores.

### 🎯 Pergunta de investigação

> **Após cinco anos do início da pandemia, que alterações podem ser
> observadas nos principais indicadores de saúde e mortalidade em Portugal?**

---

## ◈ O QUE ESTE PROJETO PROCURA?

### ◈ Questão central

> **Após cinco anos do início da pandemia, que alterações podem ser
> observadas nos principais indicadores de saúde e mortalidade em Portugal?**

### ◈ Objetivo

Analisar a evolução de diferentes indicadores de saúde e mortalidade
em Portugal no período pós-pandemia, procurando identificar padrões,
alterações e associações que possam contribuir para futuras
investigações.

### ◈ O que será observado?

- ⌁ Evolução do excesso de mortalidade;
- ⌁ Evolução das mortes por COVID-19;
- ⌁ Evolução da cobertura vacinal;
- ⌁ Alterações nas principais causas de morte;
- ⌁ Indicadores relacionados com Saúde Mental;
- ⟷ Associações entre os principais indicadores;
- ⌖ Diferenças entre municípios;
- ▦ Visualização integrada dos resultados.

> **Observar → analisar → questionar → investigar.**
>
> ⧉ OS DADOS
      ↓
⇢ O TRATAMENTO
      ↓
∿ A ANÁLISE
      ↓
⟷ AS RELAÇÕES
      ↓
⌖ O TERRITÓRIO
      ↓
▦ A VISUALIZAÇÃO
      ↓
◇ OS RESULTADOS
      ↓
⟐ A REFLEXÃO FINAL
>
> ---

## ⧉ OS DADOS

A análise foi construída a partir da integração de diferentes fontes
de dados públicos, permitindo observar o período pós-pandemia a partir
de várias dimensões.

### ⧉ Principais fontes

| Fonte | Informação utilizada |
|---|---|
| **Our World in Data** | Excesso de mortalidade e cobertura vacinal |
| **PORDATA** | Mortalidade por diferentes causas |
| **INE** | Informação estatística complementar |
| **CAOP 2025** | Informação geográfica dos municípios |

### ⌁ Períodos analisados

**2020–2023**  
Evolução semanal do excesso de mortalidade, mortes por COVID-19 e
cobertura vacinal.

**2020–2024**  
Evolução das principais causas de morte através dos dados da PORDATA.

**2020**  
**26 de outubro de 2020** — análise geográfica dos casos de COVID-19
por município.

**2024**  
Análise geográfica de causas de morte por município.

## ⧉ DATASET FINAL

O dataset final utilizado na análise temporal apresenta:

**208 observações · 4 variáveis · 2020-01-06 → 2023-12-25**

### ⧉ Variáveis principais

`data_semana` · `excesso_cumulativo_por_milhao` · `mortes_covid` · `cobertura_vacinal`

---

## ⇢ O TRATAMENTO

Antes da análise, os diferentes conjuntos de dados passaram por um processo de preparação e transformação em Python.

### ⇢ Principais etapas

**⧉ Dados originais**  
↓  
**⌕ Inspeção e compreensão**  
↓  
**⟿ Limpeza**  
↓  
**◇ Transformação**  
↓  
**⟷ Integração**  
↓  
**✓ Validação**  
↓  
**◈ Dados preparados para análise**

---

## ∿ A ANÁLISE

Foram utilizadas técnicas de estatística descritiva e análise exploratória para compreender a distribuição 
e evolução dos indicadores.

**Medidas utilizadas:**  
`Média` · `Mediana` · `Mínimo` · `Máximo` · `Desvio-padrão` · `Quartis` · `IQR` · `Assimetria` · `Coeficiente de variação`

### ⌁ Evolução temporal

Análise da evolução do excesso de mortalidade, mortes por COVID-19 e cobertura vacinal.

### ⟷ Relações entre indicadores

Foi explorada a correlação entre os principais indicadores.

> **Correlação não significa causalidade.**

### ∿ Causas de morte

Os dados da PORDATA permitiram comparar diferentes causas de morte entre **2020 e 2024**.

---

## ⌖ O TERRITÓRIO

A componente geográfica foi desenvolvida com **GeoPandas** e **Folium**.

**278 municípios do Continente**

`Casos de COVID-19` · `Causas de morte — 2024`

---

## ▦ A VISUALIZAÇÃO

Os resultados foram integrados num **dashboard interativo desenvolvido em Python, Dash e Plotly**.

`Evolução temporal` · `Vacinação` · `Mortalidade` · `Causas de morte` · `Correlação` · `Mapas`

---

## ◇ RESULTADOS

A análise permite observar alterações nos indicadores de mortalidade ao longo do período estudado e 
identificar padrões que merecem investigação adicional.

> **Os dados mostram padrões. A investigação procura compreender as razões.**

---

## ⟐ REFLEXÃO FINAL

Os resultados são de natureza observacional. O trabalho não tem como objetivo estabelecer relações causais além do que 
os dados permitem observar.
O projeto procura identificar sinais, padrões e questões que possam orientar análises futuras.

---

## ⌘ TECNOLOGIAS

`Python` · `Pandas` · `NumPy` · `Matplotlib` · `Plotly` · `GeoPandas` · `Folium` · `Dash`

### ⌘ Desenvolvimento

`Python` · `Jupyter / Spyder`

### ⌘ Visualização

`Plotly` · `Matplotlib` · `Folium` · `Dash`

### ⌘ Análise geográfica

`GeoPandas` · `CAOP 2025`

---

## § FONTES

- **Our World in Data** — dados de excesso de mortalidade e COVID-19  
  https://ourworldindata.org/explorers/covid

- **PORDATA** — mortalidade por causas de morte em Portugal  
  https://www.pordata.pt/portugal/obitos+de+residentes+em+portugal+por+algumas+causas-156

- **Instituto Nacional de Estatística (INE)** — estatísticas oficiais de mortalidade  
  https://www.ine.pt/

- **Direção-Geral do Território (DGT)** — CAOP 2025  
  https://www.dgterritorio.gov.pt/carta-administrativa-oficial-de-portugal-caop-2025

  ---

**◈ Projeto desenvolvido em Python · Portugal**
---

<p align="left">
  <sub>
    No âmbito da UFCD 10809 — Visualização de Dados em Python<br>
    Prof. Albano Afonso · ETacademy
  </sub>
</p>
