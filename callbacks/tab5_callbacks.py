from dash import html, dcc, Input, State, Output
import dash_bootstrap_components as dbc
from datetime import datetime
from helper_functions import *


def callbacks_tab5(app):
    @app.callback([Output('headlines', 'children'), Output('headlines_time', 'children')],
                 [Input('i5', 'n_intervals')])
    def get_headlines(n):
        headlines = get_top10_headlines()
        table = html.Table(className="table_news", children=[
                    html.Tr(children=[
                                html.Td(children=[
                                    html.A( className="td-link",
                                            children=i["description"],
                                            href=i["url"],
                                            target="_blank",)
                                    ])
                            ]) for i in headlines ])
        
        card = dbc.Card([
                # dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                dbc.CardBody([
                    html.H4("Card title", className="card-title"),
                    html.P(
                        "Some quick example text to build on the card title and "
                        "make up the bulk of the card's content.",
                        className="card-text",
                    ),
                    dbc.Button("Go somewhere", color="primary"),
                    ]
                ),
            ],
            style={"width": "18rem"},
        )

        return [card, "Last update : " + datetime.now().strftime("%H:%M:%S")]
