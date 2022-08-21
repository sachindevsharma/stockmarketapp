from dash import html, dcc
import dash_bootstrap_components as dbc
from assets import studies_options, styles_options

def build_tab1_content(app):
    
    return html.Div(id = "Tab1_div",#  className="second_div", 
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
                build_left_panel_header(app),
                build_top_movers_div(),
                # build_headlines_div()
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
                html.Div(dcc.Tabs(id='top_movers_tab', value = 'tab1', children=[
                                        dcc.Tab(label='Gainers', value='tab1', selected_style={'backgroundColor':'#45df7e'}),
                                        dcc.Tab(label='Losers',  value='tab2', selected_style={'backgroundColor':'#da5657'})])),
                html.Div(id='top_movers_content')
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
#     return html.Div(dcc.Graph(id="daily_chart",
#                               config={"displayModeBar": False, "scrollZoom": True},
#                 ))

    studies_items = [dbc.DropdownMenuItem(i["label"]) for i in studies_options]
    styles_items = [dbc.DropdownMenuItem(i["label"]) for i in styles_options]
    return html.Div(id="graph_div", children=[
            # Menu for Currency Graph
            html.Div(id="menu", className="not_visible", children=[
                # stores current menu tab
                html.Div(id="menu_tab", children=["Studies"], style={"display": "none"} ),
                html.Span( "Style ", id="style_header", className="span-menu", n_clicks_timestamp=2),
                html.Span("Studies ", id="studies_header", className="span-menu", n_clicks_timestamp=1),
                # Studies Checklist
                html.Span(id="menu_button", className="inline-block chart-title", children="☰",n_clicks=0),
                html.Div(id="studies_tab",children=[
                        dbc.DropdownMenu(studies_items, label="Studies", size="sm", id="studies", className="graph_dropdown")
                    ]),
                # Styles checklist
                html.Div(id="style_tab", children=[
                    dbc.DropdownMenu(styles_items, label="Styles", size="sm", id="chart_type", className="graph_dropdown")
                    ]),
                ]),
            # Chart Top Bar
            html.Div(className="row chart-top-bar", children=[
                
                # Dropdown and close button float right
                html.Div(className="graph-top-right inline-block", children=[
                    html.Div(className="inline-block", children=[
                        dcc.Dropdown(className="graph_dropdown", id="dropdown_period", 
                                        value="15Min", clearable=False, options=[
                                {"label": "5 min", "value": "5Min"},
                                {"label": "15 min", "value": "15Min"},
                                {"label": "30 min", "value": "30Min"},
                                    ])
                            ]),
                #     html.Span(id="close", className="chart-close inline-block float-right",
                #             children="×", n_clicks=0),
                    ]),
            ]),
            # Graph div
            html.Div(dcc.Graph(id="chart",className="chart-graph", 
                                config={"displayModeBar": False, "scrollZoom": True},
                )),
        ])
