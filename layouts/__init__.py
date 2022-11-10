from dash import html, register_page, page_container

from .header_bar import build_header_bar
from .tab1_layout import build_tab1_content
from .tab2_layout import build_tab2_content
from .tab3_layout import build_tab3_content
from .tab4_layout import build_tab4_content
from .tab5_layout import build_tab5_content

def register_app_pages():
    register_page("tab1", name="Home", path='/', layout=build_tab1_content(), order=0)
    register_page("tab2", name="Tab2", path='/tab2', layout=build_tab2_content(), order=1)
    register_page("tab3", name="Tab3", path='/tab3', layout=build_tab3_content(), order=2)
    register_page("tab4", name="Tab4", path='/tab4', layout=build_tab4_content(), order=3)
    register_page("tab5", name="News", path='/news', layout=build_tab5_content(), order=4)
    
    
def Layout(app):

    return html.Div(id="main_div", children=[
                build_header_bar(app),
                html.Hr(),
                html.Div(id='second_div',children=[
                    page_container

                # END OF 2nd Division   
                    ])

                # END OF MAIN DIV
                ])

    