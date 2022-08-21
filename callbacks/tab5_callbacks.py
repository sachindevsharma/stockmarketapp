from dash import html, dcc, Input, State, Output
import dash_bootstrap_components as dbc
from datetime import datetime
from helper_functions import *


def callbacks_tab5(app):
    @app.callback([Output('headlines', 'children'), Output('headlines_time', 'children')],
                 [Input('i60', 'n_intervals')])
    def get_headlines(n):
            headlines = get_top10_headlines()
        
            # source (id, author), author, title, description, url, urlToImage, , publishedAt, content
            urlToImage = headlines[0]
            
            card = dbc.Row([dbc.Card(className="card_div",  color="light", children=[
                        dbc.CardImg(src=item["urlToImage"], top=True),
                        dbc.CardBody([
                            html.H4(item["title"], className="card-title"),
                            html.P(item["description"], className="card-text"),
                            dbc.Button(dbc.CardLink("See News", href=item["url"], class_name="news_card_link"), color="primary"),
                        ]),
                    ], )
                    for item in headlines])

            return [card, "Last update : " + datetime.now().strftime("%H:%M:%S")]
