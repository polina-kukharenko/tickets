from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
cache = Cache(app, config={'CACHE_TYPE': 'redis'})
database = SQLAlchemy(app)
