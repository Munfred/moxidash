import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
import pandas as pd
import numpy as np

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, 'https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
    html.Div(id='group1div', style={'border': '6px darkblue solid'}, children=[

        html.Div(
            [
                html.H6(""" Select timepoint for group 1 """,
                        style={'textAlign': 'left', 'font-weight': 'bold', 'margin-left': '0em', 'margin-right': '2em',
                               'display': 'inline-block', 'width': '40%'}),

                html.P("""D = Dox (first 8 days)"""),
            ],
        ),
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
            value='D0 Dox',
            labelStyle={'display': 'inline-block'}
        ),
    ]),

    html.Div(id='group2div', style={'border': '6px lightblue solid'}, children=[

        html.Div(
            [
                html.H6(
                    """ Select timepoint for group 2 """,
                    style={'textAlign': 'left', 'font-weight': 'bold', 'margin-left': '0em', 'margin-right': '2em',
                           'display': 'inline-block', 'width': '40%'}),
                html.P(
                    """D = Dox (first 8 days),  I = i2 branch of last 10 days, S = serum branch of last 10 days""")
            ],
        ),
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
            value='D5 Dox',
            labelStyle={'display': 'inline-block'}
        ),
    ]),
    html.Div(

        id='volcanodiv', style={'border': '6px darkred solid',
                                'textAlign': 'left', 'font-weight': 'bold', 'margin-left': '2em',
                                'margin-right': '2em',
                                'display': 'inline-block', 'width': '40%'
                                },
        children=[
            html.Div(
                [
                    html.H6(""" Search for gene to visualize in timecourse """),
                    html.P("""(or click on volcano plot)"""),
                ],
            ),
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
                value="D0 Dox"
            ),
        ]

    ),
])

if __name__ == '__main__':
    app.run_server()
