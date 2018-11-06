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

os.chdir("/home/admin123/Starspace/data")
fp = "starspace_item_clustering.csv"
df = pd.read_csv(fp)

df["Cluster"] = df["Cluster"].astype(str)
clus_ids = df["Cluster"].unique().tolist()
clus_opts = [{'label': "Cluster-" + cid ,\
              'value' : cid} for cid in clus_ids]


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
        html.H2(children='Select a Cluster'),
        dcc.Dropdown(options = clus_opts, id='cluster-dropdown', value = clus_ids[1]),
    html.H2(children='Cluster Details'),
    html.Div(id='table-container')
], style={'margin-left':'auto', 'margin-right': 'auto', 'width': '400px'})
@app.callback(
    dash.dependencies.Output('table-container', 'children'),
    [dash.dependencies.Input('cluster-dropdown', 'value')])
def display_table(dropdown_value):
    if dropdown_value is None:
        return generate_table(df)
    
    dff = df[df["Cluster"] == dropdown_value]
   
    return generate_table(dff)

if __name__ == '__main__':
    app.run_server(debug=True)