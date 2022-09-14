from dash.dependencies import Input, State, Output

from .tab1_callbacks import callbacks_tab1
from .tab2_callbacks import callbacks_tab2
from .tab5_callbacks import callbacks_tab5


def Callbacks(app, client):
    
    callbacks_tab1(app, client)
    callbacks_tab2(app)
    callbacks_tab5(app)

    @app.callback([Output('Tab1_div', 'style'),
                   Output('Tab2_div', 'style'),
                   Output('shareholder_portfolio_tab', 'style'),
                   Output('Tab4_div', 'style'),
                   Output('news_div', 'style')],
                  [Input('main_tabs', 'value')])
    def render_content(tab):
        n_tabs = 5
        return [{'dispaly':'block'} if i==int(tab[-1]) else {'display':'none'} for i in range(1, n_tabs+1)]
    