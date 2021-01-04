import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import json
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np

app = dash.Dash(external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

########## LOAD CSVS AND OTHER RESOURCES INTO PYTHON #####################

added_gene_name_csv = ''
added_gene_id_csv = ''
selected_gene_name_csv = ''
selected_gene_id_csv = ''


## colors for line plots
colordict={
'DoxC1':'#000099',
'2iC1':'#d48002',
'serumC1':'#5B2C6F',
'DoxC2':'#66a3ff',
'2iC2':'#F4D03F',
'serumC2':'#DF9AFF'
}

# create list of gene ids/names to search on searchbox
gene_search_options_df = pd.read_csv('broad17866genelist.csv')
gene_search_options_list = []
for idx, row in gene_search_options_df.iterrows():
    gene_search_options_list.append(
        # creates a dict with label `geneid genename` and value `geneid`
        {'label': row[0] + ' ' + row[1], 'value': row[0]}
    )

nice_descriptions=pd.read_csv('nice_mouse_gene_descriptions.csv', index_col=0)

samples = pd.read_csv('https://docs.google.com/spreadsheets/d/' +
                   '1_NePfzEcTq2VS9U1y5tpWm9tf2N6oTmEgoAjuT-YVZw' +
                   '/export?gid=0&format=csv',
                   index_col=0,
                  )
samples=samples.set_index('numid')


bigdedf = pd.read_csv('broad_de_df_20201230.csv', index_col=0)
print('Loaded!')

########## DASH APP LAYOUT ###################

app.layout = html.Div(id='megadiv', children=[
    html.Div(id='mesodiv', children=[
        html.Div(id='group1div', children=[
            html.Div([
                html.H6(""" Select timepoint for group 1 """),
                html.P("""D = Dox (first 8 days)"""),
            ]),
            dcc.Dropdown(
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
            ),
        ], className="four columns"),
        html.Div(id='group2div', children=[
            html.Div([
                html.H6(""" Select timepoint for group 2 """),
                html.P("D = Dox (first 8 days), I = i2 branch, last 10 days, S = serum branch, last 10 days")
            ]),
            dcc.Dropdown(
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
            ),
        ], className="four columns"),
        html.Div(id='volcanoseldiv', children=[
            html.Div([
                html.H6(""" Search for gene to visualize in timecourse """),
                html.P("(or click on volcano plot)")
            ]),
            dcc.Dropdown(
                id='gene_searchbox',
                options=gene_search_options_list,
                multi=False,
                value="ENSMUSG00000012396"
            )
        ], className="four columns"),

    ], className="row"),

    html.Div(id='volcanosdiv',children=[
            html.Div([
                # html.H3('Column 1'),
                dcc.Graph(id='volcano1', figure={})
            ], className="six columns"),

            html.Div([
                # html.H3('Column 2'),
                dcc.Graph(id='volcano2', figure={})
            ], className="six columns"),
        ], className="row"),
    html.Div(id='bottomdiv', children=[
        html.Div(id='timecoursediv',  children=[
            html.Div(id='t1div',children=[
                # html.H3('Column 1'),
                dcc.Graph(id='timecourse_expression', figure={}),

            ]),

            html.Div(id='t2div', children=[
                # html.H3('Column 2'),
                dcc.Graph(id='timecourse_lfc', figure={})
            ]),
        ], className="nine columns"),
        html.Div([
            html.Div([
                html.Div(id='searched_gene', style={'border': '6px yellow solid'}, children=' SEARCHED GENE SHOWS HERE'),
                html.Div(html.Button('Add selected genes', id='addgenes_button', n_clicks=0)),
                html.Div(id='selection_header', style={'border': '2px red solid'}, children=' Selected genes: '),
                html.Div(id='selected_genename_preview', style={'border': '2px lime solid'}),
                html.Br(),
                html.Div(html.Button('Clear chosen genes', id='removegenes_button', n_clicks=0))
            ], style={'border': '8px blue solid'}),
            # html.H3('Gene list'),

            html.Div([
                html.Div(id='chosen_genename_list', style={'border': '2px gray solid'}),
                html.Div(id='chosen_geneid_list', style={'border': '2px magenta solid'})
            ]),
        ], className="three columns", style={'border': '8px orange solid'}),
    ], className="row"),

])


####################### CALLBACKS TO MAKE PLOTS ##########################

def make_volcano(de, group1_name, group2_name, replicate):
    fig = go.Figure(
        data=go.Scattergl(
            x=de["lfc_mean"].round(3)
            , y=de["pval"].round(3)
            , mode='markers'
            , marker=dict(color=de.pval, opacity=0.5, colorscale='Hot', reversescale=True)
            , hoverinfo='text'
            , text=de['gene_description_html']
            , customdata=de.gene_name.astype(str) + '<br>' + de.gene_id.values + \
                         '<br>-log10(p-value): \t' + de["pval"].round(3).astype(str) + \
                         '<br>LFC mean: \t' + de["lfc_mean"].round(3).astype(str) + \
                         '<br>LFC std: \t' + de["lfc_std"].round(3).astype(str)
            , hovertemplate='%{customdata} <br><extra>%{text}</extra>'
        )
        , layout={
            "title": {"text": "<br>" + str(replicate) + " replicate DE - day " +
                              str(group1_name) + ' VS day ' + str(group2_name)
                , 'font': {'size': 16}
                , 'x': 0
                      }
            , 'xaxis': {'title': {"text": "　&nbsp;　log fold change <br> <br> "}}
            , 'yaxis': {'title': {"text": "<br> <br> -log10(p-value)"}}
            , 'margin': {'t': 20, 'b': 15, 'l': 10, 'r': 0}
            # , 'width': 1200
            # , 'height': 300
        }
    )

    fig.update_layout(hovermode='closest', template='none')
    fig.add_shape(type="line", x0=-10, y0=3, x1=10, y1=3, line=dict(color="Red", width=2, dash="dash"))
    # fig.show()
    return fig


def fetchnumid(rep, group):
    rep = rep
    timepoint = group.split(' ')[0]
    condition = group.split(' ')[1]
    return samples[(samples.timepoint == float(timepoint)) & (samples.condition == condition) & (
                samples.replicate == rep)].index.values[0]


@app.callback(Output('volcano1', 'figure'),
              [Input('group1', 'value'),
               Input('group2', 'value')])
def update_volcano1(timepoint1, timepoint2):
    rep = 'C1'
    numid1 = fetchnumid(rep, timepoint1)
    numid2 = fetchnumid(rep, timepoint2)
    de = bigdedf[(bigdedf.group1 == numid1) & (bigdedf.group2 == numid2)].copy()
    de['gene_name'] = de.index.map(nice_descriptions['gene_name'])
    de['gene_description_html'] = de.index.map(nice_descriptions['html_description'])
    de['gene_id']=de.index
    fig = make_volcano(de, timepoint1, timepoint2, replicate=rep)
    return fig


@app.callback(Output('volcano2', 'figure'),
              [Input('group1', 'value'),
               Input('group2', 'value')])
def update_volcano2(timepoint1, timepoint2):
    rep = 'C2'
    numid1 = fetchnumid(rep, timepoint1)
    numid2 = fetchnumid(rep, timepoint2)
    de = bigdedf[(bigdedf.group1 == numid1) & (bigdedf.group2 == numid2)].copy()
    de['gene_name'] = de.index.map(nice_descriptions['gene_name'])
    de['gene_description_html'] = de.index.map(nice_descriptions['html_description'])
    de['gene_id']=de.index
    fig = make_volcano(de, timepoint1, timepoint2, replicate=rep)
    return fig


@app.callback(Output('selected_genename_preview', 'children'),
              [Input('volcano1', 'selectedData'),
               Input('volcano2', 'selectedData')])
def update_selected_gene_preview(graph_one_selectData, graph_two_selectData):
    if dash.callback_context.triggered[0]['prop_id'] == 'volcano1.selectedData':
        global selected_gene_name_csv
        global selected_gene_id_csv

        selected_gene_name_csv = ''
        selected_gene_id_csv = ''
        for i in range(len(graph_one_selectData['points'])):
            # add comma separator if this is not the first element
            if len(selected_gene_name_csv) !=0: selected_gene_name_csv += ', '
            customdata = graph_one_selectData['points'][i]['customdata']
            gene_name = customdata.split('<br>')[0]
            gene_id = customdata.split('<br>')[1]
            selected_gene_name_csv = selected_gene_name_csv + gene_name
            selected_gene_id_csv = selected_gene_id_csv + gene_id
        return selected_gene_name_csv

    if dash.callback_context.triggered[0]['prop_id'] == 'volcano2.selectedData':
        selected_gene_name_csv = ''
        selected_gene_id_csv = ''
        for i in range(len(graph_two_selectData['points'])):
            # add comma separator if this is not the first element
            if len(selected_gene_name_csv) !=0: selected_gene_name_csv += ', '
            customdata = graph_two_selectData['points'][i]['customdata']
            gene_name = customdata.split('<br>')[0]
            gene_id = customdata.split('<br>')[1]
            selected_gene_name_csv = selected_gene_name_csv  + gene_name
            selected_gene_id_csv = selected_gene_id_csv + gene_id
        return selected_gene_name_csv

    return "Select genes with the lasso or box tool and they will show up here"
#     # table_style_conditions = update_table_style(selectedData)
#     print(json.dumps(selectedData))
#     return json.dumps(selectedData)

@app.callback(Output('chosen_genename_list', 'children'),
              [Input('volcano1', 'clickData'),
               Input('volcano2', 'clickData')])
def update_click_data(graph_one_clickData, graph_two_clickData):
    if dash.callback_context.triggered[0]['prop_id'] == 'volcano1.clickData':
        customdata = graph_one_clickData['points'][0]['customdata']
        print(customdata.split('<br>')[0])
        print(customdata.split('<br>')[1])
        gene_id = customdata.split('<br>')[1]
        gene_name = customdata.split('<br>')[0]
        return "You clicked on graph one " + gene_id + ' ' + gene_name

    if dash.callback_context.triggered[0]['prop_id'] == 'volcano2.clickData':
        customdata = graph_two_clickData['points'][0]['customdata']
        gene_id = customdata.split('<br>')[1]
        gene_name = customdata.split('<br>')[0]
        return "You clicked on graph two " + gene_id + ' ' + gene_name

    return "Start adding genes and they will show up here"



def make_timecourse_expression_fig(gene_id, numid11, numid21):
    gene_name = nice_descriptions.loc[gene_id]['gene_name']
    tc = bigdedf.loc[gene_id].copy()  ## create tc dataframe to hold timecourse data for chosen data
    tc = tc[(tc.group1 == numid11) | (tc.group1 == numid21)].copy()
    for col in ['day', 'replicate', 'timepoint', 'dcr', 'condition']:
        tc[col] = tc.group2.map(samples[col])
    tc['condition_replicate'] = tc['condition'] + tc['replicate']
    # Create traces
    fig = go.Figure()
    for cr in tc.condition_replicate.unique():
        plotdf = tc.query('condition_replicate==@cr')
        fig.add_trace(go.Scatter(
            x=plotdf.timepoint,
            y=plotdf.logscale2,
            mode='lines+markers',
            name=cr,
            line_color=colordict[cr]
        ))
    fig.update_layout(
        title="Timecourse expression of gene " + gene_name + '  -  ' + gene_id,
        xaxis_title="Day",
        yaxis_title="<br> <br> <br> log10 of expression frequency",
        legend_title="Condition",
        template='none',
        margin= {'t': 30, 'b': 15, 'l': 10, 'r': 0},
        height= 350

    )
    return fig
@app.callback(Output('timecourse_expression', 'figure'),
              [Input('group1', 'value'),
               Input('gene_searchbox', 'value')])
def update_timecourse_expression(timepoint1, gene_searchbox):
    numid11 = fetchnumid('C1', timepoint1)
    numid21 = fetchnumid('C2', timepoint1)
    gene_id=gene_searchbox
    return make_timecourse_expression_fig(gene_id, numid11, numid21)



def make_timecourse_lfc_fig(gene_id, numid11, numid21, timepoint1):
    gene_name = nice_descriptions.loc[gene_id]['gene_name']
    tc = bigdedf.loc[gene_id].copy()  ## create tc dataframe to hold timecourse data for chosen data
    tc = tc[(tc.group1 == numid11) | (tc.group1 == numid21)].copy()
    for col in ['day', 'replicate', 'timepoint', 'dcr', 'condition']:
        tc[col] = tc.group2.map(samples[col])
    tc['condition_replicate'] = tc['condition'] + tc['replicate']

    # Create traces
    fig = go.Figure()
    for cr in tc.condition_replicate.unique():
        plotdf = tc.query('condition_replicate==@cr')

        fig.add_trace(go.Scatter(
            x=plotdf.timepoint,
            y=plotdf.lfc_mean,
            mode='lines+markers',
            name=cr,
            line_color=colordict[cr]
        ))
        fig.add_trace(go.Scatter(
            x=np.append(plotdf.timepoint.values, plotdf.timepoint.values[::-1]),  # x, then x reversed
            y=np.append(plotdf.lfc_mean.values + plotdf.lfc_std.values,
                        plotdf.lfc_mean.values[::-1] - plotdf.lfc_std.values[::-1]),  # upper, then lower reversed
            fill='toself',
            fillcolor='rgba(100,100,100,0.1)',
            line=dict(color='rgba(255,255,255,0)'),
            hoverinfo="skip",
            showlegend=False,

        ))

    fig.update_layout(
        title="Timecourse of log fold change of gene " + gene_name + ' relative to group1: day ' + str (timepoint1),
        xaxis_title="Day",
        yaxis_title="<br><br><br> relative log fold change",
        legend_title="Condition",
        template='none',
        margin = {'t': 30, 'b': 15, 'l': 10, 'r': 0},
        height=350
    )
    return fig

@app.callback(Output('timecourse_lfc', 'figure'),
              [Input('group1', 'value'),
               Input('gene_searchbox', 'value')])
def update_timecourse_lfc(timepoint1, gene_searchbox):
    numid11 = fetchnumid('C1', timepoint1)
    numid21 = fetchnumid('C2', timepoint1)
    gene_id=gene_searchbox
    return make_timecourse_lfc_fig(gene_id, numid11, numid21, timepoint1)








#
# def update_timeseries_expression_volcano(graph_one_clickData, graph_two_clickData):
#     if dash.callback_context.triggered[0]['prop_id'] == 'volcano1.clickData':
#         customdata = graph_one_clickData['points'][0]['customdata']
#         print(customdata.split('<br>')[0])
#         print(customdata.split('<br>')[1])
#         gene_id = customdata.split('<br>')[1]
#         gene_name = customdata.split('<br>')[0]
#         return "You clicked on graph one " + gene_id + ' ' + gene_name
#
#     if dash.callback_context.triggered[0]['prop_id'] == 'volcano2.clickData':
#         customdata = graph_two_clickData['points'][0]['customdata']
#         gene_id = customdata.split('<br>')[1]
#         gene_name = customdata.split('<br>')[0]
#         return "You clicked on graph two " + gene_id + ' ' + gene_name
#
#     return "Start adding genes and they will show up here"



#
# def update_timeseries_lfc(graph_one_clickData, graph_two_clickData):
#     if dash.callback_context.triggered[0]['prop_id'] == 'volcano1.clickData':
#         customdata = graph_one_clickData['points'][0]['customdata']
#         print(customdata.split('<br>')[0])
#         print(customdata.split('<br>')[1])
#         gene_id = customdata.split('<br>')[1]
#         gene_name = customdata.split('<br>')[0]
#         return "You clicked on graph one " + gene_id + ' ' + gene_name
#
#     if dash.callback_context.triggered[0]['prop_id'] == 'volcano2.clickData':
#         customdata = graph_two_clickData['points'][0]['customdata']
#         gene_id = customdata.split('<br>')[1]
#         gene_name = customdata.split('<br>')[0]
#         return "You clicked on graph two " + gene_id + ' ' + gene_name
#
#     return "Start adding genes and they will show up here"
















if __name__ == '__main__':
    app.run_server(debug=True)
