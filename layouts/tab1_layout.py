from dash import html, dcc
import dash_bootstrap_components as dbc
from helper_functions import build_figure


def build_tab1_content(app):
    
    return html.Div(id = "Tab1_div",children=[
            html.Div(className="div_left_panel", children=[
                build_top_movers_div(),
            ]), 
            html.Div(className="div_right_panel", children=[
                build_indicator_div(),
                build_chart_div()
            ])
        ])


def build_left_panel_header(app):
    return html.Div(className="div-info", children=[
                html.Img(className="logo", src=app.get_asset_url("dash-logo-new.png")),
                html.P(
                    """
                    This app continually queries csv files and updates Ask and Bid prices
                    for major currency pairs as well as Stock Charts. You can also virtually
                    buy and sell stocks and see the profit updates.
                    """
                        ),
            ])
    
    
def build_top_movers_div():
    return  html.Div(id='top_movers', children = [
                dbc.Row([
                    dbc.Col(html.H4("Top Gainers", className="top_movers_header")), 
                    dbc.Col(dbc.DropdownMenu(label="Market", size="sm", children=[
                            dbc.DropdownMenuItem("Nifty"),
                            dbc.DropdownMenuItem("Sensex"),
                    ])),
                ]),
                html.Div(id="top_gainers_div"), 
                dbc.Row([
                    dbc.Col(html.H4("Top Losers", className="top_movers_header")), 
                    dbc.Col(dbc.DropdownMenu(label="Market", size="sm", children=[
                            dbc.DropdownMenuItem("Nifty"),
                            dbc.DropdownMenuItem("Sensex"),
                    ])),
                ]),
                html.Div(id="top_losers_div")
                ])
    

def build_indicator_div():
    return html.Div(id='indicator_div', children=[
            dcc.Graph(id='indicator1', className='indicator', config={'displayModeBar':False}),
            dcc.Graph(id='indicator2', className='indicator', config={'displayModeBar':False}),
            dcc.Graph(id='indicator3', className='indicator', config={'displayModeBar':False}),
            dcc.Graph(id='indicator4', className='indicator', config={'displayModeBar':False})
                        ])


def build_chart_div():
    return html.Div(id='graph_tab1', children=build_figure("tab1"))
