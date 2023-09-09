# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('/home/chawn1272/Documents/aser-data-tall-dash2.csv')

figH1 = px.histogram(df, x="question", nbins=15)

fig1 = px.scatter(df, x="parm1", y="assessment",
                 size="question", color="parm2v1", hover_name="company",
                 log_x=False, size_max=25)

fig2 = px.scatter(df, x="parm1", y="question",
                 size="question", color="parm2v1", hover_name="company",
                 log_x=False, size_max=30)

app.layout = html.Div([
    html.Div([
    dcc.Graph(
        id='parm1 vs assessment',
        figure=fig2
    )
], style={'width': '33%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
    dcc.Graph(
        id='parm1 vs question',
        figure=figH1
    )
], style={'width': '33%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
    dcc.Graph(
        id='Question Histogram',
        figure=fig1
    )
], style={'width': '33%', 'display': 'inline-block', 'padding': '0 20'})
])

if __name__ == '__main__':
    app.run_server(debug=True)