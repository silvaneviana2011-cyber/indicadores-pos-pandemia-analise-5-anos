# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:35:17 2026

@author: silva
"""

# -*- coding: utf-8 -*-
"""
PROJETO COVID-19 EM PORTUGAL
06 — DASHBOARD INTERATIVO
"""

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc


# ============================================================
# 1. CARREGAR DATASETS
# ============================================================

dataset = pd.read_csv(
    "03_dados_tratados/dataset_final_covid_portugal.csv"
)

dataset["data_semana"] = pd.to_datetime(
    dataset["data_semana"]
)

dataset = dataset.sort_values(
    "data_semana"
).reset_index(drop=True)


# PORDATA — causas de morte
pordata = pd.read_csv(
    "03_dados_tratados/obitos_pordata_2020_2024.csv"
)


# ============================================================
# 2. KPIs
# ============================================================

total_mortes = dataset["mortes_covid"].sum()

max_excesso = dataset[
    "excesso_cumulativo_por_milhao"
].max()

max_vacinacao = dataset[
    "cobertura_vacinal"
].max()


# ============================================================
# 3. GRÁFICO — MORTES COVID-19
# ============================================================

fig_covid = px.line(
    dataset,
    x="data_semana",
    y="mortes_covid",
    title="Evolução das mortes por COVID-19",
    labels={
        "data_semana": "Data",
        "mortes_covid": "Mortes por semana"
    }
)

fig_covid.update_layout(
    template="plotly_white",
    hovermode="x unified"
)


# ============================================================
# 4. GRÁFICO — COBERTURA VACINAL
# ============================================================

fig_vacinacao = px.line(
    dataset,
    x="data_semana",
    y="cobertura_vacinal",
    title="Evolução da cobertura vacinal",
    labels={
        "data_semana": "Data",
        "cobertura_vacinal": "Cobertura vacinal (%)"
    }
)

fig_vacinacao.update_layout(
    template="plotly_white",
    hovermode="x unified",
    yaxis=dict(range=[0, 100])
)


# ============================================================
# 5. GRÁFICO — EXCESSO CUMULATIVO
# ============================================================

fig_excesso = px.line(
    dataset,
    x="data_semana",
    y="excesso_cumulativo_por_milhao",
    title="Excesso cumulativo de mortalidade",
    labels={
        "data_semana": "Data",
        "excesso_cumulativo_por_milhao":
            "Excesso cumulativo por milhão"
    }
)

fig_excesso.update_layout(
    template="plotly_white",
    hovermode="x unified"
)


# ============================================================
# 6. PORDATA — PRINCIPAIS CAUSAS DE MORTE
# ============================================================

anos = pordata.iloc[:, 0]

circulatorio = pordata.iloc[:, 1]
tumores = pordata.iloc[:, 2]
respiratorio = pordata.iloc[:, 6]
covid_pordata = pordata.iloc[:, 11]


df_causas = pd.DataFrame({
    "Ano": anos,
    "Doenças circulatórias": circulatorio,
    "Tumores malignos": tumores,
    "Doenças respiratórias": respiratorio,
    "COVID-19": covid_pordata
})


df_causas_long = df_causas.melt(
    id_vars="Ano",
    var_name="Causa de morte",
    value_name="Óbitos"
)


# ============================================================
# 7. GRÁFICO — COVID VS OUTRAS CAUSAS
# ============================================================

fig_causas = px.line(
    df_causas_long,
    x="Ano",
    y="Óbitos",
    color="Causa de morte",
    markers=True,
    title="COVID-19 e principais causas de morte",
    labels={
        "Ano": "Ano",
        "Óbitos": "Número de óbitos",
        "Causa de morte": "Causa"
    }
)

fig_causas.update_layout(
    template="plotly_white",
    hovermode="x unified"
)

# ============================================================
# 8. APLICAÇÃO DASH
# ============================================================

app = Dash(__name__)
# ============================================================
# COMPARAÇÃO DAS CAUSAS DE MORTE — 2020 VS. 2024
# ============================================================

dados_2020 = pordata.iloc[0, 1:]
dados_2024 = pordata.iloc[-1, 1:]

df_comparacao = pd.DataFrame({
    "Causa de morte": dados_2020.index,
    "2020": dados_2020.values,
    "2024": dados_2024.values
})

df_comparacao["2020"] = pd.to_numeric(
    df_comparacao["2020"],
    errors="coerce"
)

df_comparacao["2024"] = pd.to_numeric(
    df_comparacao["2024"],
    errors="coerce"
)

df_comparacao = df_comparacao.dropna()

df_comparacao = df_comparacao.sort_values(
    "2024",
    ascending=True
)

df_comparacao_plot = df_comparacao.melt(
    id_vars="Causa de morte",
    value_vars=["2020", "2024"],
    var_name="Ano",
    value_name="Óbitos"
)

fig_comparacao = px.bar(
    df_comparacao_plot,
    x="Óbitos",
    y="Causa de morte",
    color="Ano",
    orientation="h",
    barmode="group",
    title="Comparação das causas de morte — Portugal, 2020 vs. 2024",
    labels={
        "Óbitos": "Número de óbitos",
        "Causa de morte": "",
        "Ano": ""
    },
    color_discrete_map={
        "2020": "#5B2C83",
        "2024": "#0FF1F5"
    }
)

fig_comparacao.update_layout(
    height=600,
    margin=dict(
        l=20,
        r=40,
        t=70,
        b=40
    ),
    plot_bgcolor="white",
    paper_bgcolor="white"
)


# ============================================================
# VARIAÇÃO PERCENTUAL DOS ÓBITOS — 2020 VS. 2024
# ============================================================

valores_2020 = pordata.iloc[0, 1:]
valores_2024 = pordata.iloc[-1, 1:]

valores_2020 = pd.to_numeric(
    valores_2020,
    errors="coerce"
)

valores_2024 = pd.to_numeric(
    valores_2024,
    errors="coerce"
)

variacao_percentual = (
    (valores_2024 - valores_2020)
    / valores_2020
) * 100

df_variacao = pd.DataFrame({
    "Causa de morte": valores_2020.index,
    "Variação (%)": variacao_percentual.values
})

df_variacao = df_variacao[
    df_variacao["Causa de morte"] != "COVID-19"
]

df_variacao = df_variacao.dropna()

df_variacao = df_variacao.sort_values(
    "Variação (%)",
    ascending=True
)

fig_variacao = px.bar(
    df_variacao,
    x="Variação (%)",
    y="Causa de morte",
    orientation="h",
    title="Variação percentual dos óbitos por causa — 2020–2024",
    labels={
        "Variação (%)": "Variação (%)",
        "Causa de morte": ""
    },
    text="Variação (%)"
)

fig_variacao.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside"
)

fig_variacao.update_layout(
    height=550,
    margin=dict(
        l=20,
        r=80,
        t=70,
        b=40
    ),
    plot_bgcolor="white",
    paper_bgcolor="white"
)

fig_variacao.add_vline(
    x=0,
    line_width=1
)


# ============================================================
# 9. LAYOUT
# ============================================================
app.layout = html.Div(
    [

        # ----------------------------------------------------
        # CABEÇALHO
        # ----------------------------------------------------

        html.Div(
            [
                html.Div(
                    [
                        html.H1(
                            "SAÚDE EM DADOS",
                            style={
                                "margin": "0",
                                "fontSize": "32px",
                                "fontWeight": "700",
                                "color": "#3326A8"
                            }
                        ),

                        html.P(
                            "COVID-19 EM PORTUGAL",
                            style={
                                "margin": "4px 0 0 0",
                                "fontSize": "16px",
                                "color": "#5B5B8A",
                                "letterSpacing": "1px"
                            }
                        )
                    ]
                ),

                html.Div(
                    [
                        html.P(
                            "No âmbito da UFCD - 10809",
                            style={
                                "margin": "0",
                                "fontSize": "17px",
                                "fontWeight": "600",
                                "color": "#3326A8"
                            }
                        ),

                        html.P(
                            "Visualização de dados em Python",
                            style={
                                "margin": "3px 0",
                                "fontSize": "17px",
                                "color": "#444477"
                            }
                        ),

                        html.P(
                            "Sob orientação do Prof. Albano Afonso – Etacademy",
                            style={
                                "margin": "0",
                                "fontSize": "17px",
                                "color": "#777799"
                            }
                        )
                    ],
                    style={
                        "textAlign": "right",
                        "paddingRight": "20px"
                    }
                )
            ],
            style={
                "display": "flex",
                "justifyContent": "space-between",
                "alignItems": "center",
                "padding": "30px",
                "margin": "25px 30px 15px 30px",
                "background": "linear-gradient(90deg, #F7F5FF 0%, #F0FDFF 100%)",
                "borderRadius": "20px",
                "boxShadow": "0 8px 25px rgba(51,38,168,0.10)"
            }
        ),
        
        # ----------------------------------------------------
        # ENQUADRAMENTO
        # ----------------------------------------------------

        html.Div(
            [
        html.H3(
            "ENQUADRAMENTO",
            style={
                "margin": "0 0 10px 0",
                "fontSize": "18px",
                "fontWeight": "700",
                "color": "#3326A8"
            }
        ),

        html.P(
            "Este Dashboard reúne análises da evolução das mortes por "
            "COVID-19, da cobertura vacinal e do excesso de mortalidade "
            "em Portugal, complementadas pela análise das principais "
            "causas de morte. O objetivo é contextualizar o impacto da "
            "pandemia na mortalidade e explorar a evolução destes "
            "indicadores através de dados estatísticos e visualizações "
            "interativas.",
            style={
                "margin": "0 0 8px 0",
                "fontSize": "14px",
                "lineHeight": "1.6",
                "color": "#444477"
            }
        ),

        html.P(
            "Período de referência: 2020–2024",
            style={
                "margin": "0 0 4px 0",
                "fontSize": "12px",
                "fontStyle": "italic",
                "color": "#777799"
            }
        ),

        html.P(
            "Fontes: INE · PORDATA · Our World in Data",
            style={
                "margin": "0",
                "fontSize": "12px",
                "fontStyle": "italic",
                "color": "#777799"
            }
        )
    ],
    style={
        "margin": "20px 30px 0 30px",
        "padding": "18px 24px",
        "backgroundColor": "#F8F7FF",
        "borderRadius": "16px",
        "borderLeft": "4px solid #12DADF",
        "boxShadow": "0 5px 18px rgba(51,38,168,0.06)"
    }
),
        
# ----------------------------------------------------
# VÍDEO DE APRESENTAÇÃO
# ----------------------------------------------------

html.Div(
    html.Video(
        src="/assets/video.mp4",
        controls=True,
        style={
            "width": "100%",
            "maxWidth": "800px",
            "height": "auto",
            "borderRadius": "18px"
        }
    ),
    style={
        "display": "flex",
        "justifyContent": "center",
        "margin": "20px 30px 30px 30px"
    }
),
        
        
            
           
            

        # ----------------------------------------------------
        # KPIs
        # ----------------------------------------------------

        html.Div(
            [

                html.Div(
                    [
                        html.P(
                            "TOTAL DE MORTES COVID-19",
                            style={
                                "margin": "0",
                                "fontSize": "13px",
                                "fontWeight": "600",
                                "color": "#777799"
                            }
                        ),

                        html.H2(
                            f"{total_mortes:,.0f}".replace(",", "."),
                            style={
                                "margin": "5px 0",
                                "fontSize": "30px",
                                "color": "#3326A8"
                            }
                        ),

                        html.P(
                            "mortes acumuladas",
                            style={
                                "margin": "0",
                                "fontSize": "12px",
                                "color": "#9999AA"
                            }
                        )
                    ],
                    style={
                        "flex": "1",
                        "padding": "20px",
                        "backgroundColor": "#FFFFFF",
                        "borderRadius": "18px",
                        "boxShadow":
                            "0 8px 25px rgba(51,38,168,0.12)"
                    }
                ),


                html.Div(
                    [
                        html.P(
                            "MÁXIMO DO EXCESSO CUMULATIVO",
                            style={
                                "margin": "0",
                                "fontSize": "13px",
                                "fontWeight": "600",
                                "color": "#777799"
                            }
                        ),

                        html.H2(
                            f"{max_excesso:,.0f}".replace(",", "."),
                            style={
                                "margin": "5px 0",
                                "fontSize": "30px",
                                "color": "#35C9A5"
                            }
                        ),

                        html.P(
                            "por milhão",
                            style={
                                "margin": "0",
                                "fontSize": "12px",
                                "color": "#9999AA"
                            }
                        )
                    ],
                    style={
                        "flex": "1",
                        "padding": "20px",
                        "backgroundColor": "#FFFFFF",
                        "borderRadius": "18px",
                        "boxShadow":
                            "0 8px 25px rgba(51,38,168,0.12)"
                    }
                ),


                html.Div(
                    [
                        html.P(
                            "MÁXIMA COBERTURA VACINAL",
                            style={
                                "margin": "0",
                                "fontSize": "13px",
                                "fontWeight": "600",
                                "color": "#777799"
                            }
                        ),

                        html.H2(
                            f"{max_vacinacao:.1f}%",
                            style={
                                "margin": "5px 0",
                                "fontSize": "30px",
                                "color": "#0AAFC0"
                            }
                        ),

                        html.P(
                            "cobertura registada",
                            style={
                                "margin": "0",
                                "fontSize": "12px",
                                "color": "#9999AA"
                            }
                        )
                    ],
                    style={
                        "flex": "1",
                        "padding": "20px",
                        "backgroundColor": "#FFFFFF",
                        "borderRadius": "18px",
                        "boxShadow":
                            "0 8px 25px rgba(51,38,168,0.12)"
                    }
                )

            ],

            style={
                "display": "flex",
                "gap": "20px",
                "padding": "25px 30px"
            }
        ),


        # ----------------------------------------------------
        # GRÁFICO 1
        # ----------------------------------------------------

        html.Div(
            dcc.Graph(
                figure=fig_covid
            ),
            style={
                "margin": "0 30px 25px 30px",
                "backgroundColor": "#FFFFFF",
                "borderRadius": "18px",
                "padding": "10px",
                "boxShadow":
                    "0 8px 25px rgba(51,38,168,0.08)"
            }
        ),


        # ------------------------------------------------------------------
        # GRÁFICOS 2 E 3 Evolução da cobertura vacinal e Excesso cumulativo
        # ------------------------------------------------------------------

        html.Div(
            [

                html.Div(
                    dcc.Graph(
                        figure=fig_vacinacao
                    ),
                    style={
                        "flex": "1",
                        "backgroundColor": "#FFFFFF",
                        "borderRadius": "18px",
                        "padding": "10px"
                    }
                ),

                html.Div(
                    dcc.Graph(
                        figure=fig_excesso
                    ),
                    style={
                        "flex": "1",
                        "backgroundColor": "#FFFFFF",
                        "borderRadius": "18px",
                        "padding": "10px"
                    }
                )

            ],

            style={
                "display": "flex",
                "gap": "20px",
                "margin": "0 30px 25px 30px"
            }
        ),
        
        
        html.Div(
    [
        html.H4(
            "📌 Como interpretar o excesso cumulativo de mortalidade?",
            style={
                "margin": "0 0 12px 0",
                "color": "#3326A8",
                "fontSize": "17px",
                "fontWeight": "700"
            }
        ),

        html.P(
            "Exemplo: num determinado período, eram esperadas "
            "100.000 mortes, mas ocorreram 103.000.",
            style={
                "margin": "0 0 8px 0",
                "fontSize": "14px",
                "color": "#444477",
                "lineHeight": "1.6"
            }
        ),

        html.P(
            "Excesso de mortalidade = 103.000 − 100.000 = 3.000 mortes",
            style={
                "margin": "0 0 8px 0",
                "fontSize": "14px",
                "fontWeight": "700",
                "color": "#3326A8"
            }
        ),

        html.P(
            "O excesso cumulativo corresponde à acumulação desses "
            "excessos ao longo do período analisado.",
            style={
                "margin": "0 0 8px 0",
                "fontSize": "14px",
                "color": "#444477",
                "lineHeight": "1.6"
            }
        ),

        html.P(
            "Nota: o excesso de mortalidade não corresponde ao número "
            "total de mortes nem exclusivamente às mortes por COVID-19.",
            style={
                "margin": "0",
                "fontSize": "13px",
                "fontStyle": "italic",
                "color": "#5B5B8A",
                "lineHeight": "1.5"
            }
        )
    ],
    style={
        "margin": "10px 30px 25px 30px",
        "padding": "18px 22px",
        "backgroundColor": "#F1F0FF",
        "borderRadius": "14px",
        "borderLeft": "4px solid #3326A8"
        }
    ),


        # ----------------------------------------------------
        # GRÁFICO 6 — CAUSAS DE MORTE
        # ----------------------------------------------------

        html.Div(
            dcc.Graph(
                figure=fig_causas
            ),
            style={
                "margin": "0 30px 25px 30px",
                "backgroundColor": "#FFFFFF",
                "borderRadius": "18px",
                "padding": "10px",
                "boxShadow":
                    "0 8px 25px rgba(51,38,168,0.08)"
            }
        ),
            


            
        # ============================================================
        # COMPARAÇÃO DAS CAUSAS DE MORTE — 2020 VS. 2024
        # ============================================================

        html.Div(
            dcc.Graph(
                figure=fig_comparacao
            ),
            style={
                "margin": "0 30px 25px 30px",
                "backgroundColor": "#FFFFFF",
                "borderRadius": "18px",
                "padding": "10px",
                "boxShadow": "0 8px 25px rgba(51,38,168,0.08)"
            }
        ),

        # ============================================================
        # VARIAÇÃO PERCENTUAL DOS ÓBITOS — 2020 VS. 2024
        # ============================================================

        html.Div(
            dcc.Graph(
                figure=fig_variacao
            ),
            style={
                "margin": "0 30px 25px 30px",
                "backgroundColor": "#FFFFFF",
                "borderRadius": "18px",
                "padding": "10px",
                "boxShadow": "0 8px 25px rgba(51,38,168,0.08)"
            }
        ),
        
# ============================================================
# BLOCO 24 — MAPA INTERATIVO COVID
# ============================================================

html.H2(
    "Mapa Interativo — Casos COVID-19 por Município",
    style={
        "textAlign": "center",
        "marginTop": "30px"
    }
),

html.Iframe(
    src="/assets/mapa_covid_interativo.html",
    style={
        "width": "100%",
        "height": "700px",
        "border": "none"
    }
),

# ============================================================
# BLOCO 25 — MAPA INTERATIVO — CAUSAS DE MORTE
# ============================================================

html.H2(
    "Mapa Interativo — Suicídios por Município — 2024",
    style={
        "textAlign": "center",
        "marginTop": "30px"
    }
),

html.Iframe(
    src="/assets/mapa_2_causas_morte_2024.html",
    style={
        "width": "100%",
        "height": "700px",
        "border": "none"
    }
),


        # ============================================================
        # CONCLUSÃO
        # ============================================================

        html.Div(
    [
        html.H2(
            "CONCLUSÃO",
            style={
                "margin": "0 0 15px 0",
                "fontSize": "22px",
                "fontWeight": "700",
                "color": "#3326A8"
            }
        ),

        html.P(
            "1) A análise dos dados evidencia uma redução das mortes por "
            "COVID-19 à medida que a cobertura vacinal aumentou, sendo "
            "observada uma correlação negativa entre as duas variáveis "
            "(r = -0,47).",
            style={
                "fontSize": "15px",
                "lineHeight": "1.7",
                "color": "#444477",
                "marginBottom": "12px"
            }
        ),

        html.P(
            "2) Embora o excesso cumulativo de mortalidade tenha aumentado "
            " os dados não comprovam mudanças abruptas nas mortes por outra causa.",
            style={
                "fontSize": "15px",
                "lineHeight": "1.7",
                "color": "#444477",
                "marginBottom": "12px"
            }
        ),

        html.P(
            "3) A análise das principais causas de morte permite ainda "
            "contextualizar o impacto da pandemia face às restantes "
            "causas de mortalidade em Portugal.",
            style={
                "fontSize": "15px",
                "lineHeight": "1.7",
                "color": "#444477",
                "margin": "0"
            }
        ),
        
        html.P(
            "4) Os dados não evidenciam um aumento sustentado da mortalidade"
            " que possa ser atribuído a efeitos colaterias da vacinação. ",
            style={
                "fontSize": "15px",
                "lineHeight": "1.7",
                "color": "#444477",
                "margin": "0"
            }
        ),

        html.Div(
            "Nota: correlação não implica causalidade. "
            "Os resultados devem ser interpretados no contexto de uma "
            "análise observacional de dados agregados.",
            style={
                "marginTop": "18px",
                "padding": "12px 16px",
                "backgroundColor": "#F1F0FF",
                "borderLeft": "4px solid #3326A8",
                "borderRadius": "8px",
                "fontSize": "13px",
                "color": "#5B5B8A"
            }
        )
    ],

    style={
        "margin": "0 30px 35px 30px",
        "padding": "25px 30px",
        "backgroundColor": "#FFFFFF",
        "borderRadius": "18px",
        "boxShadow": "0 8px 25px rgba(51,38,168,0.08)"
    }
    ),
        
        
        
        
    
# ============================================================
# BLOCO 26 — CONSIDERAÇÃO FINAL
# ============================================================

html.H2(
    "Consideração Final",
    style={
        "textAlign": "center",
        "marginTop": "40px",
        "color": "#3326A8"
    }
),

html.P(
    "A pandemia de COVID-19 constituiu um período de forte impacto "
    "na mortalidade em Portugal, mas os dados analisados mostram sinais "
    "de recuperação após esse período. Ao mesmo tempo, a evolução de "
    "algumas causas específicas de morte merece atenção. Estes resultados "
    "não permitem estabelecer relações causais, mas podem contribuir para "
    "levantar hipóteses e orientar análises futuras, nomeadamente sobre "
    "o crescimento observado em determinadas causas associadas à Saúde "
    "Mental. Neste contexto, o acompanhamento contínuo destes indicadores "
    "poderá ser relevante para apoiar a definição de prioridades de saúde "
    "pública e para uma maior atenção aos sinais de alteração da Saúde "
    "Mental da população portuguesa.",
    style={
        "textAlign": "justify",
        "fontSize": "16px",
        "lineHeight": "1.7",
        "margin": "20px 8%"
    }
    ),

   
    
html.Div(
    [
        # MASCOTE
        html.Div(
            html.Img(
                src="/assets/ze_agulha.png",
                style={
                    "width": "250px",
                    "height": "auto"
                }
            ),
            style={
                "flex": "0 0 220px",
                "textAlign": "center"
            }
        ),

        # CARTÃO DE IDENTIFICAÇÃO
        html.Div(
            [
                html.P(
                    "No âmbito da UFCD - 10809",
                    style={
                        "margin": "0",
                        "fontSize": "16px",
                        "fontWeight": "700",
                        "color": "#3326A8"
                    }
                ),

                html.P(
                    "Visualização de dados em Python",
                    style={
                        "margin": "3px 0 10px 0",
                        "fontSize": "14px",
                        "color": "#5B5B8A"
                    }
                ),

                html.P(
                    "Professor: Albano Afonso",
                    style={
                        "margin": "2px 0",
                        "fontSize": "13px",
                        "color": "#5B5B8A"
                    }
                ),

                html.P(
                    "Formanda: Silvane Viana",
                    style={
                        "margin": "2px 0",
                        "fontSize": "13px",
                        "color": "#5B5B8A"
                    }
                )
            ],
            style={
                "flex": "1",
                "padding": "14px 22px",
                "backgroundColor": "#F8FCFF",
                "borderRadius": "14px",
                "border": "1px solid #E5E2FF"
            }
        )
    ],

    style={
        "display": "flex",
        "alignItems": "center",
        "gap": "20px",
        "margin": "15px 30px",
        "padding": "12px 20px",
        "backgroundColor": "#F7FBFF",
        "borderRadius": "18px",
        "boxShadow": "0 5px 18px rgba(51,38,168,0.06)"
    }
),

 ]
 )
        
     


        

# ============================================================
# 10. EXECUTAR
# ============================================================

if __name__ == "__main__":
    app.run(
        debug=False,
        jupyter_mode="external"
    ) 