from dash import html, dcc
import dash_bootstrap_components as dbc
from assets import studies_options, styles_options

def build_tab1_content(app):
    
    return html.Div(id = "Tab1_div",
                    children=[
                        build_left_panel(app),
                        build_right_panel(),
            
            # Hidden div that stores all clicked charts (EURUSD, USDCHF, etc.)
            # html.Div(id="charts_clicked", style={"display": "none"}),
            # Hidden div for each that stores orders
            # html.Div([html.Div(id="orders", style={"display": "none"}) for in currencies]),
            # html.Div([modal(pair) for in currencies]),
            # Hidden Div that stores all orders
            # html.Div(id="orders", style={"display": "none"}),
        ])

def build_left_panel(app):
    return  html.Div(className="div_left_panel", children=[
                # build_left_panel_header(app),
                build_top_movers_div(),
            ])

def build_right_panel():
    return  html.Div(className="div_right_panel", children=[
                build_indicator_div(),
                build_chart_div()
                # html.Div(id="top_bar", className="row div-top-bar", children=get_top_bar()),
                # html.Div(id="charts", className="row", children=[chart_div(pair) for in currencies]),
                # html.Div(id="bottom_panel", className="row div-bottom-panel", children=[
                #     html.Div(className="display-inlineblock", children=[
                #         dcc.Dropdown(id="dropdown_positions",className="bottom-dropdown",
                #                     options=[
                #                         {"label": "Open Positions", "value": "open"},
                #                         {"label": "Closed Positions", "value": "closed"},
                #                     ],
                #                     value="open",
                #                     clearable=False,
                #                     style={"border": "0px solid black"},
                #                 )
                #             ]),
                #     html.Div(className="display-inlineblock float-right", children=[
                #         dcc.Dropdown(id="closable_orders", className="bottom-dropdown", placeholder="Close order")
                #             ]),
                #     html.Div(id="orders_table", className="row table-orders"),
                # ]),
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

def build_headlines_div():
    return html.Div(className="div_news", children=[
                html.P(className="p_news", children="Headlines"),
                html.P(id = 'headlines_time_1', className="p_news float-right"),
                html.Div(id="headlines_1")
                ])

def build_indicator_div():
    return html.Div(id='indicator_div', children=[
            dcc.Graph(id='indicator1', className='indicator', config={'displayModeBar':False}),
            dcc.Graph(id='indicator2', className='indicator', config={'displayModeBar':False}),
            dcc.Graph(id='indicator3', className='indicator', config={'displayModeBar':False}),
            dcc.Graph(id='indicator4', className='indicator', config={'displayModeBar':False})
                        ])


def build_chart_div():
    
    studies_items = [dbc.DropdownMenuItem(i["label"]) for i in studies_options]
    styles_items = [dbc.DropdownMenuItem(i["label"]) for i in styles_options]
    return html.Div(id="graph_div", children=[
            html.Div(id="menu", className="not_visible m-4", children=[
                # Studies Checklist
                html.Span(id="menu_button", className="inline-block chart-title", children="☰",n_clicks=0),
                dbc.DropdownMenu(studies_items, id="studies_tab", className="graph_dropdown", 
                                 label="Studies", size="sm"),
                dbc.DropdownMenu(styles_items, id="style_tab", className="graph_dropdown", 
                                 label="Styles", size="sm"),
                ]),

            # Graph div
            html.Div(dcc.Graph(id="daily_chart", className="chart-graph", 
                                config={"displayModeBar": False, "scrollZoom": True},
                )),
            html.Div(dbc.Checklist(inline=True, options=[
                {"label": "Price", "value": 1},
                {"label": "50 DMA", "value": 2},
                {"label": "200 DMA", "value": 3},
                {"label": "50 EMA", "value": 4},
            ]))
        ])
