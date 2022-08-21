from dash import Input, State, Output
import plotly.graph_objects as go
from nsetools import Nse
import pandas as pd 
nse = Nse()

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')


def callbacks_tab2(app):

    @app.callback([Output('stock_graph','figure')],
                  [Input('main_tabs', 'value')])
    def stock_graph(n):
        
        xaxis = dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1Y", step="year", stepmode="backward"),
                    dict(count=2, label="2Y", step="year", stepmode="backward"),
                    dict(count=5, label="5Y", step="year", stepmode="backward"),
                    dict(label="Max", step="all")
                ])
            )
        )
        # autosize=True, , 
        layout = go.Layout(xaxis = xaxis, margin={'t': 40,'l':30,'b':20,'r':15})
        
        fig = {'data' : [go.Scatter(x=df.Date, y=df["AAPL.High"])],
               'layout': layout
            }
        
        # layout.update_yaxes(
            # fixedrange=True
        # )

        return [fig]
        

            