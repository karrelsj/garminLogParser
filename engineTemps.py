# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


df = pd.read_csv('19JAN2021.csv')

#app = dash.Dash(__name__)

colors = px.colors.qualitative.Plotly

#Make plot for CHT vs Manifold Pressure
fig = make_subplots(
    rows=4,cols=1,
    row_heights=[0.25, 0.25, 0.25,0.25],
    specs=[[{"secondary_y": True}]*1]*4,
    subplot_titles=("Manifold Pressure vs Cylinder Head Temp","Manifold Pressure vs Exhaust Gas Temp","Knots Indicated Airspeed vs Cylinder Head Temp","Vertical Speed vs Cylinder Head Temp"))

fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['Manifold Press (inch Hg)'], mode = 'lines', name='Manifold Press', line=dict(color=colors[0])),secondary_y=False,row=1,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT1 (deg F)'], mode = 'lines', name='CHT1', line=dict(color=colors[1])),secondary_y=True,row=1,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT2 (deg F)'], mode = 'lines', name='CHT2', line=dict(color=colors[2])),secondary_y=True,row=1,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT3 (deg F)'], mode = 'lines', name='CHT3', line=dict(color=colors[3])),secondary_y=True,row=1,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT4 (deg F)'], mode = 'lines', name='CHT4', line=dict(color=colors[4])),secondary_y=True,row=1,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT5 (deg F)'], mode = 'lines', name='CHT5', line=dict(color=colors[5])),secondary_y=True,row=1,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT6 (deg F)'], mode = 'lines', name='CHT6', line=dict(color=colors[6])),secondary_y=True,row=1,col=1)

#fig.update_layout(
#title="CHT vs Manifold Pressure",
#xaxis_title="Time",
#yaxis_title="Cylinder Head Temp",
#legend_title="Legend"
#)


#Make plot for EGT vs Manifold Pressure
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['Manifold Press (inch Hg)'], mode = 'lines', name='Manifold Press', line=dict(color=colors[0])),secondary_y=False,row=2,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['EGT1 (deg F)'], mode = 'lines', name='EGT1', line=dict(color=colors[1])),secondary_y=True,row=2,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['EGT2 (deg F)'], mode = 'lines', name='EGT2', line=dict(color=colors[2])),secondary_y=True,row=2,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['EGT3 (deg F)'], mode = 'lines', name='EGT3', line=dict(color=colors[3])),secondary_y=True,row=2,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['EGT4 (deg F)'], mode = 'lines', name='EGT4', line=dict(color=colors[4])),secondary_y=True,row=2,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['EGT5 (deg F)'], mode = 'lines', name='EGT5', line=dict(color=colors[5])),secondary_y=True,row=2,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['EGT6 (deg F)'], mode = 'lines', name='EGT6', line=dict(color=colors[6])),secondary_y=True,row=2,col=1)

#fig.update_layout(
#title="CHT vs Manifold Pressure",
#xaxis_title="Time",
#yaxis_title="Cylinder Head Temp",
#legend_title="Legend"
#)


#Make plot for EGT vs CHT
#fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['EGT1 (deg F)'], mode = 'lines', name='EGT1', line=dict(color=colors[1])),secondary_y=True,row=3,col=1)
#fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['EGT2 (deg F)'], mode = 'lines', name='EGT2', line=dict(color=colors[2])),secondary_y=True,row=3,col=1)
#fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['EGT3 (deg F)'], mode = 'lines', name='EGT3', line=dict(color=colors[3])),secondary_y=True,row=3,col=1)
#fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['EGT4 (deg F)'], mode = 'lines', name='EGT4', line=dict(color=colors[4])),secondary_y=True,row=3,col=1)
#fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['EGT5 (deg F)'], mode = 'lines', name='EGT5', line=dict(color=colors[5])),secondary_y=True,row=3,col=1)
#fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['EGT6 (deg F)'], mode = 'lines', name='EGT6', line=dict(color=colors[6])),secondary_y=True,row=3,col=1)
#fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT1 (deg F)'], mode = 'lines', name='CHT1', line=dict(color=colors[1])),secondary_y=True,row=3,col=1)
#fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT2 (deg F)'], mode = 'lines', name='CHT2', line=dict(color=colors[2])),secondary_y=True,row=3,col=1)
#fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT3 (deg F)'], mode = 'lines', name='CHT3', line=dict(color=colors[3])),secondary_y=True,row=3,col=1)
#fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT4 (deg F)'], mode = 'lines', name='CHT4', line=dict(color=colors[4])),secondary_y=True,row=3,col=1)
#fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT5 (deg F)'], mode = 'lines', name='CHT5', line=dict(color=colors[5])),secondary_y=True,row=3,col=1)
#fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT6 (deg F)'], mode = 'lines', name='CHT6', line=dict(color=colors[6])),secondary_y=True,row=3,col=1)

#Make plot for CHT vs KIAS
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['Indicated Airspeed (kt)'], mode = 'lines', name='KIAS', line=dict(color=colors[0])),secondary_y=False,row=3,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT1 (deg F)'], mode = 'lines', name='CHT1', line=dict(color=colors[1])),secondary_y=True,row=3,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT2 (deg F)'], mode = 'lines', name='CHT2', line=dict(color=colors[2])),secondary_y=True,row=3,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT3 (deg F)'], mode = 'lines', name='CHT3', line=dict(color=colors[3])),secondary_y=True,row=3,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT4 (deg F)'], mode = 'lines', name='CHT4', line=dict(color=colors[4])),secondary_y=True,row=3,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT5 (deg F)'], mode = 'lines', name='CHT5', line=dict(color=colors[5])),secondary_y=True,row=3,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT6 (deg F)'], mode = 'lines', name='CHT6', line=dict(color=colors[6])),secondary_y=True,row=3,col=1)
#

#Make plot for CHT vs Vertical Speed
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['Vertical Speed (ft/min)'], mode = 'lines', name='Vertical Speed (ft/min)', line=dict(color=colors[0])),secondary_y=False,row=4,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT1 (deg F)'], mode = 'lines', name='CHT1', line=dict(color=colors[1])),secondary_y=True,row=4,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT2 (deg F)'], mode = 'lines', name='CHT2', line=dict(color=colors[2])),secondary_y=True,row=4,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT3 (deg F)'], mode = 'lines', name='CHT3', line=dict(color=colors[3])),secondary_y=True,row=4,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT4 (deg F)'], mode = 'lines', name='CHT4', line=dict(color=colors[4])),secondary_y=True,row=4,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT5 (deg F)'], mode = 'lines', name='CHT5', line=dict(color=colors[5])),secondary_y=True,row=4,col=1)
fig.add_trace(go.Scatter(x=df['UTC Time (hh:mm:ss)'], y = df['CHT6 (deg F)'], mode = 'lines', name='CHT6', line=dict(color=colors[6])),secondary_y=True,row=4,col=1)
#

fig.update_layout(height=1000, width=1600, title_text="Engine Temps")

fig.show()




#app.run_server(debug=True)


