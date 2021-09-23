class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/tickets_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
