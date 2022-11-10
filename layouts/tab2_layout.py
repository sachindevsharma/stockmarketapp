from dash import html, dcc
from helper_functions import build_figure

def build_tab2_content():
    return html.Div(id='Tab2_div', children=[
                    build_graph()
            ])
    
def build_stock_details_div():
    return html.Div()
    
def build_graph():
    return html.Div(id='graph_tab2 m-4', children=build_figure("tab2"))

    
    
