from dash import html, dcc, dash_table, Input, State, Output
import plotly.graph_objs as go
from datetime import datetime
from nsetools import Nse
from helper_functions import *
nse = Nse()

loc = 'assets/images/'

def callbacks_tab1(app):

    @app.callback(Output('top_movers_content', 'children'),
                 [Input('top_movers_tab', 'value'), Input('i60', 'n_intervals')])
    def top_movers(tab, n):

        # if tab == 'tab1':
        #     top_movers = nse.get_top_gainers()[:5]
        # elif tab == 'tab2': 
        #     top_movers = nse.get_top_losers()[:5]
        top_movers = []
        header_color = '#45df7e' if tab=='tab1' else '#da5657'
        data, columns = format_top_movers(top_movers)
        return [dash_table.DataTable(columns=columns, 
                                     data=data, 
                                    #  style_table={'overflowX':'scroll'},
                                     style_header={'backgroundColor': header_color,},
                                     style_cell={'text-align':'center', 
                                                 'backgroundColor': plot_bg_color2, 
                                                 'color': text_color})]


    @app.callback([Output('indicator1','figure'), Output('indicator2','figure'),
                   Output('indicator3','figure'), Output('indicator4','figure')],
                  [Input('i1', 'n_intervals')])
    def indicators(n):
        #bg_color = '#30333d'
        bg_color = 'black'
        layout = {'autosize':True, 'margin':{'t': 20,'l':0,'b':0,'r':10}, 
                  'plot_bgcolor': bg_color, 'paper_bgcolor': bg_color}
        fig1 = {'data' : build_indicator('NIFTY', 14928, 14888, bg_color), 'layout': layout  }
        fig2 = {'data' : build_indicator('SENSEX', 50000, 49744, bg_color), 'layout': layout  }
        fig3 = {'data' : build_indicator('NIFTY BANK', 1200, 2300, bg_color), 'layout': layout  }
        fig4 = {'data' : build_indicator('NIFTY IT', 1200, 1100, bg_color), 'layout': layout  }

        return [fig1, fig2, fig3, fig4]


    
    
    # @app.callback(Output("orders_table", "children"),
    #              [Input("orders", "children"),
    #               Input("dropdown_positions", "value")])
    # def update_order_table(orders, position):
    #     headers = [
    #         "Order Id",
    #         "Time",
    #         "Type",
    #         "Volume",
    #         "Symbol",
    #         "TP",
    #         "SL",
    #         "Price",
    #         "Profit",
    #         "Status",
    #         "Close Time",
    #         "Close Price",
    #     ]

    #     # If there are no orders
    #     if orders is None or orders is "[]":
    #         return [
    #             html.Table(html.Tr(children=[html.Th(title) for title in headers])),
    #             html.Div(
    #                 className="text-center table-orders-empty",
    #                 children=[html.P("No " + position + " positions data row")],
    #             ),
    #         ]

    #     rows = []
    #     list_order = json.loads(orders)
    #     for order in list_order:
    #         tr_childs = []
    #         for attr in order:
    #             if str(order["status"]) == position:
    #                 tr_childs.append(html.Td(order[attr]))
    #         # Color row based on profitability of order
    #         if float(order["profit"]) >= 0:
    #             rows.append(html.Tr(className="profit", children=tr_childs))
    #         else:
    #             rows.append(html.Tr(className="no-profit", children=tr_childs))

    #     return html.Table(children=[html.Tr([html.Th(title) for title in headers])] + rows)


    # # Update Options in dropdown for Open and Close positions
    # @app.callback(Output("dropdown_positions", "options"), 
    #               [Input("orders", "children")])
    # def update_positions_dropdown(orders):
    #     closeOrders = 0
    #     openOrders = 0
    #     if orders is not None:
    #         orders = json.loads(orders)
    #         for order in orders:
    #             if order["status"] == "closed":
    #                 closeOrders += 1
    #             if order["status"] == "open":
    #                 openOrders += 1
    #     return [
    #         {"label": "Open positions (" + str(openOrders) + ")", "value": "open"},
    #         {"label": "Closed positions (" + str(closeOrders) + ")", "value": "closed"},
    #     ]


    # # Callback to close orders from dropdown options
    # @app.callback(Output("closable_orders", "options"), [Input("orders", "children")])
    # def update_close_dropdown(orders):
    #     options = []
    #     if orders is not None:
    #         orders = json.loads(orders)
    #         for order in orders:
    #             if order["status"] == "open":
    #                 options.append({"label": order["id"], "value": order["id"]})
    #     return options


    # # Callback to update Top Bar values
    # @app.callback(Output("top_bar", "children"), [Input("orders", "children")])
    # def update_top_bar(orders):
    #     if orders is None or orders is "[]":
    #         return get_top_bar()

    #     orders = json.loads(orders)
    #     open_pl = 0
    #     balance = 50000
    #     free_margin = 50000
    #     margin = 0

    #     for order in orders:
    #         if order["status"] == "open":
    #             open_pl += float(order["profit"])
    #             conversion_price = (
    #                 1 if order["symbol"][:3] == "USD" else float(order["price"])
    #             )
    #             margin += (float(order["volume"]) * 100000) / (200 * conversion_price)
    #         else:
    #             balance += float(order["profit"])

    #     equity = balance - open_pl
    #     free_margin = equity - margin
    #     margin_level = "%" if margin == 0 else "%2.F" % ((equity / margin) * 100) + "%"
    #     equity = "%.2F" % equity
    #     balance = "%.2F" % balance
    #     open_pl = "%.2F" % open_pl
    #     free_margin = "%.2F" % free_margin
    #     margin = "%2.F" % margin

    #     return get_top_bar(balance, equity, margin, free_margin, margin_level, open_pl)


    # # Callback to update live clock
    # @app.callback(Output("live_clock", "children"), [Input("interval", "n_intervals")])
    # def update_time(n):
    #     return datetime.datetime.now().strftime("%H:%M:%S")


    # # Callback to update news
    # @app.callback(Output("news", "children"), [Input("i_news", "n_intervals")])
    # def update_news_div(n):
    #     return update_news()

