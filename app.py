import dash
from dash import html
import dash_bootstrap_components as dbc
# from aio.aio_components import ThemeChangerAIO
import gunicorn                     #whilst your local machine's webserver doesn't need this, Heroku's linux webserver (i.e. dyno) does. I.e. This is your HTTP server
from whitenoise import WhiteNoise   #for serving static files on Heroku

from layouts import Layout, register_app_pages
from callbacks import Callbacks
from sql import MongoConnector


client = MongoConnector().connect()
app = dash.Dash(__name__, 
           update_title=None,
           title='Analysis', 
           external_stylesheets=[dbc.themes.CERULEAN], 
           pages_folder="layouts",
           use_pages=True)

app.config["suppress_callback_exceptions"] = True
server = app.server 

# Enable Whitenoise for serving static files from Heroku (the /static folder is seen as root by Heroku) 
# server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/') 

register_app_pages()
app.layout = Layout(app)
Callbacks(app, client)

if __name__ == "__main__":
    app.run_server(debug=False, port=8050)