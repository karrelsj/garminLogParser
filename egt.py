# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('19JAN2021.csv')
#df = px.data.stocks()

app = dash.Dash(__name__)

#app.layout = html.Div([
#    dcc.Dropdown(
#        id="cht",
#        options=[{"label": x, "value": x} 
#                 for x in df.columns[1:]],
#        value=df.columns[1],
#        clearable=False,
#    ),
#    dcc.Graph(id="time-series-chart"),
#])

#@app.callback(
#    Output("time-series-chart", "figure"), 
#    [Input("cht", "value")])
#def display_time_series(cht):
#    print cht
#    fig = px.line(df, x=df.index, y=cht)
#    return fig



colors = px.colors.qualitative.Plotly
fig = go.Figure()
fig.add_traces(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT1 (deg F)'], mode = 'lines', name='CHT1', line=dict(color=colors[0])))
fig.add_traces(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT2 (deg F)'], mode = 'lines', name='CHT2', line=dict(color=colors[1])))
fig.add_traces(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT3 (deg F)'], mode = 'lines', name='CHT3', line=dict(color=colors[2])))
fig.add_traces(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT4 (deg F)'], mode = 'lines', name='CHT4', line=dict(color=colors[3])))
fig.add_traces(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT5 (deg F)'], mode = 'lines', name='CHT5', line=dict(color=colors[4])))
fig.add_traces(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT6 (deg F)'], mode = 'lines', name='CHT6', line=dict(color=colors[5])))
fig.show()



app.run_server(debug=True)


