import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

from dash.dependencies import Input, Output
import pandas as pd
import numpy as np



########## LOAD CSVS AND OTHER RESOURCES INTO PYTHON #####################

# create list of gene ids/names to search on searchbox
gene_search_options_df=pd.read_csv('broad17866genelist.csv')
gene_search_options_list = []
for idx, row in gene_search_options_df.iterrows():
    gene_search_options_list.append(
    # creates a dict with label `geneid genename` and value `geneid`
    {'label': row[0] + ' ' + row[1], 'value':row[0]}
    )



########## DASH APP LAYOUT ###################
app = dash.Dash(external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div(id='megadiv', style={'border': '6px black solid'}, children=[
    html.Div(id='mesodiv', style={'border': '6px pink solid'}, children=[
        html.Div(id='group1div', style={'border': '6px darkblue solid'}, children=[

            html.Div([
                html.H6(""" Select timepoint for group 1 """),
                html.P("""D = Dox (first 8 days)"""),
            ]),
            dcc.RadioItems(
                id='group1',
                options=[
                    {'label': 'D0　　', 'value': '0 Dox'},
                    {'label': 'D0.5　　', 'value': '0.5 Dox'},
                    {'label': 'D1　　', 'value': '1 Dox'},
                    {'label': 'D1.5　　', 'value': '1.5 Dox'},
                    {'label': 'D2　　', 'value': '2 Dox'},
                    {'label': 'D2.5　　', 'value': '2.5 Dox'},
                    {'label': 'D3　　', 'value': '3 Dox'},
                    {'label': 'D3.5　　', 'value': '3.5 Dox'},
                    {'label': 'D4　　', 'value': '4 Dox'},
                    {'label': 'D4.5　　', 'value': '4.5 Dox'},
                    {'label': 'D5　　', 'value': '5 Dox'},
                    {'label': 'D5.5　　', 'value': '5.5 Dox'},
                    {'label': 'D6　　', 'value': '6 Dox'},
                    {'label': 'D6.5　　', 'value': '6.5 Dox'},
                    {'label': 'D7　　', 'value': '7 Dox'},
                    {'label': 'D7.5　　', 'value': '7.5 Dox'},
                    {'label': 'D8　　', 'value': '8 Dox'},
                ],
                value='0 Dox',
                labelStyle={'display': 'inline-block'}
            ),
            html.Div(id='volcanoseldiv', style={'border': '6px darkred solid',
                                                'marginTop': '2em'}, children=[
                html.Div([
                    html.H6(""" Search for gene to visualize in timecourse (or click on volcano plot)"""),
                ]),
                dcc.Dropdown(
                    id='gene_searchbox',
                    options=gene_search_options_list,
                    multi=False,
                    value="ENSMUSG00000012396"
                )]
                     ),
        ], className="six columns"),

        html.Div(id='group2div', style={'border': '6px lightblue solid'}, children=[
            html.Div([
                html.H6(""" Select timepoint for group 2 """),
                html.P("D = Dox (first 8 days), I = i2 branch, last 10 days, S = serum branch, last 10 days")
            ]),
            dcc.RadioItems(
                id='group2',
                options=[
                    {'label': 'D0　　', 'value': '0 Dox'},
                    {'label': 'D0.5　　', 'value': '0.5 Dox'},
                    {'label': 'D1　　', 'value': '1 Dox'},
                    {'label': 'D1.5　　', 'value': '1.5 Dox'},
                    {'label': 'D2　　', 'value': '2 Dox'},
                    {'label': 'D2.5　　', 'value': '2.5 Dox'},
                    {'label': 'D3　　', 'value': '3 Dox'},
                    {'label': 'D3.5　　', 'value': '3.5 Dox'},
                    {'label': 'D4　　', 'value': '4 Dox'},
                    {'label': 'D4.5　　', 'value': '4.5 Dox'},
                    {'label': 'D5　　', 'value': '5 Dox'},
                    {'label': 'D5.5　　', 'value': '5.5 Dox'},
                    {'label': 'D6　　', 'value': '6 Dox'},
                    {'label': 'D6.5　　', 'value': '6.5 Dox'},
                    {'label': 'D7　　', 'value': '7 Dox'},
                    {'label': 'D7.5　　', 'value': '7.5 Dox'},
                    {'label': 'D8　　', 'value': '8 Dox'},
                    {'label': 'S8.25　　', 'value': '8.25 serum'},
                    {'label': 'S8.5　　', 'value': '8.5 serum'},
                    {'label': 'S8.75　　', 'value': '8.75 serum'},
                    {'label': 'S9　　', 'value': '9 serum'},
                    {'label': 'S9.5　　', 'value': '9.5 serum'},
                    {'label': 'S10　　', 'value': '10 serum'},
                    {'label': 'S10.5　　', 'value': '10.5 serum'},
                    {'label': 'S11　　', 'value': '11 serum'},
                    {'label': 'S11.5　　', 'value': '11.5 serum'},
                    {'label': 'S12　　', 'value': '12 serum'},
                    {'label': 'S12.5　　', 'value': '12.5 serum'},
                    {'label': 'S13　　', 'value': '13 serum'},
                    {'label': 'S13.5　　', 'value': '13.5 serum'},
                    {'label': 'S14　　', 'value': '14 serum'},
                    {'label': 'S14.5　　', 'value': '14.5 serum'},
                    {'label': 'S15　　', 'value': '15 serum'},
                    {'label': 'S15.5　　', 'value': '15.5 serum'},
                    {'label': 'S16　　', 'value': '16 serum'},
                    {'label': 'S16.5　　', 'value': '16.5 serum'},
                    {'label': 'S17　　', 'value': '17 serum'},
                    {'label': 'S17.5　　', 'value': '17.5 serum'},
                    {'label': 'S18　　', 'value': '18 serum'},
                    {'label': 'I8.25　　', 'value': '8.25 2i'},
                    {'label': 'I8.5　　', 'value': '8.5 2i'},
                    {'label': 'I8.75　　', 'value': '8.75 2i'},
                    {'label': 'I9　　', 'value': '9 2i'},
                    {'label': 'I9.5　　', 'value': '9.5 2i'},
                    {'label': 'I10　　', 'value': '10 2i'},
                    {'label': 'I10.5　　', 'value': '10.5 2i'},
                    {'label': 'I11　　', 'value': '11 2i'},
                    {'label': 'I11.5　　', 'value': '11.5 2i'},
                    {'label': 'I12　　', 'value': '12 2i'},
                    {'label': 'I12.5　　', 'value': '12.5 2i'},
                    {'label': 'I13　　', 'value': '13 2i'},
                    {'label': 'I13.5　　', 'value': '13.5 2i'},
                    {'label': 'I14　　', 'value': '14 2i'},
                    {'label': 'I14.5　　', 'value': '14.5 2i'},
                    {'label': 'I15　　', 'value': '15 2i'},
                    {'label': 'I15.5　　', 'value': '15.5 2i'},
                    {'label': 'I16　　', 'value': '16 2i'},
                    {'label': 'I16.5　　', 'value': '16.5 2i'},
                    {'label': 'I17　　', 'value': '17 2i'},
                    {'label': 'I17.5　　', 'value': '17.5 2i'},
                    {'label': 'I18　　', 'value': '18 2i'},
                ],
                value='5 Dox',
                labelStyle={'display': 'inline-block'}
            ),
        ], className="six columns"),
    ], className="row"),

    html.Div(id='volcanosdiv', style={'border': '6px none solid'}
             , children=[
        html.Div([
            # html.H3('Column 1'),
            dcc.Graph(id='volcano1', figure={'data': [{'y': [1, 2, 3]}],
                                       'layout': go.Layout(
                                           # margin={'t': 3, 'b':3},
                                           title="Plot Title t1",
                                           xaxis_title="X Axis Title",
                                           yaxis_title="Y Axis Title",
                                           legend_title="Legend Title",
                                           height=300,
                                       ),
                                       })
        ], className="six columns"),

        html.Div([
            # html.H3('Column 2'),
            dcc.Graph(id='volcano2', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),
    ], className="row"),
    html.Div(id='bottomdiv', style={'border': '6px brown solid'}, children=[
        html.Div(id='timecoursediv', style={'border': '6px green solid'}, children=[
            html.Div(id='t1div', style={'border': '6px gold solid'}, children=[
                # html.H3('Column 1'),
                dcc.Graph(id='t1', figure={'data': [{'y': [1, 2, 3], 'name': 'fooo'}],
                                           'layout': go.Layout(
                                               margin={'t': 0},
                                               title="Plot Title t1",
                                               xaxis_title="X Axis Title",
                                               yaxis_title="Y Axis Title",
                                               legend_title="Legend Title",
                                               height=300,
                                           ),
                                           }),
            ]),

            html.Div(id='t2div', style={'border': '6px purple solid'}, children=[
                # html.H3('Column 2'),
                dcc.Graph(id='t2', figure={'data': [{'y': [1, 2, 3]}],
                                           'layout': go.Layout(
                                               margin={'t': 0},
                                               title="Plot Title t2",
                                               xaxis_title="X Axis Title",
                                               yaxis_title="Y Axis Title",
                                               legend_title="Legend Title",
                                               height=300,
                                           ),
                                           })
            ]),
        ], className="nine columns"),
        html.Div([
            html.Div([
                html.Div(html.Button('Add selected genes', id='addgenes_button', n_clicks=0)),
                html.Br(),
                html.Div(html.Button('Clear chosen genes', id='removegenes_button', n_clicks=0))
            ], style={'border': '8px blue solid'}),
            # html.H3('Gene list'),

            html.Div(
                html.Pre(id='chosen_genename_list', children='GENE NAMES  \n \t GO HERE',
                         style={'border': '2px gray solid'})),
            html.Div(html.Pre(id='chosen_geneid_list', children='GENE IDS <br> GO HERE',
                              style={'border': '2px magenta solid'}))
        ], className="three columns", style={'border': '8px orange solid'}),
    ], className="row"),

])

####################### CALLBACKS TO MAKE PLOTS ##########################

@app.callback( Output('volcano2', 'figure'),
               [Input('group1', 'value'),
                Input('group2', 'value')])
def update_volcano1(timepoint1, timepoint2):
    group1_name=timepoint1
    group2_name=timepoint2
    de=pd.read_csv('testdedf_D0D5.csv', index_col = 0)
    jitterpval = de["pval"] + np.random.uniform(low=-1, high=1, size=len(de["pval"])) * de["pval"].pow(4).values / 625
    fig = go.Figure(
        data=go.Scattergl(
            x=de["lfc_mean"].round(3)
            # , y=jitterpval
            , y=de["pval"].round(3)
            , mode='markers'
            , marker=dict(color=de.pval, opacity=0.2, colorscale='Hot', reversescale=True)
            , hoverinfo='text'
            , text=de['gene_description_html']
            , customdata=de.gene_name.astype(str) + '<br>' + de.gene_id.values + \
                         '<br>-log10(p-value): \t' + de["pval"].round(3).astype(str) + \
                         '<br>LFC mean: \t' + de["lfc_mean"].round(3).astype(str) + \
                         '<br>LFC std: \t' + de["lfc_std"].round(3).astype(str)
            , hovertemplate='%{customdata} <br><extra>%{text}</extra>'
        )
        , layout={
            "title": {"text": "<br>Replicate 2 Differential expression of day " + str(group1_name) + ' vs day ' + str(group2_name)
                      , 'font':{'size':14}
                # , 'x': 0.5
                      }
            , 'xaxis': {'title': {"text": "　&nbsp;　log fold change <br> <br> "}}
            , 'yaxis': {'title': {"text": "<br> <br> -log10(p-value)"}}
            , 'margin':{'t': 0, 'b':15, 'l':10, 'r':0}
            # , 'width': 1200
            # , 'height': 300
        }
    )

    fig.update_layout(hovermode='closest')
    fig.add_shape(type="line", x0=-10, y0=3, x1=10, y1=3,
                  line=dict(color="Red", width=2, dash="dash", )
                  )
    fig.update_layout(
        hoverlabel=dict(
            #         bgcolor="white",
            #         font_size=16,
            #         font_family="Rockwell"
        )
    )
    fig.update_layout(template='none')
    # fig.show()
    return fig























if __name__ == '__main__':
    app.run_server(debug=True)
