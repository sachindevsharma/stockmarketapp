from dash import html, dcc

def build_tab3_content():
    return html.Div(id='shareholder_portfolio_tab', style={'display':'none'}, children = [
                html.Iframe(src="https://trendlyne.com/portfolio/superstar-shareholders/178317/latest/radhakishan-damani-portfolio/",
                            style={"height": "1067px", "width": "100%"}),
            ])