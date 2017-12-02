from flask import Flask
import tmdbsimple as tmdb

app = Flask(__name__)
app.config.from_pyfile("../config.cfg")
CONFIG = app.config

tmdb.API_KEY = CONFIG['TMDB_KEY']
from . import views