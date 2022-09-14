from dash import Dash
import dash_bootstrap_components as dbc
import gunicorn                     #whilst your local machine's webserver doesn't need this, Heroku's linux webserver (i.e. dyno) does. I.e. This is your HTTP server
from whitenoise import WhiteNoise   #for serving static files on Heroku

from layouts import Layout
from callbacks import Callbacks
from sql import MongoConnector


client = MongoConnector().connect()

app = Dash(__name__, 
           update_title=None,
           title='Analysis', 
           external_stylesheets=[dbc.themes.BOOTSTRAP])

app.config["suppress_callback_exceptions"] = True

server = app.server 

# Enable Whitenoise for serving static files from Heroku (the /static folder is seen as root by Heroku) 
# server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/') 

app.layout = Layout(app)
Callbacks(app, client)

if __name__ == "__main__":
    app.run_server(debug=False, port=8050)