import os
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

my_app = dash.Dash('My app', external_stylesheets=external_stylesheets)

my_app.layout = html.Div([
    dcc.Graph(id='my-graph'),
    html.P('Mean'),
    dcc.Slider(id="mean", min=-3, max=3, value=0,
               marks={-3: '-3', -2: '-2', -1: '-1', 0: '0', 1: '1', 2: '2', 3: '3'}),
    html.Br(),
    html.P("Standard deviation"),
    dcc.Slider(id='std', min=1, max=3, value=1,
               marks={1: "1", 3: "3"}),
    html.Br(),
    html.P("Number of samples"),
    dcc.Slider(id='size', min=1, max=10000, value=100,
               marks={100: "100", 500: "500", 1000: "1000", 5000: "5000", 10000: "10000"}),
    html.Br(),
    html.P("Number of bins"),
    dcc.Slider(id='bins', min=10, max=100, value=10,
               marks={10: "10", 30: "30", 60: "60", 80: "80", 100: "100"}),
])

@my_app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [
        Input(component_id='mean', component_property='value'),
        Input(component_id='std', component_property='value'),
        Input(component_id='size', component_property='value'),
        Input(component_id='bins', component_property='value')
    ]
)
def display_color(mean, std, size, bins):
    x = np.random.normal(mean, std, size=size)
    fig = px.histogram(x=x, nbins=bins, range_x=[-5, 5])
    return fig

# Dynamically set port for Cloud Run (8080) or local (8888)
port = int(os.environ.get('PORT', 8888))
my_app.run(
    debug=True,
    port=port,
    host='0.0.0.0'
)