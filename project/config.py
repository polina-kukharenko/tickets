import os

from dotenv import load_dotenv

load_dotenv('.flaskenv')

os.getenv('DEBUG')
os.getenv('SQLALCHEMY_DATABASE_URI')
os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

cache_config = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_REDIS_HOST': os.getenv('CACHE_REDIS_HOST'),
    'CACHE_REDIS_PORT': os.getenv('CACHE_REDIS_PORT'),
}
