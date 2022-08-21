from dash import dcc, html
import dash_bootstrap_components as dbc
from assets import dropdown_values


def build_main_page():
    return html.Div(className="header_div", children=[
        build_banner(),
        build_tabs(),
        build_intervals_div()
    ])
    
def build_banner():
    PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
    return dbc.Navbar(dbc.Container([
        # dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px", width="30px")),
        dbc.Col(dbc.NavbarBrand("Dashboard", href="#"), sm=3, md=2),
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
        dbc.Col(
            dbc.Nav(dbc.Container(dbc.NavItem(dbc.NavLink("Sign out"))), navbar=True, ),
            width="auto",
        ),
        ]), 
        color="dark", dark=True)



    # return  html.Div(id="banner", className="banner", children=[
    #             html.Div(id="banner-text", children=[
    #                     html.H5("Sachin's App"),
    #                     html.H6("Analysing Stocks"),
    #                     ]),
    #             html.Div(dcc.Dropdown(id='main_dropdown', 
    #                                   options= dropdown_values,
    #                                   optionHeight=30, 
    #                                   clearable=True, 
    #                                   placeholder='Select a Company')),
    #             html.Div(id="banner-logo", children=[
    #                     html.Button(id="learn-more-button", children="LEARN MORE", n_clicks=0),
    #                     ]),
    #         ])

def build_tabs():
    return html.Div(id="tabs", className="tabs", children=[
                dcc.Tabs(id='main_tabs', value = 'tab1', children=[
                        dcc.Tab(label='HOME', value='tab1'),
                        dcc.Tab(label='Tab 2', value='tab2'),
                        dcc.Tab(label="Shareholder's PortFolio", value='tab3'),
                        dcc.Tab(label='ABOUT', value='tab4'),
                        dcc.Tab(label='News', value='tab5'),
                        dcc.Tab(label='Tab 6', value='tab6'),
                        ]),
                ])
    
def build_intervals_div():
    return html.Div(id='interval_div', children=[
        dcc.Interval(id="i1", interval=1 * 1000, n_intervals=0),
        dcc.Interval(id="i2", interval=1 * 2000, n_intervals=0),
        dcc.Interval(id="i5", interval=1 * 5000, n_intervals=0),
        dcc.Interval(id="i60", interval=1 * 60000, n_intervals=0),
    ])


