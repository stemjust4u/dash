# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

markdown_text = '''
### My Dashboard

This is a dashboard
'''

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('/home/chawn1272/Documents/aser-data-tall-dash2.csv')
#dfpivot = pd.pivot_table(df, values='question', index=['parm1'], columns = ['company']).reset_index()
#dfpivot = df.groupby(['parm1']).describe().round(1)
#dfpivot = df.describe().round(1)
#dfpivot = df.describe().T
#df[[0]].describe().T  # single column
#pivoted.groupby(['file']).describe().round(1).drop(['sensor', 'delta', 'raw', 'ave'], axis=1)

df2 = pd.read_csv('/home/chawn1272/Documents/aser-data-tall-dash.csv')
dfquestion = df2[df2["Metric Name"].isin(["question"])] # Get rows only with "question" category
dfpivot = dfquestion

def generate_table(dataframe, max_rows=3):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

fig1 = px.scatter(df, x="parm1", y="assessment",
                 size="question", color="parm2v1", hover_name="company",
                 log_x=False, size_max=25)

fig2 = px.scatter(df, x="parm1", y="question",
                 size="question", color="parm2v1", hover_name="company",
                 log_x=False, size_max=30)

figH1 = px.histogram(df, x="question", nbins=15)

app.layout = html.Div(children=[
    html.H1(children='Header'),
    dcc.Markdown(children=markdown_text),
    generate_table(dfpivot),
    html.Div([
    dcc.Graph(
        id='parm1 vs assessment',
        figure=fig1)], style={'width': '33%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
    dcc.Graph(
        id='parm1 vs question',
        figure=fig2)], style={'width': '33%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
    dcc.Graph(
        id='Question Histogram',
        figure=figH1)], style={'width': '33%', 'display': 'inline-block', 'padding': '0 20'}),
    html.P("x-axis:"),
    dcc.Checklist(
        id='x-axis', 
        options=[{'value': x, 'label': x} 
                 for x in ['parm1', 'parm2v1', 'parm2v2']],
        value=['parm1'], 
        labelStyle={'display': 'inline-block'}
    ),
    html.P("y-axis:"),
    dcc.RadioItems(
        id='y-axis', 
        options=[{'value': x, 'label': x} 
                 for x in ['Value']],
        value='Value', 
        labelStyle={'display': 'inline-block'}
    ),
    html.Div([
        dcc.Graph(id="box-plot")], style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'})
])

@app.callback(
    Output("box-plot", "figure"), 
    [Input("x-axis", "value"), 
     Input("y-axis", "value")])
def generate_chart(x, y):
    fig = px.box(df2, x=x, y=y, color="Metric Name")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)