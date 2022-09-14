from dash import html

from .main_page import build_main_page
from .tab1_layout import build_tab1_content
from .tab2_layout import build_tab2_content
from .tab3_layout import build_tab3_content
from .tab4_layout import build_tab4_content
from .tab5_layout import build_tab5_content


def Layout(app):

    return html.Div(id="main_div", children=[
                build_main_page(app),
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
    