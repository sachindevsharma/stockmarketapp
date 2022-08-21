from dash import html, dcc

def build_tab2_content():
    return html.Div(id='Tab2_div', 
                    style={'display':'none'}, 
                    children=[
                        build_graph()
            ])
    
def build_graph():
    return html.Div(id='ind_tab2', children=[
                         dcc.Graph(id='stock_graph', config={'displayModeBar':False}),
                        #  dcc.Graph(id='indicator2', className='indicator', config={'displayModeBar':False})
                ])
