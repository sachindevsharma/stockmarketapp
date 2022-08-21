from dash import dcc, html
import dash_bootstrap_components as dbc
from assets import dropdown_values
from .main_page import build_main_page
from .tab1_layout import build_tab1_content
from .tab2_layout import build_tab2_content
from .tab3_layout import build_tab3_content
from .tab4_layout import build_tab4_content
from .tab5_layout import build_tab5_content

def build_banner():
    return  html.Div(id="banner", className="banner", children=[
                html.Div(id="banner-text", children=[
                        html.H5("Sachin's App"),
                        html.H6("Analysing Stocks"),
                        ]),
                html.Div(dcc.Dropdown(id='main_dropdown', 
                                      options= dropdown_values,
                                      optionHeight=30, 
                                      clearable=True, 
                                      placeholder='Select a Company')),
                html.Div(id="banner-logo", children=[
                        html.Button(id="learn-more-button", children="LEARN MORE", n_clicks=0),
                        ]),
            ])

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


def Layout(app):

    return html.Div(className="main_div", children=[
                build_main_page(),
                html.Div(id='second_div',children=[
                    build_tab1_content(app),
                    build_tab2_content(),
                    build_tab3_content(),
                    build_tab4_content(),
                    build_tab5_content(),

                # END OF 2nd Division   
                    ])

                # END OF MAIN DIV
                ])


            #dcc.Dropdown(id='main_dropdown', options= dropdown_values, clearable=True, placeholder='Select a Company'),
            # dcc.ConfirmDialogProvider(id='danger-danger', message='Danger danger! Are you sure you want to continue?',
            #     children=html.Button( 'Click Me', style={'float':'right'} )
            #         ),
    