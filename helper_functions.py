import requests
import plotly.graph_objs as go
from plotly.subplots import make_subplots


paper_bg_color = '#1a1c23'
plot_bg_color  = '#30333d'
plot_bg_color2 = '#22252b'
header_color   = '#b2b2b2'
text_color     = '#ededed'


dropdown_values = [
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ]

def format_top_movers(data):
    '''formatting the top movers data'''
    
    columns =  [{'name':'SYMBOL', 'id':'symbol'},
                {'name':'LTP', 'id':'ltp'},
                {'name':'Change', 'id':'change'},
                {'name':'%Change', 'id':'netPrice'}]

    for i in data:
        i['netPrice'] = str(i['netPrice']) + '%'
    return data, columns



# API Call to update news
def get_top10_headlines():
    url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=da8e2e705b914f9f86ed2e9692e66012"
    news_requests = requests.get(url)
    json_data = news_requests.json()["articles"][:10]
    return json_data


def build_indicator(text, value, reference, background_color):

    # the first two traces are just the delta with the value set to the background color
    trace1 = go.Indicator(
        mode = "number+delta", 
        value = value, 
        delta = {'reference':reference, 'position':'bottom', 'relative':False, 'font':{'size':15}, 'valueformat':'.2f'},
        number = {'font': {'color':background_color}},
        domain = {'x': [0, 0.6], 'y': [0, 1]},
    )

    trace2 = go.Indicator(
        mode = "number+delta", 
        value = value, 
        delta = {'reference':reference, 'position':'bottom', 'relative':True, 'font':{'size':15},
                 'valueformat':',.2%', 'increasing':{'symbol':' '}, 'decreasing':{'symbol':' '}},
        number = {'font': {'color':background_color}},
        domain = {'x': [0.4, 1], 'y': [0, 1]}, 
    )

    ## this adds the title and value
    trace3 = go.Indicator(mode = "number", 
        value = value, 
        number = {'font': {'size': 30, 'color':text_color}, 'valueformat':'.2f'},
        title = {'text': text, 'font':{'size':20, 'color': header_color}},
        domain = {'x': [0, 1], 'y': [0, 1]}
    )

    #fig.update_layout(autosize=True, margin={'t': 20,'l':0,'b':0,'r':10})
    return [trace1, trace2, trace3]

def generate_figure(currency_pair, ask, bid, type_trace, studies, period):
    # Get OHLC data
    data_frame = currency_pair_data[currency_pair]
    t = datetime.datetime.now()
    data = data_frame.loc[
        : t.strftime("2016-01-05 %H:%M:%S" )  # all the data from the beginning until current time
    ]
    data_bid = data["Bid"]
    df = data_bid.resample(period).ohlc()

    subplot_traces = [  # first row traces
        "accumulation_trace",
        "cci_trace",
        "roc_trace",
        "stoc_trace",
        "mom_trace",
    ]
    selected_subplots_studies = []
    selected_first_row_studies = []
    row = 1  # number of subplots

    if studies:
        for study in studies:
            if study in subplot_traces:
                row += 1  # increment number of rows only if the study needs a subplot
                selected_subplots_studies.append(study)
            else:
                selected_first_row_studies.append(study)

    fig = make_subplots(
        rows=row,
        shared_xaxes=True,
        shared_yaxes=True,
        cols=1,
        print_grid=False,
        vertical_spacing=0.12,
    )

    # Add main trace (style) to figure
    fig.append_trace(eval(type_trace)(df), 1, 1)

    # Add trace(s) on fig's first row
    for study in selected_first_row_studies:
        fig = eval(study)(df, fig)

    row = 1
    # Plot trace on new row
    for study in selected_subplots_studies:
        row += 1
        fig.append_trace(eval(study)(df), row, 1)

    fig["layout"][
        "uirevision"
    ] = "The User is always right"  # Ensures zoom on graph is the same on update
    fig["layout"]["margin"] = {"t": 50, "l": 50, "b": 50, "r": 25}
    fig["layout"]["autosize"] = True
    fig["layout"]["height"] = 400
    fig["layout"]["xaxis"]["rangeslider"]["visible"] = False
    fig["layout"]["xaxis"]["tickformat"] = "%H:%M"
    fig["layout"]["yaxis"]["showgrid"] = True
    fig["layout"]["yaxis"]["gridcolor"] = "#3E3F40"
    fig["layout"]["yaxis"]["gridwidth"] = 1
    fig["layout"].update(paper_bgcolor="#21252C", plot_bgcolor="#21252C")

    return fig

