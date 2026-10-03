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

### ⧉ Variáveis principais

O dataset final utilizado na análise temporal integra:

```text
data_semana
excesso_cumulativo_por_milhao
mortes_covid
cobertura_vacinal

---

## ⇢ O TRATAMENTO

Antes da análise, os diferentes conjuntos de dados passaram por um
processo de preparação e transformação em Python.

O objetivo foi garantir que os dados utilizados nas análises fossem
consistentes, comparáveis e adequados à construção das visualizações.

### ⇢ Principais etapas

### ⇢ Do dado à análise

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

Com os dados preparados, foi realizada uma análise exploratória e
estatística dos principais indicadores.

O objetivo foi compreender a distribuição dos dados, a sua evolução
ao longo do tempo e as relações observadas entre diferentes
variáveis.

### ∿ Estatística descritiva

Foram calculados diferentes indicadores estatísticos, incluindo:

- média;
- mediana;
- mínimo e máximo;
- desvio-padrão;
- quartis;
- intervalo interquartil (IQR);
- assimetria;
- coeficiente de variação.


### ⌁ Evolução temporal

A análise temporal permitiu observar a evolução semanal de:

- excesso de mortalidade;
- mortes por COVID-19;
- cobertura vacinal.

A representação gráfica dos indicadores permite identificar períodos
de alteração, crescimento, redução e estabilização.

### ⟷ Relações entre indicadores

Foi também analisada a correlação entre os principais indicadores.

A matriz de correlação permite observar associações estatísticas entre
as variáveis analisadas.

> **Correlação não significa causalidade.**

As associações observadas devem ser interpretadas no contexto de uma
análise observacional e não permitem, isoladamente, determinar que
uma variável tenha provocado alterações noutra.
Os dados têm sua própria linguagem, falam por si.

### ∿ Análise das causas de morte

Os dados da PORDATA permitiram complementar a análise temporal através
da comparação de diferentes causas de morte entre 2020 e 2024.

Foram consideradas, entre outras:

- doenças do aparelho circulatório;
- tumores malignos;
- diabetes;
- COVID-19;
- doenças respiratórias;
- doenças do aparelho digestivo;
- suicídio;
- tuberculose;
- SIDA.

Esta análise permite observar alterações nos padrões de mortalidade
ao longo do período estudado.

---

## ⟷ AS RELAÇÕES

Foi explorada a relação entre os principais indicadores através de
uma matriz de correlação.

**Indicadores analisados**

`Excesso de mortalidade` · `Mortes por COVID-19` · `Cobertura vacinal`

Os resultados são interpretados como associações observadas nos dados,
podendo contribuir para futuras investigações.

---

## ⌖ O TERRITÓRIO

A componente geográfica foi desenvolvida com **GeoPandas** e **Folium**,
permitindo representar indicadores por município.

**278 municípios do Continente**

→ Casos de COVID-19  
→ Causas de morte — 2024

---

## ▦ A VISUALIZAÇÃO

O projeto reúne os resultados num **dashboard interativo desenvolvido
em Python, Dash e Plotly**.

Inclui:

`Evolução temporal` · `Vacinação` · `Mortalidade` · `Causas de morte`
· `Correlação` · `Mapas`

---

## ◇ RESULTADOS

A análise permite observar alterações nos indicadores de mortalidade
ao longo do período estudado e identificar padrões que merecem
investigação adicional.

> **Os dados mostram padrões. A investigação procura compreender as razões.**

---

## ⟐ REFLEXÃO FINAL

Os resultados são de natureza observacional, o trabalho não tem como objetivo afirmar
nenhuma causa além do que os dados já o dizem. 
O projeto procura identificar sinais, padrões e questões que possam
orientar análises futuras.

