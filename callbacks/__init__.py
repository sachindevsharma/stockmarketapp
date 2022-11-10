import dash
from dash import Input, State, Output, ctx

from .tab1_callbacks import callbacks_tab1
from .tab2_callbacks import callbacks_tab2
from .tab5_callbacks import callbacks_tab5


def Callbacks(app, client):
    
    callbacks_tab1(app, client)
    callbacks_tab2(app)
    callbacks_tab5(app)
    
    # @app.callback(output=[Output("tab1", "active"), Output("tab2", "active") ],
    #               input=[Input("tab1", "n_clicks"), Input("tab2", "n_clicks") ]
    #               )
    # def show_active(n1, n2):
    #     # print(args)
    #     button_id = ctx.triggered_id if not None else 'No clicks yet'
    #     return [True, False]    

    