import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

from dash.dependencies import Input, Output
import pandas as pd
import numpy as np

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
                    id='volcano_gene_selection',
                    options=[
                        {'label': 'D0 Dox', 'value': 'D0 Dox'},
                        {'label': 'D0.5 Dox', 'value': 'D0.5 Dox'},
                        {'label': 'D1 Dox', 'value': 'D1 Dox'},
                        {'label': 'D1.5 Dox', 'value': 'D1.5 Dox'},
                        {'label': 'D2 Dox', 'value': 'D2 Dox'},
                        {'label': 'D2.5 Dox', 'value': 'D2.5 Dox'},
                        {'label': 'D3 Dox', 'value': 'D3 Dox'},
                        {'label': 'D3.5 Dox', 'value': 'D3.5 Dox'},
                        {'label': 'D4 Dox', 'value': 'D4 Dox'},
                        {'label': 'D4.5 Dox', 'value': 'D4.5 Dox'},
                        {'label': 'D5 Dox', 'value': 'D5 Dox'},
                        {'label': 'D5.5 Dox', 'value': 'D5.5 Dox'},
                        {'label': 'D6 Dox', 'value': 'D6 Dox'},
                        {'label': 'D6.5 Dox', 'value': 'D6.5 Dox'},
                        {'label': 'D7 Dox', 'value': 'D7 Dox'},
                        {'label': 'D7.5 Dox', 'value': 'D7.5 Dox'},
                        {'label': 'D8 Dox', 'value': 'D8 Dox'},
                    ],
                    multi=False,
                    value="0 Dox"
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

    html.Div(id='volcanosdiv', style={'border': '6px red solid'}, children=[
        html.Div([
            # html.H3('Column 1'),
            dcc.Graph(id='g1', figure={'data': [{'y': [1, 2, 3]}],
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
            dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}],
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

if __name__ == '__main__':
    app.run_server(debug=True)
