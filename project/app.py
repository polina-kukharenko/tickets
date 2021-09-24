from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
database = SQLAlchemy(app)
cache = Cache(config={'CACHE_TYPE': 'RedisCache', 'CACHE_REDIS_HOST': '0.0.0.0', 'CACHE_REDIS_PORT': 6379})
cache.init_app(app)
