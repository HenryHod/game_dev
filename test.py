import dash
from dash import dcc
from dash import html
from dash import Input, Output
import numpy as np
app = dash.Dash()
app.layout = html.Div([
    html.Div([
    html.Div(id="colorbox1", style={"width":"100px", "height":"100px", "background-color":"rgb(0, 0, 0)", "margin":"auto"}),
    html.Button(id="b1", children="button 1")], style={"margin":"auto"}, n_clicks=0),
    html.Div([
    html.Div(id="colorbox2", style={"width":"100px", "height":"100px", "background-color":"rgb(0, 0, 0)", "margin":"auto"}),
    html.Button(id="b2", children="button 2")], style={"margin":"auto"}, n_clicks=0),
    dcc.Store({})
], style={"display":"flex", "width":"250px", "margin":"auto"})

@app.callback(Output("b1", "n_clicks"),
              Output("b2", "n_clicks"),
              Output("colorbox1", "style"),
              Output("colorbox2", "style"),
              Input("b1", "n_clicks"),
              Input("b2", "n_clicks"),
              Input("colorbox1", "style"),
              Input("colorbox2", "style"))
def button_callback(n_clicks1, n_clicks2, style1, style2):
    style1["background-color"] = f"rgb({np.random.randint(0, 255)}, {np.random.randint(0, 255)}, {np.random.randint(0, 255)})"
    style2["background-color"] = f"rgb({np.random.randint(0, 255)}, {np.random.randint(0, 255)}, {np.random.randint(0, 255)})"
    return 0, 0, style1, style2
if __name__ == "__main__":
    app.run(debug=True)