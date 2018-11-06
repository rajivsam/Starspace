#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 17:35:51 2018

@author: admin123
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import os
import plotly.graph_objs as go

os.chdir("/home/admin123/Starspace/data")
fpsp = "starspace_tsne.csv"
fpnmf = "nmf_tsne.csv"
dfsp = pd.read_csv(fpsp)
dfnmf = pd.read_csv(fpnmf)

rep_opts=[{'label': 'Star Space Representation', 'value': 'SSR'},\
            {'label': 'NMF Representation', 'value': 'NMFR'}]

traces_sp = []
sp1 = go.Scatter(x = dfsp["Latent_Dim_1"],\
                y = dfsp["Latent_Dim_2"] , mode = 'markers')
traces_sp.append(sp1)
traces_nmf =[]
sp2 = go.Scatter(x = dfnmf["Latent_Dim_1"],\
                y = dfnmf["Latent_Dim_2"] , mode = 'markers')
traces_nmf.append(sp2)

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
        html.H2(children='Select a Representation'),
        dcc.Dropdown(options = rep_opts, id='rep-dropdown', value = 'SSR'),
    html.H2(children='TSNE Visualization'),
    dcc.Graph(id='rep-graph')],
    style={'margin-left':'auto', 'margin-right': 'auto', 'width': '400px'})
@app.callback(
    dash.dependencies.Output('rep-graph', 'figure'),
    [dash.dependencies.Input('rep-dropdown', 'value')])

def update_figure(rep_type):

    if rep_type == 'SSR':
        return {
        'data': traces_sp,
        'layout': go.Layout(
            xaxis={'title': 'Latent Dim 1'},
            yaxis={'title': 'Latent Dim 2'},
            hovermode='closest')
        }
        
    else:
        return {
        'data': traces_nmf,
        'layout': go.Layout(
            xaxis={'title': 'Latent Dim 1'},
            yaxis={'title': 'Latent Dim 2'},
            hovermode='closest')
        } 
    
   
if __name__ == '__main__':
    app.run_server(debug=True)