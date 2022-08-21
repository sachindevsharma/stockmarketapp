from dash import html, dcc

def build_tab5_content():
    return html.Div(id="news_div", children=[
        html.P(id="headlines_time"), 
        html.Div(id="headlines")
    ])

