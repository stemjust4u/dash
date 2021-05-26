# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('/home/chawn1272/Documents/aser-data-tall-dash2.csv')

fig = px.scatter(df, x="parm1", y="assessment",
                 size="question", color="parm2v1", hover_name="company",
                 log_x=False, size_max=25)

app.layout = html.Div([
    dcc.Graph(
        id='parm1 vs assessment',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)