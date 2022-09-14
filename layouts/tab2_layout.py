from dash import html, dcc
from helper_functions import build_figure

def build_tab2_content():
    return html.Div(id='Tab2_div', style={'display':'none'}, children=[
                    build_graph()
            ])
    
def build_graph():
    return html.Div(id='graph_tab2 m-4', children=build_figure("tab2"))
    
    
