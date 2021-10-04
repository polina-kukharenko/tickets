from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

from config import cache_config


app = Flask(__name__)
app.config.from_pyfile('config.py')
database = SQLAlchemy(app)
cache = Cache(config=cache_config)
cache.init_app(app)
